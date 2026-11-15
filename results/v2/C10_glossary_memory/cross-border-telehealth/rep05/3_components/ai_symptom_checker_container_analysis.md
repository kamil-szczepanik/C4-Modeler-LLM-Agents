## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, regulatory compliance (GDPR/HIPAA/EU MDR), and high availability on GCP.

## Key Elements
- Patients
- Licensed Clinicians
- Compliance Officers / Auditors
- Web Application Container (React / Next.js)
- API Gateway Container (Envoy / GCP API Gateway)
- Core Services Container (Go / Node.js microservices)
- AI Symptom Checker Container (Python / FastAPI + Vertex AI)
- Media Relay Container (Janus / WebRTC SFU)
- E-Prescription Integration Container (Java / Spring Boot)
- Databases (GCP Cloud SQL for PostgreSQL)

## Relationships
- Patients -> Web Application Container (HTTPS)
- Licensed Clinicians -> Web Application Container (HTTPS)
- Web Application Container -> API Gateway Container (HTTPS / REST & GraphQL)
- API Gateway Container -> AI Symptom Checker Container (gRPC over mTLS)
- API Gateway Container -> Core Services Container (gRPC over mTLS)
- Core Services Container -> E-Prescription Integration Container (gRPC over mTLS)
- E-Prescription Integration Container -> EU National E-Prescription Gateways (HTTPS / mTLS / HL7 FHIR)
- E-Prescription Integration Container -> US Pharmacy Networks (Surescripts) (HTTPS / mTLS / HL7 FHIR)
- AI Symptom Checker Container -> GCP Vertex AI (HTTPS / REST via GCP Private Service Connect)

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` regions for regional data residency.
- Python / FastAPI: Powers the AI Symptom Checker Container for high-performance asynchronous request handling.
- GCP Vertex AI: Managed AI platform accessed via Private Service Connect for secure symptom triage.
- GCP Cloud SQL for PostgreSQL: Relational database secured with customer-managed encryption keys (CMEK) via GCP Cloud KMS.
- gRPC over mTLS: Protocol for secure, low-latency internal microservice communication.

## Rationale
This architecture isolates EU and US health data into dedicated regional deployments to satisfy strict GDPR and HIPAA residency mandates. Furthermore, decoupling the AI symptom checker with asynchronous audit logging ensures EU MDR traceability compliance without impacting consultation availability.