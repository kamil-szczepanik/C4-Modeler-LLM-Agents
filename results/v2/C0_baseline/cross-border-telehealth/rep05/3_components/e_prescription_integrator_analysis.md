## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency and regulatory compliance under GDPR and HIPAA.

## Key Elements
- **Patients & Clinicians**: End-users accessing telehealth services via Flutter/React Native mobile and web client apps.
- **API Gateway**: GCP Cloud Endpoints / Envoy managing ingress routing.
- **Core Telehealth Service**: Go / gRPC backend coordinating core platform logic.
- **E-Prescription Integrator**: Java / Spring Boot container handling regional prescription dispatch.
- **AI Symptom Checker Service**: Python / FastAPI on GCP Cloud Run.
- **Regional Data Storage & Audit Layer**: GCP Cloud SQL and BigQuery.
- **External Systems**: Regional Pharmacy Networks, Third-Party Video Infrastructure, Regional Identity Providers.

## Relationships
- **Web & Mobile Client Apps -> API Gateway**: Sends user requests [HTTPS, gRPC]
- **API Gateway -> Core Telehealth Service**: Routes traffic [gRPC]
- **Core Telehealth Service -> E-Prescription Integrator**: Invokes prescription dispatch [mTLS-secured gRPC]
- **E-Prescription Integrator -> Regional Pharmacy Networks**: Dispatches prescriptions [HL7 FHIR, national EU formats via mTLS]
- **E-Prescription Integrator -> Regional Data Storage & Audit Layer**: Persists immutable audit logs [VPC Service Controls]
- **E-Prescription Integrator -> GCP Pub/Sub DLQ**: Buffers failed transmission payloads [AES-256 encrypted]

## Technology Stack
- **Backend & Integrations**: Java / Spring Boot with Spring Integration for enterprise message routing.
- **Resilience & Fault Tolerance**: Resilience4j (circuit breakers, bulkheads, rate-limiting) for unstable pharmacy endpoints.
- **Security & Identity**: Spring Security with OAuth2/JWT for token validation; GCP Secret Manager for mTLS certificates.
- **Cloud Infrastructure**: Google Cloud Platform (GCP) across `europe-west3` and `us-central1` regions with Terraform region-locked deployments.
- **Messaging & Telemetry**: GCP Pub/Sub for Dead-Letter Queues; OpenTelemetry and Micrometer for distributed tracing.

## Rationale
This architecture guarantees strict regional isolation of health data to comply with GDPR and HIPAA mandates. Resilient integration patterns and localized deployments ensure high availability and transaction integrity across diverse international pharmacy networks.