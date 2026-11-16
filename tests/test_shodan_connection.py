
import os
from pathlib import Path

# Locate the project's root directory.
project_dir = Path(__file__).resolve().parent.parent

# Locate the environment file.
env_file = project_dir / ".env"

# Read the Shodan API key.
for line in env_file.read_text().splitlines():
    if line.startswith("SHODAN_API_KEY="):
        os.environ["SHODAN_API_KEY"] = line.split("=", 1)[1].strip()
        break

# Retrieve the key from the environment.
api_key = os.getenv("SHODAN_API_KEY")

# Verify that the key exists.
if not api_key:
    raise SystemExit("ERROR: Shodan API key is missing.")

print("SUCCESS: Shodan API key loaded.")
