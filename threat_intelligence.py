
import ipaddress
import json
import os
import urllib.request
import urllib.error
import urllib.parse


def is_enrichment_eligible(ip_address):
    """
    Determine whether an IPv4 address is eligible
    for external threat intelligence enrichment.
    """

    try:
        ip = ipaddress.IPv4Address(ip_address)
        return ip.is_global

    except (ipaddress.AddressValueError, TypeError):
        return False


def lookup_otx(ip_address):
    """
    Retrieve threat intelligence from AlienVault OTX.
    """

    # Reject IPs that should not be sent to external APIs.
    if not is_enrichment_eligible(ip_address):
        return {
            "ip": ip_address,
            "source": "OTX",
            "status": "skipped",
            "reason": "IP address is not eligible for enrichment"
        }

    # Retrieve the API key from the environment.
    api_key = os.getenv("OTX_API_KEY")

    if not api_key:
        return {
            "ip": ip_address,
            "source": "OTX",
            "status": "error",
            "reason": "OTX API key is not configured"
        }

    # Construct the OTX endpoint.
    url = (
        "https://otx.alienvault.com/api/v1/"
        f"indicators/IPv4/{ip_address}/general"
    )

    request = urllib.request.Request(
        url,
        headers={"X-OTX-API-KEY": api_key}
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            data = json.load(response)

        pulse_info = data.get("pulse_info") or {}

        return {
            "ip": ip_address,
            "source": "OTX",
            "status": "success",
            "asn": data.get("asn"),
            "reputation": data.get("reputation"),
            "pulse_count": pulse_info.get("count")
        }

    except urllib.error.HTTPError as error:
        return {
            "ip": ip_address,
            "source": "OTX",
            "status": "error",
            "reason": f"HTTP error {error.code}"
        }

    except (urllib.error.URLError, TimeoutError):
        return {
            "ip": ip_address,
            "source": "OTX",
            "status": "error",
            "reason": "Connection failed or timed out"
        }

    except (json.JSONDecodeError, TypeError, AttributeError):
        return {
            "ip": ip_address,
            "source": "OTX",
            "status": "error",
            "reason": "Invalid OTX response"
        }

def lookup_shodan(ip_address):
    """
    Retrieve existing Shodan host observations
    for an eligible public IPv4 address.
    """

    if not is_enrichment_eligible(ip_address):
        return {
            "ip": ip_address,
            "source": "Shodan",
            "status": "skipped",
            "reason": "IP address is not eligible for enrichment"
        }

    api_key = os.getenv("SHODAN_API_KEY")

    if not api_key:
        return {
            "ip": ip_address,
            "source": "Shodan",
            "status": "error",
            "reason": "Shodan API key is not configured"
        }

    base_url = f"https://api.shodan.io/shodan/host/{ip_address}"
    query = urllib.parse.urlencode({"key": api_key})
    url = f"{base_url}?{query}"

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.load(response)

        return {
            "ip": ip_address,
            "source": "Shodan",
            "status": "success",
            "organization": data.get("org"),
            "asn": data.get("asn"),
            "ports": data.get("ports", [])
        }

    except urllib.error.HTTPError as error:
        return {
            "ip": ip_address,
            "source": "Shodan",
            "status": "error",
            "reason": f"HTTP error {error.code}"
        }

    except (urllib.error.URLError, TimeoutError):
        return {
            "ip": ip_address,
            "source": "Shodan",
            "status": "error",
            "reason": "Connection failed or timed out"
        }

    except (json.JSONDecodeError, TypeError, AttributeError):
        return {
            "ip": ip_address,
            "source": "Shodan",
            "status": "error",
            "reason": "Invalid Shodan response"
        }

def enrich_ip(ip_address):
    """
    Combine AlienVault OTX and Shodan intelligence
    for a single IPv4 address.
    """

    if not is_enrichment_eligible(ip_address):
        return {
            "ip": ip_address,
            "status": "skipped",
            "reason": "IP address is not eligible for enrichment",
            "otx": None,
            "shodan": None
        }

    otx_result = lookup_otx(ip_address)
    shodan_result = lookup_shodan(ip_address)

    # Determine whether each provider succeeded.
    otx_success = otx_result.get("status") == "success"
    shodan_success = shodan_result.get("status") == "success"

    # Classify the overall enrichment result.
    if otx_success and shodan_success:
        overall_status = "success"

    elif otx_success or shodan_success:
        overall_status = "partial"

    else:
        overall_status = "error"

    

    return {
        "ip": ip_address,
        "status": overall_status,
        "otx": otx_result,
        "shodan": shodan_result
    }
