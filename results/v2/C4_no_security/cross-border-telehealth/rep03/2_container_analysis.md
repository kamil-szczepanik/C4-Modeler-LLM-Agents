## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring high availability and regulatory compliance.

## Key Elements
- Patients (EU/US) using Flutter Patient Mobile/Web App
- Licensed Clinicians using React/Node.js Clinician Portal
- GCP API Gateway (Cloud Endpoints/Envoy)
- Core Telehealth Service (Go/Spring Boot)
- AI Inference Wrapper (Python/FastAPI)
- Consent & Profile Management Service
- Pharmacy Integration Gateway (Camel/Spring Integration)
- GCP GKE Regional Clusters (`europe-west3`, `us-central1`)
- Cloud SQL PostgreSQL Databases
- GCP Cloud Pub/Sub

## Relationships
- Patients/Clinicians to API Gateway via HTTPS, WebRTC, and OAuth2/JWT
- API Gateway to Core Telehealth Service via gRPC
- Core Telehealth Service to AI Inference Wrapper via gRPC
- Core Telehealth Service to Pharmacy Integration Gateway via GCP Pub/Sub
- Services to Cloud SQL PostgreSQL via TLS

## Technology Stack
- Flutter: Client-side development supporting local caching for low-bandwidth degradation
- React/Node.js: Clinician portal web application framework
- Go / Spring Boot: Core microservice runtime for high-throughput telehealth orchestration
- Python / FastAPI: AI inference wrapper for symptom checker integration
- Apache Camel / Spring Integration: Translates data to HL7 FHIR (US) and EU national standards
- GCP GKE (`europe-west3`, `us-central1`): Isolated regional container orchestration
- Cloud SQL PostgreSQL: Region-locked primary data stores enforcing data residency
- GCP Cloud Pub/Sub: Asynchronous messaging buffer for prescription reliability

## Rationale
Region-isolated GKE clusters and databases guarantee strict GDPR and HIPAA data residency compliance. Asynchronous Pub/Sub messaging and local client caching ensure high availability and continuous operation during unstable rural internet connections.