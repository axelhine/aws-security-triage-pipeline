
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
| TC-06 | Valid source and destination IPs | Both VALID | Pending |
| TC-07 | Invalid source IP | Source INVALID | Pending |
| TC-08 | Existing severity classification | Classification still works | Pending |

### Findings
To be completed after testing.

### Conclusion
To be completed after testing.
