
import sys
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_dir))

from threat_intelligence import lookup_shodan

test_ips = [
    "8.8.8.8",
    "192.168.1.1",
    "192.0.2.10"
]

for ip in test_ips:
    result = lookup_shodan(ip)

    print(f"\nIP: {ip}")
    print("Status:", result["status"])
    print("Source:", result["source"])

    if result["status"] == "success":
        print("Organization:", result.get("organization"))
        print("ASN:", result.get("asn"))
        print("Observed Ports:", result.get("ports"))

    if "reason" in result:
        print("Reason:", result["reason"])
