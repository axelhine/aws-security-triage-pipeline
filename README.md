# Automated Security Alert & IOC Triage Pipeline

**Project Status:** In Development  
**Project Type:** Cybersecurity | Cloud Security | Security Automation  
**Technologies:** Python, JSON, Git, GitHub, AWS (Planned)

## Project Overview

This project focuses on developing an automated security alert processing and Indicator of Compromise (IOC) triage pipeline using Python and Amazon Web Services (AWS).

The objective is to build a system that can eventually receive real security alerts from an AWS cloud environment, extract suspicious indicators, evaluate potential security risks, and generate structured incident reports.

The project is being developed incrementally to build practical cybersecurity knowledge, programming skills, and cloud security experience.

## Project Objectives

- Understand how security monitoring and incident triage work.
- Learn Python programming through cybersecurity applications.
- Extract and analyze Indicators of Compromise (IOCs).
- Implement automated threat intelligence enrichment.
- Develop basic risk classification and reporting.
- Integrate AWS services to process real cloud security telemetry.
- Document technical decisions, challenges, and lessons learned.

## Development Milestones

| Milestone | Description | Status |
|---|---|---|
| 1 | Python & JSON Alert Processing | In Progress |
| 2 | IOC Extraction & Validation | Planned |
| 3 | Threat Intelligence Enrichment | Planned |
| 4 | Automated Triage & Risk Scoring | Planned |
| 5 | AWS Cloud Integration | Planned |
| 6 | Testing, Documentation & Final Demonstration | Planned |

## Milestone 1: Python & Security Alert Foundations

**Objective:** Build a basic Python program that reads simulated cybersecurity alerts from a JSON file.

### Skills Being Developed

- Python fundamentals
- JSON parsing
- Security alert structure
- Basic incident information extraction
- Command-line execution
- Git version control

### Expected Deliverables

- `main.py` — Python security alert processor
- `alert.json` — Simulated security alert
- `README.md` — Project documentation

### Current Progress

The initial project files have been created. Functional testing and further development are ongoing.

## Planned AWS Architecture

The future pipeline is intended to use:

1. **Amazon VPC Flow Logs:** Collect network connection metadata.
2. **AWS Lambda:** Process alerts automatically.
3. **Amazon DynamoDB:** Store incident metadata and triage results.
4. **Amazon S3:** Retain security evidence and reports.
5. **AWS IAM:** Control access to cloud resources.

Additional services may be introduced as the project develops.

## Security Considerations

The initial development environment uses simulated security alerts and documentation-only IP addresses.

Future testing will be limited to authorized AWS resources. Credentials, sensitive information, and private security data will not be published.

## Learning Journal

Each completed milestone will document:

- What I learned
- How I implemented the functionality
- Challenges encountered
- Troubleshooting steps
- Testing results
- Improvements for future development

## Disclaimer

This is an educational cybersecurity project under active development and is not intended for production incident response.