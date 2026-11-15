## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. It enforces strict regional data residency, HIPAA/GDPR compliance, and asynchronous pharmacy integration to handle unstable rural connections.

## Key Elements
* Patients, Licensed Clinicians, Compliance Officers
* Client Apps (Flutter / Web application)
* API Gateway (Google Cloud API Gateway / Envoy)
* Core Telehealth Service (Node.js / Go container)
* AI Symptom Checker Container (Python / FastAPI)
* Patient Consent Service (Node.js / Go container)
* Pharmacy Integration Gateway (Go / Apache Camel container) comprising Prescription Orchestrator, Adapter Engine, Status & Audit Publisher, and Regional State Store
* Video Media Server (LiveKit / WebRTC SFU)
* Data Storage (Google Cloud SQL PostgreSQL with FHIR extensions, Google Cloud Memorystore for Redis)
* External Systems (EU National E-Prescription Gateways, US Pharmacy Networks, GCP Pub/Sub, GCP Secret Manager)

## Relationships
* Client Apps -> API Gateway: Client requests [HTTPS / WSS]
* API Gateway -> Core Telehealth Service: Routes consultation requests [gRPC over mTLS]
* API Gateway -> Pharmacy Integration Gateway: Routes e-prescription requests [gRPC over mTLS]
* Prescription Orchestrator -> Adapter Engine: Internal routing [In-memory Go channels]
* Adapter Engine -> EU National E-Prescription Gateways / US Pharmacy Networks: Submits e-prescriptions [mTLS over HTTPS]
* Status & Audit Publisher -> GCP Pub/Sub: Event emission [gRPC]
* Prescription Orchestrator -> Regional State Store: Read/Write idempotency state [Redis Protocol over TLS via internal VPC]

## Technology Stack
* GCP (europe-west3, us-central1): Target cloud infrastructure enforcing regional data residency (R-05)
* Go & Node.js: Container runtimes for core microservices and API routing
* Python & FastAPI: AI symptom checker runtime for model execution and traceability (R-03, R-07)
* LiveKit / WebRTC SFU: Video streaming supporting degraded modes below 300 kbit/s (R-06)
* Apache Camel: Integration framework for protocol mapping and retry handling
* Google Cloud SQL (PostgreSQL with FHIR): Relational data storage supporting HL7 FHIR (R-08)
* Google Cloud Memorystore for Redis: Regional transient state store for idempotency with strict TTLs
* GCP Pub/Sub: Asynchronous messaging for event-driven status delivery acknowledgments
* GCP Secret Manager & Workload Identity: Secure management of mTLS certificates and third-party keys

## Rationale
This architecture segregates workloads across dual GCP regions with strict VPC controls and CMEK encryption to satisfy GDPR and HIPAA data residency constraints without cross-region leakage. Additionally, the asynchronous event-driven design and regional state caching guarantee zero-drop patient status transparency and reliable retries over unstable connections.