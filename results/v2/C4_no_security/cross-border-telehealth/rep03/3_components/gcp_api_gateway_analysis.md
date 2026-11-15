## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture uses regional GCP infrastructure to enforce strict data residency and compliance.

## Key Elements
* Patients and Licensed Clinicians (Users)
* GCP API Gateway (Cloud Endpoints / Envoy)
* Core Telehealth Service (Go / Spring Boot)
* Regional Identity Providers
* GCP GKE Regional Clusters (`europe-west3`, `us-central1`)
* Regional Health Authorities and Auditors

## Relationships
* Patients / Clinicians -> GCP API Gateway: Accesses telehealth services [HTTPS, WebRTC, OAuth2/JWT]
* GCP API Gateway -> Core Telehealth Service: Routes API requests [gRPC]
* GCP API Gateway -> Regional Identity Providers: Authenticates users [OIDC, HTTPS]
* Regional Health Authorities -> GCP API Gateway: Accesses audit endpoints [mTLS, signed JWTs, HTTPS]

## Technology Stack
* GCP API Gateway / Envoy: Edge routing and local JWT validation to minimize latency
* gRPC over TLS: Inter-service communication for minimal serialization overhead on constrained networks
* OpenTelemetry / Cloud Trace: Distributed tracing across regional boundaries without data leakage
* Cloud Load Balancing: Anycast geo-routing to enforce physical entry-point segregation

## Rationale
Regional gateway deployments in `europe-west3` and `us-central1` enforce strict data residency requirements for GDPR and HIPAA compliance. Envoy-based traffic prioritization preserves availability for low-bandwidth users during active consultations.