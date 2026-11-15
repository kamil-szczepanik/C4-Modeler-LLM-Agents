## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It utilizes GCP (`europe-west3`, `us-central1`) with strict data residency, encryption, and compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Anti-Corruption Layer (ACL) Container
- Inference Service (Python, gRPC)
- Regional Databases (GCP Managed Database)
- Cryptographic Vault (Cloud KMS / HSM)
- EU/US Pharmacies & National E-Prescription Gateways
- External Payment and Billing Gateways

## Relationships
- Patients/Clinicians -> API Gateway: Accesses services [HTTPS, WebSockets]
- ACL -> EU/US Pharmacies: Sends e-prescriptions and health data [REST, HL7 FHIR, National Standards]
- ACL -> Payment Gateways: Processes transactions [REST]
- Inference Service -> AI Model Registry: Loads and logs model versions [gRPC]

## Technology Stack
- Hexagonal Architecture (Ports and Adapters): Isolates core logic from external volatility.
- Pluggable Regional Modules: Manages diverging EU (National Standards) and US (HL7 FHIR) formats.
- Circuit Breaker & Idempotency Keys: Prevents cascading failures and duplicate pharmacy submissions over unstable links.
- Distributed Tracing & Correlation IDs: Ensures end-to-end observability across regional boundaries.
- Contract Testing (Pact): Catches breaking schema changes in external APIs proactively.

## Rationale
This architecture ensures strict data localization and regulatory compliance (GDPR/HIPAA) while maintaining high availability and resilience for users with unstable internet connections. Pluggable adapters and rigorous fault-tolerance patterns protect clinical workflows from third-party API instability.