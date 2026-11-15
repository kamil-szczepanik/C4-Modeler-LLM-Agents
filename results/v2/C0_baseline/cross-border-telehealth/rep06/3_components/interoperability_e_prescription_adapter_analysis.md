## Overview
Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency while ensuring interoperability with US and EU pharmacy networks.

## Key Elements
- Patients (EU & US) & Licensed Clinicians
- External Pharmacists (EU/US), EU National E-Prescription Gateways, & US Pharmacy Networks
- API Gateway (Envoy / Kong) & Interoperability & E-Prescription Adapter (GKE)
- FHIR Translation Engine, EU Gateway Translator, Regional Routing Dispatcher, Outbox & Retry Dispatcher, Secure DLQ Handler, mTLS & Policy Enforcement Proxy
- Regional Data Storage (Cloud SQL, Cloud Spanner, Cloud KMS, Cloud Pub/Sub, Cloud Logging / Cloud Storage)

## Relationships
- API Gateway -> Interoperability & E-Prescription Adapter: Routes requests [gRPC / mTLS via Istio Mesh]
- Regional Routing Dispatcher -> Regional Data Storage: Validates and logs transaction audits [SQL / TLS]
- Outbox & Retry Dispatcher -> EU National E-Prescription Gateways & US Pharmacy Networks: Delivers payloads [HTTPS / mTLS]
- Interoperability & E-Prescription Adapter -> External Gateways: Authenticates and transmits encrypted medical data [REST / SOAP / HL7 FHIR over HTTPS/mTLS]

## Technology Stack
- Google Cloud Platform (GCP): Primary cloud provider (`europe-west3`, `us-central1`) ensuring data residency compliance.
- Google Kubernetes Engine (GKE): Container orchestration for microservices and regional routing nodes.
- Python / Go: Core languages for translation engines, dispatchers, and handlers.
- Cloud Pub/Sub & Cloud SQL/Spanner: Asynchronous outbox queuing and regional data storage.
- Cloud KMS & Secret Manager: CMEK data encryption and secret management.
- Envoy Sidecar: Enforces mutual TLS (mTLS) and validates OIDC clinician license claims.

## Rationale
The architecture guarantees GDPR and HIPAA compliance by isolating regional health data within `europe-west3` and `us-central1` via localized GKE egress nodes and CMEK encryption. Asynchronous outbox patterns, circuit breakers, and Dead-Letter Queues (DLQ) ensure high availability and zero prescription loss during unstable connections or external gateway outages.