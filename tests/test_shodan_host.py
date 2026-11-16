
import json
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

# Locate the project's .env file.
project_dir = Path(__file__).resolve().parent.parent
env_file = project_dir / ".env"

# Load the Shodan API key.
api_key = None

for line in env_file.read_text().splitlines():
    if line.startswith("SHODAN_API_KEY="):
        api_key = line.split("=", 1)[1].strip()
        break

if not api_key:
    raise SystemExit("ERROR: Shodan API key is missing.")

# Public IP used for testing.
test_ip = "8.8.8.8"

# Construct the Shodan host-information URL.
base_url = f"https://api.shodan.io/shodan/host/{test_ip}"
query = urllib.parse.urlencode({"key": api_key})
url = f"{base_url}?{query}"

try:
    with urllib.request.urlopen(url, timeout=10) as response:
        data = json.load(response)

    print("SUCCESS: Shodan host lookup completed.")
    print("IP Address:", data.get("ip_str"))
    print("Organization:", data.get("org"))
    print("ASN:", data.get("asn"))
    print("Observed Ports:", data.get("ports", []))

except urllib.error.HTTPError as error:
    print("HTTP error:", error.code)

except urllib.error.URLError:
    print("ERROR: Unable to connect to Shodan.")

except TimeoutError:
    print("ERROR: Shodan request timed out.")

except json.JSONDecodeError:
    print("ERROR: Invalid JSON response.")
