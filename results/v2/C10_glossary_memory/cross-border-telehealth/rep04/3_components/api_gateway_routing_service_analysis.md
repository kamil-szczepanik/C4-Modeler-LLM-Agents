## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and compliance using GCP across `europe-west3` and `us-central1`.

## Key Elements
- Patients (EU & US)
- Licensed Clinicians
- Patient Web/Mobile App (Flutter / React Native)
- Clinician Portal (React SPA)
- API Gateway & Routing Service (Envoy Proxy / Istio)
- Core Telehealth Service (Node.js / Go)
- E-Prescription Interoperability Service (Spring Boot / Apache Camel)
- AI Symptom Checker Service (Python / FastAPI)
- Database Cluster (Cloud Spanner / PostgreSQL)

## Relationships
- Patient Web/Mobile App -> API Gateway & Routing Service: Sends client requests [HTTPS / WebSockets]
- Clinician Portal -> API Gateway & Routing Service: Sends clinician requests [HTTPS]
- API Gateway & Routing Service -> Core Telehealth Service: Routes consultation and consent requests [gRPC / mTLS]
- API Gateway & Routing Service -> E-Prescription Interoperability Service: Routes e-prescription requests [gRPC / mTLS]
- API Gateway & Routing Service -> AI Symptom Checker Service: Routes symptom check requests [gRPC / mTLS]
- Core Telehealth Service -> Database Cluster: Persists regional health data [TCP / CMEK]

## Technology Stack
- Envoy Proxy / Istio: Manages regional API gateway routing, Istio service mesh mTLS, and Canary deployments.
- GCP (`europe-west3`, `us-central1`): Enforces regional physical data residency for GDPR and HIPAA.
- Redis: Provides regional rate-limiting and consent state management.
- Cloud Spanner / PostgreSQL: Secures regional data stores with Google Cloud KMS CMEK.

## Rationale
Regionalized gateway deployments and strict geo-routing guarantee that EU and US health data never cross borders without explicit consent. This decoupled, resilient architecture maintains availability for rural users while ensuring regulatory compliance under GDPR, HIPAA, and EU MDR.