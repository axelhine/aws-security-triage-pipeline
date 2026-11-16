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