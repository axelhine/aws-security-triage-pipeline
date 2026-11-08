
import json

# Open the simulated security alert
with open("alert.json", "r") as file:
    alert = json.load(file)

# Extract important information
incident_id = alert["incident_id"]
severity = alert["severity"]
source_ip = alert["source_ip"]
destination_ip = alert["destination_ip"]

# Display the alert summary
print("=== SECURITY ALERT REPORT ===")
print("Incident ID:", incident_id)
print("Severity:", severity)
print("Source IP:", source_ip)
print("Destination IP:", destination_ip)
print("=============================")
