# Threat Intelligence API Research

**Project:** AWS Security Triage Pipeline  
**Milestone:** 3 — Threat Intelligence Enrichment  
**GitHub Issue:** #6

## Research Objective

Evaluate AlienVault OTX and Shodan as complementary sources for enriching public IPv4 indicators extracted from security alerts.

The objective is to distinguish threat intelligence from internet exposure intelligence and determine how both can contribute to automated security triage.

## AlienVault OTX

**Primary purpose:** Threat intelligence enrichment.

Provides information about indicators associated with reported threats, including related threat intelligence Pulses and supporting context.
### AlienVault OTX — Initial Research

**Provider:** AlienVault Open Threat Exchange (OTX)

**Intelligence category:** Community-driven threat intelligence.

**Purpose:** Enrich validated public IPv4 indicators with reported threat intelligence and supporting context.

**Relevant API endpoint:**

`GET /api/v1/indicators/IPv4/{ip_address}/general`

**Potentially useful response fields:**

- `indicator`: The investigated IPv4 address.
- `pulse_info.count`: Number of associated intelligence Pulses.
- `pulse_info.pulses`: Information about associated Pulses, when available.
- `reputation`: Reputation-related information, subject to documented interpretation.

**Analytical limitations:**

- Historical reports may no longer reflect current activity.
- Public IP addresses may change ownership or assignment.
- Intelligence reports can contain false positives.
- A lack of reports does not prove an IP address is safe.
- The number of associated Pulses should not be interpreted as a definitive threat score.

**Proposed use in the pipeline:**

Retrieve threat intelligence for eligible public IPv4 addresses, preserve relevant evidence and source information, and provide context for subsequent analyst review.

**Reference:** https://github.com/AlienVault-OTX/OTX-Python-SDK

### API Authentication

AlienVault OTX supports API-key authentication.

Authenticated requests include the `X-OTX-API-KEY` HTTP header.

**Credential management:**

- Store API credentials in a local `.env` file.
- Exclude `.env` from Git version control.
- Never hardcode credentials in Python source files.
- Never expose credentials in logs or documentation.
- Use environment-based configuration for future AWS deployment.

**Authentication status:** Account created; API connectivity testing pending.
### OTX API Response Analysis

**Test indicator:** `8.8.8.8`

**Observed API response:**

| Field | Returned value |
|---|---|
| Indicator | `8.8.8.8` |
| ASN | `AS15169 google llc` |
| Reputation | `0` |
| Associated Pulses | `0` |

**Analysis:**

The API successfully returned network attribution and threat intelligence metadata for the investigated public IPv4 address.

The ASN identifies the network associated with the IP address. The reputation field returned a numeric value of zero, but its meaning requires verification against OTX documentation.

The Pulse count indicates that no associated Pulses were returned during this lookup.

Neither result establishes that the IP address is benign.

**Conclusion:**

AlienVault OTX can provide structured intelligence that may support automated IOC triage. The pipeline should preserve the original evidence, distinguish missing data from negative findings, and avoid interpreting Pulse counts as definitive maliciousness scores.

## Shodan

**Primary purpose:** Internet exposure intelligence.

Provides information about publicly observed network services, open ports, technologies, and potential vulnerability associations.

## Proposed Integration

1. Extract and validate IPv4 indicators.
2. Determine whether each IP is eligible for public enrichment.
3. Query AlienVault OTX for threat intelligence.
4. Query Shodan for exposure information.
5. Normalize and correlate findings.
6. Produce an evidence-based security triage report.

## Research Remaining

- [ ] Identify relevant API endpoints.
- [ ] Document authentication requirements.
- [ ] Verify usage limits and account restrictions.
- [ ] Examine example JSON response structures.
- [ ] Design API error handling.
- [ ] Compare the value of both intelligence sources.
- [ ] Document official references.
### Shodan API — Initial Research

**Provider:** Shodan

**Intelligence category:** Internet exposure intelligence.

**Purpose:** Enrich eligible public IPv4 indicators with previously observed network service information.

**Relevant API endpoint:**

`GET /shodan/host/{ip}`

**API base URL:**

`https://api.shodan.io`

**Potentially useful response fields:**

- `ip_str`: Investigated IP address.
- `org`: Associated organization.
- `asn`: Autonomous system information.
- `ports`: Observed service ports.
- `data`: Service observation records, where available.

**Authentication:**

Shodan uses API-key authentication. Its documented REST API supports the `key` query parameter.

**Access limitations:**

- API keys are available with Shodan accounts.
- The main host-information endpoint requires Membership-level access.
- Eligible academic accounts can receive a free Membership upgrade.
- Certain capabilities, including API searches using the `vuln` filter, are restricted for academic users.

**Analytical limitations:**

- Observations may be outdated.
- An exposed service does not necessarily indicate a vulnerability.
- A potential vulnerability association does not prove exploitation.
- Missing results do not establish that a host has no exposed services.

**Integration status:** Research underway; API access not yet verified.

**References:**

- https://developer.shodan.io/api
- https://help.shodan.io/the-basics/academic-upgrade
- https://help.shodan.io/developer-fundamentals/looking-up-ip-info

### Shodan API Connectivity and Host Lookup Test

**Test indicator:** `8.8.8.8`

**API endpoints tested:**

- `GET /api-info`
- `GET /shodan/host/{ip}`

**Account information results:**

- API authentication: Successful
- Reported plan: `dev`
- Query credits: `100`
- Scan credits: `100`

**Host lookup results:**

| Field | Observed value |
|---|---|
| IP address | `8.8.8.8` |
| Organization | `Google LLC` |
| ASN | `AS15169` |
| Observed ports | `443`, `53` |

**Analysis:**

Shodan successfully returned host information for a public IPv4 indicator. The response identified the associated organization, autonomous system, and previously observed network service ports.

These observations provide exposure context but do not independently establish malicious behavior or confirmed vulnerabilities.

**Conclusion:**

Shodan can serve as a secondary enrichment source in the AWS Security Triage Pipeline, complementing AlienVault OTX's reported threat intelligence.

**Test status:** PASSED

### Initial API Connectivity Test

**Test objective:** Verify authenticated communication with the AlienVault OTX IPv4 general-information endpoint.

**Test indicator:** `8.8.8.8` (public DNS infrastructure)

**Endpoint:** `GET /api/v1/indicators/IPv4/{ip_address}/general`

**Observed results:**
- API request: Successful
- JSON parsing: Successful
- Returned indicator: `8.8.8.8`
- Associated Pulses: `0`

**Interpretation:**

The test confirms that the Python application can authenticate with AlienVault OTX, retrieve an IPv4 intelligence response, and extract selected JSON fields.

The absence of associated Pulses does not establish that an indicator is benign.

**Test status:** PASSED