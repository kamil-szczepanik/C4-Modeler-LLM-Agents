## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict regional data residency, regulatory compliance, and resilience for unstable internet connections.

## Key Elements
- Patients
- Licensed Clinicians
- Pharmacies
- Regional Identity & Consent Providers
- AI Model Providers / Medical Devices
- Patient Web/Mobile App (Flutter / React Native)
- Clinician Portal (React SPA)
- API Gateway & Routing Service (Envoy Proxy / Istio)
- Core Telehealth Service (Go)
- E-Prescription Interoperability Service (Spring Boot / Apache Camel)
- AI Symptom Checker Service (Python / FastAPI)
- Database Cluster (Cloud Spanner / PostgreSQL)

## Relationships
- Patients -> Patient Web/Mobile App (HTTPS / WebSockets (adaptive codec))
- Patient Web/Mobile App -> API Gateway & Routing Service (HTTPS / WebSockets)
- Clinician Portal -> API Gateway & Routing Service (HTTPS)
- API Gateway & Routing Service -> Core Telehealth Service (gRPC / mTLS)
- API Gateway & Routing Service -> E-Prescription Interoperability Service (gRPC / mTLS)
- API Gateway & Routing Service -> AI Symptom Checker Service (gRPC / mTLS)
- Core Telehealth Service -> Database Cluster (TCP / CMEK)
- E-Prescription Interoperability Service -> External Pharmacies (TLS / Mutual TLS)
- AI Symptom Checker Service -> AI Model Providers / Medical Devices (HTTPS (REST/gRPC with payload masking))
- Core Telehealth Service -> Regional Identity & Consent Providers (OAuth2 / OpenID Connect)

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` regions for strict data residency.
- Google Kubernetes Engine (GKE): Regional container orchestration ensuring isolated workloads per geography.
- Istio Service Mesh & Envoy Proxy: Manages traffic routing, mTLS, and canary deployments.
- Go: Powers high-performance internal microservices within the Core Telehealth Service.
- Cloud Spanner / PostgreSQL: Regional data stores secured via Google Cloud KMS CMEK.

## Rationale
This architecture enforces GDPR and HIPAA compliance by isolating regional data processing and storage within specific GCP zones. It ensures high availability and low-bandwidth resilience for rural patients through adaptive WebSockets and localized session handling.