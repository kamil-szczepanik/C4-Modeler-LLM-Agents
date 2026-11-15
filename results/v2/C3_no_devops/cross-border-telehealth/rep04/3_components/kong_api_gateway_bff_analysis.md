## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency, regulatory compliance, and resilience for unstable rural connections.

## Key Elements
- Patients (EU/US), Licensed Clinicians, Local Pharmacies, Compliance Officers
- Kong API Gateway/BFF (with Geo-Routing, JWT/OIDC Interceptor, Payload Compression, Header Enrichment)
- Spring Boot Core Telehealth Service
- FastAPI AI Symptom Checker
- Node.js E-Prescription Service
- Java Consent Management Service
- Node.js/Go Billing & Localization Container
- GCP Cloud SQL (PostgreSQL), GCP Cloud Storage, GCP Cloud Pub/Sub, Cloud KMS
- GCP Regions: `europe-west3`, `us-central1`

## Relationships
- Flutter/React Native Web and Mobile Apps -> Kong API Gateway/BFF: Sends API requests [HTTPS / TLS 1.3 / WebSockets with OAuth2/OIDC and DPoP]
- Kong API Gateway/BFF -> Spring Boot Core Telehealth Service: Routes core telehealth requests [gRPC / mTLS via Anthos Service Mesh]
- Kong API Gateway/BFF -> FastAPI AI Symptom Checker: Routes symptom check requests [gRPC / mTLS via Anthos Service Mesh]
- Kong API Gateway/BFF -> Node.js E-Prescription Service: Routes e-prescription requests [gRPC / mTLS via Anthos Service Mesh]
- Kong API Gateway/BFF -> Java Consent Management Service: Validates consent and tokens [gRPC / mTLS via Anthos Service Mesh]
- Kong API Gateway/BFF -> Node.js/Go Billing & Localization Container: Forwards localized requests [gRPC / mTLS via Anthos Service Mesh]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud infrastructure spanning `europe-west3` and `us-central1` for data residency.
- Kong API Gateway: Acts as BFF, enforcing geo-routing, rate limiting, and header injection via custom plugins.
- Spring Boot (Java) & FastAPI (Python): Core telehealth services and AI symptom checker container implementation.
- Node.js & Go: E-prescription, billing, and localization container runtimes.
- Anthos Service Mesh: Secures internal service-to-service communication with mTLS.
- PostgreSQL (GCP Cloud SQL): Relational data storage enforcing regional separation.

## Rationale
This architecture isolates data regionally between EU and US GCP regions to satisfy strict GDPR and HIPAA compliance mandates. Edge caching and payload optimization via Kong ensure reliable telehealth access for rural patients under unstable connections.