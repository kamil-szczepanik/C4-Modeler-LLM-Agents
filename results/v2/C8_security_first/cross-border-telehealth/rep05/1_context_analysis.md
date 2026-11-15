## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency while enabling compliant cross-border clinician access.

## Key Elements
- **Patients (EU & US)**: End users managing consent and participating in telehealth sessions.
- **Licensed Clinicians**: Healthcare providers delivering remote care and issuing e-prescriptions.
- **Compliance & Quality Assurance Officers**: Internal stakeholders auditing platform safety and regulatory adherence.
- **Cross-Border Telehealth Platform**: System-of-interest deployed across GCP regions `europe-west3` and `us-central1`.
- **AI Diagnostic Service**: Containerized/external service for patient triage and urgency recommendations.
- **EU National e-Prescription Gateways & US Pharmacy Networks**: External systems for localized prescription fulfillment.

## Relationships
- Patients & Clinicians to Platform: HTTPS (web UI/API) and WebRTC (video streaming, supporting <300 kbit/s degraded mode).
- Platform to AI Diagnostic Service: gRPC for low-latency triage requests with WORM audit logging.
- Platform to e-Prescription Gateways & Pharmacies: REST / HL7 FHIR secured via mTLS.
- Cross-Region Platform Access: Cryptographic, time-bound consent tokens enforced at regional boundaries.

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (GCP) in `europe-west3` and `us-central1` for region-locked data residency.
- **Encryption**: TLS 1.3 for data in transit; mTLS with HSM-backed X.509 certificates for external integrations; SRTP for video streams.
- **Data Protection & Storage**: Cloud KMS with regionally managed keys; Cloud Storage Object Lock (WORM storage) for AI audit logs.
- **Streaming & Routing**: Selective Forwarding Units (SFUs) and Global Load Balancing with hard geo-fencing overrides.

## Rationale
This multi-region active-active isolated architecture guarantees strict GDPR and HIPAA compliance by ensuring EU and US health data never leaves its source region without explicit cryptographic consent. Concurrently, it delivers high availability and low-bandwidth resilience for rural users while maintaining traceability required for EU MDR compliance.