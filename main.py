

import json
import sys
from ioc_validator import validate_ip, classify_ip

# Attempt to load the security alert
try:
    with open("alert.json", "r") as file:
        alert = json.load(file)

except FileNotFoundError:
    print("ERROR: alert.json could not be found.")
    sys.exit(1)

except json.JSONDecodeError:
    print("ERROR: alert.json contains invalid JSON.")
    sys.exit(1)

# Verify the alert contains a JSON object
if not isinstance(alert, dict):
    print("ERROR: Expected a JSON object.")
    sys.exit(1)

# Extract important information
incident_id = alert.get("incident_id", "UNKNOWN")
severity = alert.get("severity", "UNKNOWN")
source_ip = alert.get("source_ip")
destination_ip = alert.get("destination_ip")


# Display the alert summary
print("=== SECURITY ALERT REPORT ===")
print("Incident ID:", incident_id)
print("Severity:", severity)
print("Source IP:", source_ip)
print("Destination IP:", destination_ip)
print("=============================")

# Validate IP addresses extracted from the alert
print("\n=== IOC VALIDATION ===")

if validate_ip(source_ip):
    print("Source IP: VALID")
else:
    print("Source IP: INVALID")

if validate_ip(destination_ip):
    print("Destination IP: VALID")
else:
    print("Destination IP: INVALID")

# Classify IP addresses
print("\n=== IP CLASSIFICATION ===")

print("Source IP:", source_ip)
print("Classification:", classify_ip(source_ip))

print("\nDestination IP:", destination_ip)
print("Classification:", classify_ip(destination_ip))

print("=========================")

# Evaluate the alert's reported severity
print("\n=== INITIAL ALERT CLASSIFICATION ===")

if severity == "HIGH":
    print("Priority: HIGH")
    print("Action: Security analyst review recommended.")

elif severity == "MEDIUM":
    print("Priority: MEDIUM")
    print("Action: Review when possible.")

elif severity == "LOW":
    print("Priority: LOW")
    print("Action: Record for routine monitoring.")

else:
    print("Priority: UNKNOWN")
    print("Action: Verify the alert's severity.")

print("Destination IP:", destination_ip)
print("=============================")

