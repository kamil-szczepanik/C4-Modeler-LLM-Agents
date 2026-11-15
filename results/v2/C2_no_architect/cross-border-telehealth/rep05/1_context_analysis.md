## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, regulatory compliance, and high availability over low-bandwidth connections.

## Key Elements
- **Users**: Patients, Licensed Clinicians, Support Staff, Compliance/Legal Officers
- **External Systems**: Local Pharmacy Networks, National Health Authorities
- **Containers**: GCP Regional Deployments (`europe-west3`, `us-central1`), Zero-Trust API Gateways, WebRTC Signaling Servers, Edge CDN
- **Components**: AI Symptom Checker Service, Consent Management Service, E-Prescription Router, Immutable Audit Logger

## Relationships
- **Patients to WebRTC Signaling Servers**: Video consultations via WebRTC (SRTP/DTLS) with dynamic codec adaptation below 300 kbit/s
- **Clinicians to E-Prescription Router**: E-prescriptions sent via national standards (EU) and HL7 FHIR (US) over mTLS APIs
- **AI Symptom Checker to Immutable Audit Logger**: Inputs and model versions logged with cryptographic hashing via internal gRPC
- **Support Staff to Regional Deployments**: Just-In-Time (JIT) privileged access governed by break-glass controls

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` for EU, `us-central1` for US) for strict data residency and isolated infrastructure
- **Security & Encryption**: TLS 1.3, mTLS, Customer-Managed Encryption Keys (CMEK), OAuth 2.0 / OIDC with step-up MFA
- **Streaming & Connectivity**: WebRTC with adaptive bitrate codecs for low-bandwidth rural connections
- **Interoperability**: HL7 FHIR (US) and national e-prescription standards (EU) via zero-trust API gateways
- **Auditing & Compliance**: GCP Cloud Logging with tamper-proof storage for GDPR, HIPAA, and EU MDR traceability

## Rationale
Isolated regional GCP deployments guarantee that EU health data remains in `europe-west3` and US data in `us-central1`, satisfying GDPR and HIPAA requirements. Zero-trust security controls, JIT break-glass access, and bandwidth-resilient WebRTC streaming ensure secure, reliable cross-border care for vulnerable and rural patient populations.