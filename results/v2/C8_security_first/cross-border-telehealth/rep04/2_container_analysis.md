## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It enforces strict regional data residency and compliance using isolated cloud infrastructure.

## Key Elements
* **Patients & Clinicians**: End-users accessing the platform via web and mobile frontends.
* **API Gateway**: Envoy and Google Cloud Load Balancing acting as the regional entry point.
* **Core Telehealth Service**: Node.js/Go container managing appointments, clinician jurisdictions, and patient consent profiles.
* **E-Prescription Integration Service**: Java/Spring Boot container handling HL7 FHIR and EU national standard translations.
* **AI Symptom Checker Service**: Python/FastAPI container managing inference and WORM audit logging.
* **Media Streaming Container**: Janus WebRTC SFU handling adaptive video transcoding and DTLS-SRTP encryption.
* **Infrastructure**: GKE clusters, Istio service mesh with SPIFFE/SPIRE, ArgoCD, and regional OpenTelemetry collectors.

## Relationships
* **Client to API Gateway**: HTTPS and WSS protocols for secure client-to-container communication.
* **Internal Microservices**: gRPC over mTLS secured via Istio service mesh and SPIFFE/SPIRE identities.
* **External Integrations**: E-Prescription services communicating with EU National E-Prescription Gateways and US Healthcare Networks.

## Technology Stack
* **Cloud Provider**: GCP (`europe-west3` and `us-central1`) for regional data residency isolation.
* **Orchestration**: GKE and Istio service mesh for workload identity and mTLS enforcement.
* **Backend & Gateways**: Node.js/Go (Core), Java/Spring Boot (E-Prescriptions), Python/FastAPI (AI), and Envoy (Gateway).
* **Media & Storage**: Janus WebRTC SFU with DTLS-SRTP for video streaming; Regional WORM storage for AI audit logs.
* **Operations**: ArgoCD for GitOps deployment segregation and OpenTelemetry for regional observability.

## Rationale
This architecture strictly separates EU and US data processing to comply with GDPR and HIPAA mandates while supporting secure cross-border access. Containerized microservices, regional isolation, and adaptive WebRTC streaming ensure high availability and regulatory compliance under unstable rural network conditions.