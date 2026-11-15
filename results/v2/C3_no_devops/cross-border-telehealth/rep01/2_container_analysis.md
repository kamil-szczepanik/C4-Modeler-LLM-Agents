## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients, caregivers, and clinicians in the EU and US. The system enforces strict regional data residency and regulatory compliance on GCP.

## Key Elements
* Users: Patients, Caregivers, Licensed Clinicians, Regulatory / Compliance Auditors
* External Systems: Pharmacies (EU & US), External AI Inference Provider / LLM API, Identity Providers (IDPs), Billing & Insurance Providers
* Containers: API Gateway (Cloud Endpoints / Envoy), Web & Mobile Apps (React / Flutter), Core Telehealth Service (Go / Spring Boot), Video Media Server (WebRTC / LiveKit SFU), AI Inference & Audit Service (Python / FastAPI), Prescription Integration Service (Node.js), Audit & Compliance Reporting Service (Python / BigQuery)
* Data Persistence: Regional Databases (Cloud Spanner / Cloud SQL) in `europe-west3` and `us-central1`

## Relationships
* Web & Mobile Apps to API Gateway: HTTPS / REST and gRPC over TLS
* API Gateway to Core Telehealth Service: mTLS via Istio Service Mesh
* Core Telehealth Service to Regional Databases: Secure TCP / PostgreSQL via internal VPC connectors
* Prescription Integration Service to Pharmacies: Cloud Pub/Sub and national e-prescription standards / HL7 FHIR over HTTPS
* Video Media Server to Patients/Clinicians: WebRTC over UDP/TCP
* AI Inference & Audit Service to External AI Provider: HTTPS API

## Technology Stack
* Cloud Platform: Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for geographic isolation
* Networking & Security: Istio Service Mesh for mTLS, Cloud Endpoints/Envoy for API Gateway, Cloud KMS with CMEK for encryption
* Backend & Integration: Go, Spring Boot, Python (FastAPI), Node.js, and Cloud Pub/Sub for resilient messaging
* Frontend: React / Flutter with offline-first capabilities for low-bandwidth support
* Data & Analytics: Cloud Spanner / Cloud SQL for regional persistence; BigQuery for compliance reporting

## Rationale
The architecture guarantees GDPR and HIPAA compliance by isolating regional databases and processing within dedicated GCP regions. Furthermore, it ensures high availability and traceability through resilient WebRTC media streaming, asynchronous messaging, and immutable audit logging.