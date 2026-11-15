## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US while strictly enforcing regional data residency and healthcare compliance standards.]

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- Cloud Run / Envoy API Gateway
- Core Telehealth Backend (Node.js / NestJS)
- AI Symptom Service (Python / FastAPI)
- Video Media Server (LiveKit / WebRTC)
- Interoperability Worker (Go)
- Cloud SQL (PostgreSQL) and Google Cloud BigQuery
- Google Cloud Pub/Sub with DLQs
- EU National E-Prescription Gateways and US Pharmacy Systems

## Relationships
- Interoperability Worker -> Cloud Pub/Sub: Consumes regional e-prescription tasks [Cloud Pub/Sub API]
- Interoperability Worker -> EU National E-Prescription Gateways: Transmits EU e-prescriptions [REST/SOAP, mTLS, TLS 1.3]
- Interoperability Worker -> US Pharmacy Systems: Transmits US e-prescriptions [HL7 FHIR, NCPDP, TLS 1.3]
- Interoperability Worker -> Core Telehealth Backend: Pushes delivery status updates [gRPC]

## Technology Stack
- Go: Chosen for the Interoperability Worker to ensure high-performance concurrent processing and strict memory safety.
- Google Cloud Platform (europe-west3, us-central1): Selected to guarantee strict regional data residency (R-05).
- Google Cloud Pub/Sub: Used for asynchronous, reliable message delivery with regional topic isolation and Dead-Letter Queues.
- TLS 1.3 and mTLS: Enforced for all external and internal communications to secure PHI in transit.
- Google Secret Manager: Deployed for partitioned, secure secret and certificate management per region.

## Rationale
[This architecture guarantees regional compliance by isolating data processing within specific GCP regions (europe-west3 and us-central1) to satisfy GDPR and HIPAA requirements. Furthermore, it ensures robust interoperability and high availability through containerized workers, regional Pub/Sub topics, and secure protocol adapters tailored to EU and US healthcare standards.]