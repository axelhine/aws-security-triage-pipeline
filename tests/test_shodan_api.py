
import json
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

# Locate the project directory and .env file.
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

# Construct the Shodan account information endpoint.
base_url = "https://api.shodan.io/api-info"

# Encode the API key as a URL query parameter.
query = urllib.parse.urlencode({"key": api_key})
url = f"{base_url}?{query}"

try:
    # Send the HTTPS request.
    with urllib.request.urlopen(url, timeout=10) as response:
        data = json.load(response)

    print("SUCCESS: Shodan API request completed.")

    # Display non-sensitive account information.
    print("Plan:", data.get("plan"))
    print("Query credits:", data.get("query_credits"))
    print("Scan credits:", data.get("scan_credits"))

except urllib.error.HTTPError as error:
    print("HTTP error:", error.code)

except urllib.error.URLError:
    print("ERROR: Unable to connect to Shodan.")

except TimeoutError:
    print("ERROR: Shodan request timed out.")

except json.JSONDecodeError:
    print("ERROR: Shodan returned invalid JSON.")
