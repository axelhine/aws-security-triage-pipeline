
# Milestone 2 — IOC Validation Test Results

## Objective
Verify that the Python IOC validator correctly identifies valid and invalid IPv4 addresses.

## Test Cases

| Test ID | Input | Expected | Actual | Status |
|---|---|---|---|---|
| TC-01 | 192.0.2.10 | True | True | PASS |
| TC-02 | 999.999.999.999 | False | False | PASS |
| TC-03 | 198.51.100.25 | True | True | PASS |
| TC-04 | hello.world | False | False | PASS |
| TC-05 | Empty string | False | False | PASS |

## Findings
All five initial IPv4 validation tests passed.

The validator correctly accepted valid IPv4 addresses and rejected malformed addresses, non-IP strings, and empty input.

## Limitations
- Only IPv4 addresses are currently supported.
- IP validation does not determine whether an address is malicious.
- Integration with the main alert processor is not yet complete.

## Conclusion
The initial IPv4 validation functionality passed all five tests. Further development will focus on integration with the main security alert processor.

## Integration Testing — Issue #2

### Objective
Verify that main.py successfully imports the IOC
validator and validates IP addresses extracted
from alert.json.

| Test ID | Test Case | Expected Result | Status |
|---|---|---|---|
| TC-06 | Valid source and destination IPs | Both VALID | PASS |
| TC-07 | Invalid source IP | Source INVALID | PASS |
| TC-08 | Existing severity classification | Classification still works | PASS |

### Findings
To be completed after testing.

### Conclusion
To be completed after testing.

## IP Classification Testing — Issue #3

### Objective
Verify that the IOC validator correctly classifies
different types of IPv4 addresses.

| Test ID | Input | Expected | Actual | Status |
|---|---|---|---|---|
| TC-09 | 192.168.1.10 | PRIVATE | PRIVATE | PASS |
| TC-10 | 8.8.8.8 | GLOBAL | GLOBAL | PASS |
| TC-11 | 127.0.0.1 | LOOPBACK | LOOPBACK | PASS |
| TC-12 | 192.0.2.10 | DOCUMENTATION | DOCUMENTATION | PASS |
| TC-13 | 999.999.999.999 | INVALID | INVALID | PASS |

### Findings
All five initial IP classification tests passed.

The classifier correctly distinguished private,
globally reachable, loopback, documentation,
and invalid IPv4 addresses.

### Limitations
- Only IPv4 addresses are supported.
- Classification does not determine maliciousness.
- Additional special-use address categories exist.

### Conclusion
The classifier produced the expected results
for all five tested inputs.

## Missing Field Handling — TC-14

### Objective
Verify that the alert processor handles a missing
source_ip field without crashing.

| Test ID | Test Case | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC-14 | Missing source_ip | INVALID without crashing | INVALID without crashing | PASS |

### Findings
The alert processor handled a missing source_ip
field without raising a KeyError.

The IOC validator classified the missing
address as INVALID.

### Conclusion
The pipeline successfully handled an incomplete
JSON alert while preserving its reporting functionality.
