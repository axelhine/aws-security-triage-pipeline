
import os
from pathlib import Path

# Locate the project's root directory.
project_dir = Path(__file__).resolve().parent.parent

# Locate the local environment file.
env_file = project_dir / ".env"

# Read the environment file without printing secrets.
for line in env_file.read_text().splitlines():
    if line.startswith("OTX_API_KEY="):
        os.environ["OTX_API_KEY"] = line.split("=", 1)[1].strip()
        break

# Check whether the API key was loaded.
api_key = os.getenv("OTX_API_KEY")

if api_key:
    print("SUCCESS: OTX API key loaded.")
else:
    print("ERROR: OTX API key not found.")
