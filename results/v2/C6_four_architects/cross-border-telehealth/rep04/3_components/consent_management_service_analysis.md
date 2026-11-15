## Overview
The Cross-Border Telehealth Platform provides cross-border video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture ensures strict regional data residency and regulatory compliance under GDPR and HIPAA using GCP.

## Key Elements
- **Consent Management Service**: Container managing user consent and privacy settings.
- **Consent API Controller**: Component handling incoming gRPC requests.
- **Consent Policy Engine**: Component evaluating region-specific GDPR and HIPAA consent rules.
- **Consent Repository Adapter**: Component interacting regionally with databases.
- **Consent Event Publisher**: Component emitting asynchronous privacy events.
- **Google Cloud SQL for PostgreSQL**: Regional managed relational database.
- **Google Cloud Pub/Sub**: Asynchronous event messaging service.

## Relationships
- API Gateway -> Consent API Controller [gRPC over mTLS]
- Consent API Controller -> Consent Policy Engine [In-process function calls]
- Consent Policy Engine -> Consent Repository Adapter [In-process function calls]
- Consent Policy Engine -> Consent Event Publisher [In-process function calls]
- Consent Repository Adapter -> Google Cloud SQL [PostgreSQL Wire Protocol with TLS]
- Consent Event Publisher -> Google Cloud Pub/Sub [Cloud Pub/Sub API over TLS]

## Technology Stack
- **Go**: Chosen for high performance and strong typing required for strict compliance checks.
- **gRPC over mTLS**: Used for secure, type-safe inter-service communication.
- **Google Cloud SQL (PostgreSQL)**: Regional storage ensuring EU patient data remains in `europe-west3` and US data in `us-central1`.
- **Google Cloud Pub/Sub**: Enables immediate propagation of revocation events across services.

## Rationale
This component architecture enforces strict regional data residency by deploying isolated service instances and databases per region to meet GDPR and HIPAA mandates. In-process policy evaluation combined with asynchronous event publishing ensures real-time privacy enforcement without cross-region data leaks.