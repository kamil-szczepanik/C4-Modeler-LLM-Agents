## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and compliance using GCP deployments in `europe-west3` and `us-central1`.

## Key Elements
- **Patient** & **Clinician** (Persons): Users accessing the platform via Mobile/Web Apps.
- **Client Apps**: Flutter/React frontend using Cloud CDN.
- **API Gateway / BFF**: Envoy managing client sessions and regional routing.
- **Core Telehealth Service**: Spring Boot/Go backend handling video orchestration, e-prescriptions, and consent.
- **AI Symptom Checker Container**: Python/Vertex AI service for local inference and audit logging.
- **Regional Database**: Cloud SQL PostgreSQL with regional KMS encryption.
- **External Systems**: External Pharmacies, Identity Providers (Auth0/GCP IAM), Regional Regulatory Systems, and National Health/Insurance Systems.

## Relationships
- Patient/Clinician -> Client Apps via HTTPS and WebRTC (video).
- Client Apps -> API Gateway / BFF via HTTPS / gRPC / REST.
- API Gateway -> Core Telehealth Service via internal VPC gRPC.
- Core Telehealth Service -> AI Symptom Checker Container via local gRPC.
- Core Telehealth Service -> Regional Database via encrypted SQL over TLS.
- Core Telehealth Service -> External Pharmacies & National Health Systems via REST / HL7 FHIR over TLS 1.3.
- Core Telehealth Service (EU) <-> Core Telehealth Service (US) via Mutual TLS over VPC Network Peering with cryptographic audit tokens.

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` for EU, `us-central1` for US) to enforce regional data residency.
- **Frontend**: Flutter and React with Cloud CDN to support low-bandwidth connections.
- **API Gateway**: Envoy for secure routing and session management.
- **Backend**: Spring Boot and Go for core telehealth and consent microservices.
- **AI Engine**: Python running on GCP Vertex AI for localized, traceable medical inference.
- **Database**: Cloud SQL PostgreSQL encrypted with regional KMS keys.
- **Interoperability**: HL7 FHIR (US) and national e-prescription standards (EU) via TLS 1.3.

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by isolating regional health data via dedicated GCP regions and encrypted peering. Localizing AI inference via GCP Vertex AI satisfies EU MDR traceability constraints while maintaining performance for unstable rural internet connections.