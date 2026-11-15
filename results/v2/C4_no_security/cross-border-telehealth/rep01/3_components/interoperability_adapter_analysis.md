## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and robust interoperability with national pharmacy networks.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- Interoperability Adapter container (GKE, Go) deployed regionally in `europe-west3` and `us-central1`
- US FHIR Translator Component and EU National Gateway Adapter Component
- Prescription Status & Retry Queue Component (Google Cloud Pub/Sub)
- Prescription Status Manager Component
- External EU National E-Prescription Gateways and US Pharmacy Networks
- Cloud SQL PostgreSQL, Cloud Monitoring, and Envoy sidecars

## Relationships
- Core Telehealth Service -> US FHIR Translator / EU Gateway Adapter: Sends prescription payloads [gRPC over internal VPC networks]
- US FHIR Translator / EU Gateway Adapter -> Prescription Status & Retry Queue: Publishes success/failure states [Google Cloud Pub/Sub]
- Prescription Status & Retry Queue -> Prescription Status Manager: Delivers transmission events [Internal Pub/Sub]
- Prescription Status Manager -> Core Telehealth Service: Emits standardized status updates [gRPC]
- Interoperability Adapter instances -> External Gateways and Networks: Integrates with external systems [mTLS]

## Technology Stack
- Google Kubernetes Engine (GKE): Container orchestration for regional adapter deployments, isolating EU and US workloads.
- Go: High-performance language chosen for translation and status management components.
- Google Cloud Pub/Sub: Asynchronous messaging for reliable retry queues and dead-letter routing.
- Envoy: Sidecars with circuit breakers protecting outbound connections from unstable third-party endpoints.
- OpenTelemetry & Cloud Monitoring: Distributed tracing and SLO dashboards tracking translation latency and error rates.

## Rationale
Regional GKE deployments in `europe-west3` and `us-central1` strictly enforce data residency laws by ensuring EU health data never crosses into US infrastructure. Asynchronous retry queues, status management, and circuit breakers guarantee high availability and error resilience despite unstable external pharmacy endpoints.