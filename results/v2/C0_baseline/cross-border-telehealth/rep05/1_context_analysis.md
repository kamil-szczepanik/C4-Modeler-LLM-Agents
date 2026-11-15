## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It bridges fragmented regional healthcare markets into a unified service while strictly enforcing local health regulations and data residency.

## Key Elements
- **Patients (EU/US):** External actors accessing video consultations, e-prescriptions, and the AI symptom checker.
- **Licensed Clinicians:** External actors conducting consultations and issuing treatments.
- **Pharmacies & Compliance Officers:** External actors handling fulfillment and regulatory audits.
- **Cross-Border Telehealth Platform:** Core system split into isolated `europe-west3` (EU) and `us-central1` (US) regional boundaries.
- **External Systems:** Regional Pharmacy Networks, Third-Party Video Infrastructure, and Regional Identity Providers.
- **Infrastructure Services:** Global Anycast DNS / HTTP(S) Load Balancer and regional WORM storage audit sinks.

## Relationships
- **Actors to Platform:** TLS 1.3 over HTTPS and WebRTC for video; short-lived JWTs enforced at the edge.
- **Platform to Pharmacies:** mTLS with national EU e-prescription standards and US HL7 FHIR over HTTPS.
- **Inter-Regional Traffic:** Encrypted gRPC over VPC Network Peering, permitted only with explicit cryptographic patient consent.
- **Edge Routing:** Global Anycast DNS with geo-routing policies pinning users to their home region.

## Technology Stack
- **Cloud Provider:** Google Cloud Platform (GCP) utilizing `europe-west3` and `us-central1` for strict regional isolation.
- **Security & Encryption:** Cloud KMS with Customer-Managed Encryption Keys (CMEK) for data sovereignty; WORM storage for tamper-proof AI audit logs.
- **Authentication:** OAuth 2.0 / OIDC via regional Identity Providers with step-up MFA.
- **Protocols:** TLS 1.3, HTTPS, WebRTC, mTLS, and gRPC.

## Rationale
Isolating regional deployments on GCP with strict geo-routing and CMEK guarantees compliance with GDPR and HIPAA data residency constraints. Decoupling video via third-party infrastructure ensures availability and degraded-mode resilience for rural patients with unstable internet connections.