
import sys
from pathlib import Path

# Allow Python to import modules from the project root.
project_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_dir))

from threat_intelligence import is_enrichment_eligible


test_ips = [
    "8.8.8.8",
    "192.168.1.1",
    "127.0.0.1",
    "192.0.2.10",
    "999.999.999.999"
]

for ip in test_ips:
    result = is_enrichment_eligible(ip)
    print(f"{ip}: {result}")
