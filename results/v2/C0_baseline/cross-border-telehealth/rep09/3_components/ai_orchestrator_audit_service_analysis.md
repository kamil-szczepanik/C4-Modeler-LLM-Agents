## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. It ensures strict regional data residency, regulatory compliance, and traceability under GDPR, HIPAA, and EU MDR.

## Key Elements
* Patients & Licensed Clinicians
* Compliance Officers & Medical Quality Auditors
* Regional Ingress (Cloud Load Balancing & Envoy)
* Web/Mobile Frontend (Flutter)
* Telehealth Service (Go / WebRTC)
* Prescription & Record Service (Java / Spring Boot)
* AI Orchestrator & Audit Service (Python / FastAPI)
* Consent & Identity Service (Keycloak / PostgreSQL)
* External AI Symptom Checker Engine, National E-Prescription Gateways (EU), and US Pharmacy Networks

## Relationships
* Patients / Clinicians -> Regional Ingress: HTTPS / WebRTC
* Web/Mobile Frontend -> Regional Ingress: REST / gRPC with mTLS
* AI Orchestrator -> AI Symptom Checker Engine: gRPC / HTTPS with timeout handling
* AI Orchestrator -> Telehealth Service: gRPC with mTLS and SPIFFE ID verification
* AI Orchestrator -> Regional WORM Storage: Encrypted audit writes via Cloud KMS

## Technology Stack
* Google Cloud Platform (GCP): Deployment in `europe-west3` and `us-central1` for strict regional data residency.
* Python / FastAPI: Core framework for the AI Orchestrator and audit services.
* Keycloak / PostgreSQL: Identity management and regional consent tracking with JWT-based RBAC.
* Redis / NATS: Encrypted local message broker for asynchronous audit ingestion.
* gRPC with mTLS: Secure internal service-to-service communication.
* GCP Cloud KMS & Secret Manager: Regional envelope encryption and dynamic secret injection.

## Rationale
Isolated regional GKE deployments on GCP guarantee that EU and US health data never cross borders without explicit consent. Asynchronous cryptographic logging and strict RBAC satisfy stringent EU MDR traceability and HIPAA/GDPR compliance mandates.