
import sys
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_dir))

from threat_intelligence import lookup_otx


test_ips = [
    "8.8.8.8",
    "192.168.1.1",
    "192.0.2.10"
]


for ip in test_ips:
    result = lookup_otx(ip)

    print(f"\nIP: {ip}")
    print("Status:", result["status"])
    print("Source:", result["source"])

    if result["status"] == "success":
        print("ASN:", result.get("asn"))
        print("Reputation:", result.get("reputation"))
        print("Pulse Count:", result.get("pulse_count"))

    if "reason" in result:
        print("Reason:", result["reason"])
