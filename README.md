# Automated Security Alert & IOC Triage Pipeline

**Project Status:** In Development — Milestones 1 & 2 Completed  
**Project Type:** Cybersecurity | Cloud Security | Security Automation  
**Technologies:** Python, JSON, Git, GitHub, Python `ipaddress` Library  
**Planned Technologies:** AWS Lambda, Amazon S3, Amazon DynamoDB, Amazon VPC Flow Logs, AWS IAM

---

## Project Overview

This project focuses on developing an automated security alert processing and Indicator of Compromise (IOC) triage pipeline using Python and Amazon Web Services (AWS).

The long-term objective is to build a serverless security pipeline capable of processing security alerts generated from authorized AWS environments, extracting relevant indicators, enriching them with threat intelligence, assessing potential security risks, and generating structured incident reports.

Development follows an incremental, milestone-based approach emphasizing practical cybersecurity knowledge, programming skills, cloud security, testing, and technical documentation.

**Current implementation:** A local Python application that processes simulated JSON security alerts, validates and classifies IPv4 addresses, and evaluates reported alert severity.

The application does not currently determine whether an indicator is malicious.

## Project Objectives

- Understand security monitoring and incident triage workflows.
- Develop Python programming skills through cybersecurity applications.
- Extract and validate indicators from structured security alerts.
- Classify IPv4 addresses according to network characteristics.
- Implement external threat intelligence enrichment.
- Develop evidence-based risk scoring and automated triage.
- Integrate AWS services for cloud security telemetry processing.
- Document implementation decisions, testing results, and technical limitations.

## Development Milestones

| Milestone | Description | Status |
|---|---|---|
| 1 | Python & Security Alert Foundations | Completed |
| 2 | IOC Extraction & Validation | Completed |
| 3 | Threat Intelligence Enrichment | Planned |
| 4 | Automated Triage & Risk Scoring | Planned |
| 5 | AWS Cloud Integration | Planned |
| 6 | Testing, Documentation & Final Demonstration | Planned |

## Current Project Structure

```text
security-triage-pipeline/
├── main.py
├── ioc_validator.py
├── alert.json
├── tests/
│   └── TEST_RESULTS.md
├── README.md
└── .gitignore
```

### File Descriptions

| File | Purpose |
|---|---|
| `main.py` | Loads JSON alerts, extracts incident information, validates and classifies IP addresses, and reports severity |
| `ioc_validator.py` | Contains reusable IPv4 validation and classification functions |
| `alert.json` | Provides simulated security alert data |
| `tests/TEST_RESULTS.md` | Documents test cases, expected results, observed results, and limitations |
| `.gitignore` | Defines files Git should exclude from version control |

## Current Capabilities

### 1. JSON Security Alert Processing

The application reads simulated security alerts from `alert.json` and extracts relevant incident metadata.

Supported fields include:

- Incident ID
- Reported severity
- Source IPv4 address
- Destination IPv4 address

### 2. IPv4 Address Validation

The application uses Python's built-in `ipaddress` module to validate IPv4 address syntax.

The validator distinguishes valid IPv4 addresses from malformed or missing values.

**Important:** A valid IPv4 address is not necessarily malicious.

### 3. IPv4 Address Classification

The application classifies IP addresses according to their network characteristics.

Tested classifications include:

- `PRIVATE` — Private network addresses
- `GLOBAL` — Globally reachable addresses
- `LOOPBACK` — Local loopback addresses
- `DOCUMENTATION` — Reserved documentation ranges
- `INVALID` — Invalid IPv4 addresses

Additional special-use address ranges may require further classification logic.

### 4. Severity-Based Alert Reporting

The application processes the severity reported in the original alert.

Supported severity categories include:

- HIGH
- MEDIUM
- LOW
- UNKNOWN

These classifications are based on the input alert's reported severity, not independent threat intelligence analysis.

### 5. Error Handling

The application includes error handling for:

- Missing JSON input files
- Malformed JSON
- Unexpected JSON structures
- Missing IP address fields
- Invalid IPv4 addresses

The goal is to handle invalid input predictably without unexpected application failures.

## Running the Project

### Requirements

- Python 3
- A terminal or command-line interface
- No third-party Python packages required for the current implementation

### Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/axelhine/aws-security-triage-pipeline.git
   ```

2. Navigate to the project directory:

   ```bash
   cd aws-security-triage-pipeline
   ```

3. Run the security alert processor:

   ```bash
   python main.py
   ```

   On Windows, the Python launcher can also be used:

   ```powershell
   py main.py
   ```

4. Run the standalone IOC validation and classification checks:

   ```bash
   python ioc_validator.py
   ```

## Example Output

The following example uses simulated security alert data and documentation-only IP addresses.

```text
=== SECURITY ALERT REPORT ===
Incident ID: INC-001
Severity: HIGH
Source IP: 192.0.2.10
Destination IP: 198.51.100.25

=== IOC VALIDATION ===
Source IP: VALID
Destination IP: VALID

=== IP CLASSIFICATION ===
Source IP: 192.0.2.10
Classification: DOCUMENTATION

Destination IP: 198.51.100.25
Classification: DOCUMENTATION

=== INITIAL ALERT CLASSIFICATION ===
Priority: HIGH
Action: Security analyst review recommended.
```

The example demonstrates structural validation and classification. It does not indicate that either address is malicious.

## Milestone 1: Python & Security Alert Foundations

**Status:** Completed

### Objective

Develop a Python application capable of reading simulated cybersecurity alerts and generating structured security reports.

### Implementation

- Implemented JSON parsing using Python's `json` module.
- Extracted incident metadata from simulated alerts.
- Developed severity-based conditional reporting.
- Implemented handling for missing severity values.
- Added exception handling for malformed JSON and missing files.
- Established Git and GitHub version control.

### Outcome

Established a functional Python security alert processor that serves as the foundation for subsequent IOC analysis and AWS integration.

## Milestone 2: IOC Extraction & Validation

**Status:** Completed

### Objective

Develop and integrate reusable IPv4 validation and classification functionality into the existing alert-processing pipeline.

### Implementation

- Created `ioc_validator.py`.
- Implemented IPv4 syntax validation.
- Integrated the validator with `main.py`.
- Implemented IPv4 address classification.
- Added handling for missing IP fields.
- Conducted integration and regression testing.
- Documented results and limitations.

### Testing

Testing covered:

- Valid and invalid IPv4 addresses
- Private IPv4 addresses
- Globally reachable IPv4 addresses
- Loopback addresses
- Documentation-only addresses
- Missing IP fields
- Malformed JSON
- Missing JSON files
- Regression testing of existing alert-processing functionality

Test cases and observed results are recorded in `tests/TEST_RESULTS.md`.

### Outcome

The pipeline can now validate and classify IPv4 indicators extracted from simulated alerts while preserving its original alert-processing functionality.

## Planned AWS Architecture

The future serverless architecture is intended to use:

1. **Amazon VPC Flow Logs:** Collect network connection metadata from authorized AWS environments.
2. **AWS Lambda:** Execute alert-processing and enrichment logic.
3. **Amazon DynamoDB:** Store incident metadata and triage results.
4. **Amazon S3:** Retain security evidence and generated reports.
5. **AWS IAM:** Enforce least-privilege access to cloud resources.

VPC Flow Logs provide network flow metadata rather than packet contents. Additional detection logic will be required to transform telemetry into security alerts.

Additional AWS services may be introduced as needed.

## Security Considerations

- Current development uses simulated security alerts.
- Documentation-only IP addresses are used for testing.
- Future testing will be limited to authorized AWS resources.
- Credentials, API keys, and sensitive information will not be committed to GitHub.
- AWS permissions will follow least-privilege principles.
- Threat intelligence results will be treated as supporting evidence rather than definitive proof of maliciousness.
- AWS service costs and usage will be monitored during cloud integration.

## Current Limitations

- The pipeline currently runs locally.
- It processes simulated JSON alerts rather than live AWS telemetry.
- IPv4 is supported; IPv6 is not currently implemented.
- IP address classification does not establish maliciousness.
- External threat intelligence enrichment is not yet implemented.
- Automated risk scoring is not yet implemented.
- AWS deployment is not yet implemented.
- The application is not intended for production incident response.

## Next Development Phase

### Milestone 3: Threat Intelligence Enrichment

Planned activities include:

- Evaluating public threat intelligence sources.
- Integrating an external reputation API.
- Enriching eligible IP indicators with reputation data.
- Handling API errors and missing intelligence.
- Recording evidence and enrichment results.
- Documenting source limitations and analyst confidence.

## Learning Journal

Each milestone documents:

- Skills developed
- Implementation decisions
- Challenges encountered
- Troubleshooting steps
- Test cases and observed results
- Limitations and future improvements

## Disclaimer

This is an educational cybersecurity and cloud security automation project under active development. It is not intended for production incident response.