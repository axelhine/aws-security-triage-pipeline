
import os
import json
import urllib.request
import urllib.error
from pathlib import Path

# Find the project root.
project_dir = Path(__file__).resolve().parent.parent

# Load the API key from .env.
env_file = project_dir / ".env"

for line in env_file.read_text().splitlines():
    if line.startswith("OTX_API_KEY="):
        os.environ["OTX_API_KEY"] = line.split("=", 1)[1].strip()
        break

api_key = os.getenv("OTX_API_KEY")

if not api_key:
    raise SystemExit("ERROR: OTX API key is missing.")

# Use a public IP for a basic connectivity test.
test_ip = "8.8.8.8"

url = (
    f"https://otx.alienvault.com/api/v1/"
    f"indicators/IPv4/{test_ip}/general"
)

# Construct the authenticated HTTP request.
request = urllib.request.Request(
    url,
    headers={"X-OTX-API-KEY": api_key}
)


try:
    with urllib.request.urlopen(request, timeout=10) as response:
        data = json.load(response)

    print("SUCCESS: OTX API request completed.")
    print("Indicator:", data.get("indicator"))
    print("Associated Pulses:", data.get("pulse_info", {}).get("count"))

    # Display available JSON fields after a successful response.
    print("\n=== AVAILABLE OTX RESPONSE FIELDS ===")

    for field in data.keys():
        print(field)

    print("\n=== SELECTED OTX INTELLIGENCE ===")
    print("Indicator:", data.get("indicator"))
    print("ASN:", data.get("asn"))
    print("Reputation:", data.get("reputation"))

    pulse_info = data.get("pulse_info") or {}

    print("Pulse Count:", pulse_info.get("count"))

except urllib.error.HTTPError as error:
    print("HTTP error:", error.code)

except urllib.error.URLError:
    print("ERROR: Unable to connect to OTX.")

except TimeoutError:
    print("ERROR: OTX request timed out.")
