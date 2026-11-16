
import sys
from pathlib import Path

# Locate the project's root directory.
project_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_dir))

from threat_intelligence import enrich_ip

# Test one public IP and two ineligible IPs.
test_ips = [
    "8.8.8.8",
    "192.168.1.1",
    "192.0.2.10"
]

for ip in test_ips:
    result = enrich_ip(ip)

    print(f"\n=== Enrichment for {ip} ===")
    print("Overall Status:", result["status"])

    # Display provider results whenever enrichment was attempted.
    if result["status"] in ("success", "partial", "error"):
        print("OTX:", result["otx"])
        print("Shodan:", result["shodan"])

    # Explain why enrichment was skipped, if applicable.
    if "reason" in result:
        print("Reason:", result["reason"])
