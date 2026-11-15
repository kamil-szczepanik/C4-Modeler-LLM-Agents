## Overview
[The system is a cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. Its core purpose is delivering secure, compliant telemedicine services while enforcing strict regional data residency and auditability.]

## Key Elements
- Patients (EU/US), Licensed Clinicians, Compliance / Quality Assurance Auditors
- API Gateway & BFF (Go, Envoy Proxy)
- Video Consultation Container (WebRTC SFU, MediaSoup)
- E-Prescription Integration Container (Node.js, Express)
- AI Symptom Checker Container (Python, FastAPI)
- Cloud SQL (PostgreSQL)
- Cloud Storage (WORM enabled) (Google Cloud Storage)
- External Pharmacy Networks, National e-Prescription Gateways (EU), US Pharmacy Networks (HL7 FHIR)

## Relationships
- AI Symptom Checker Container -> Cloud Storage (WORM enabled): Asynchronous log ingestion and model retrieval [Cloud Storage APIs, HTTPS (REST)]
- API Gateway & BFF -> Containers: Request routing and authorization [HTTPS, gRPC]
- Video Consultation Container -> Third-Party Video Relay: Real-time media streaming [WebRTC, TURN]
- E-Prescription Integration Container -> National Gateways/Pharmacies: E-prescription delivery [HL7 FHIR, REST]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing regions `europe-west3` and `us-central1` for strict data residency.
- Go & Python (FastAPI): High-performance languages for API gateways and AI workloads.
- Google Cloud Storage (GCS): Object storage configured with Object Retention Lock (WORM) and CMEK for immutable compliance logging.
- Terraform: Infrastructure as Code for automated, drift-free deployment of security and storage policies.

## Rationale
[This architecture satisfies strict GDPR and HIPAA mandates by isolating regional data and securing AI diagnostic logs in immutable WORM storage. It maintains high availability and low latency for patients through asynchronous logging and regional multi-zone redundancy.]