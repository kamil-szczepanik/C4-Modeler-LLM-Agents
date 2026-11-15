## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and compliance using GCP across `europe-west3` and `us-central1`.

## Key Elements
- Patients (EU & US)
- Licensed Clinicians
- Pharmacies
- External Pharmacies
- Regional Identity & Consent Providers
- AI Model Providers / Medical Devices
- Patient Web/Mobile App (Flutter / React Native)
- Clinician Portal (React SPA)
- API Gateway & Routing Service (Envoy Proxy / Istio)
- Core Telehealth Service (Node.js / Go)
- E-Prescription Interoperability Service (Spring Boot / Apache Camel)
- AI Symptom Checker Service (Python / FastAPI)
- Database Cluster (Cloud Spanner / PostgreSQL)

## Relationships
- Patients -> Cross-Border Telehealth Platform via HTTPS / WebSockets (adaptive codec)
- Licensed Clinicians -> Cross-Border Telehealth Platform via HTTPS
- Cross-Border Telehealth Platform -> External Pharmacies via TLS / Mutual TLS
- Cross-Border Telehealth Platform -> AI Model Providers / Medical Devices via HTTPS (REST/gRPC with payload masking)
- Cross-Border Telehealth Platform -> Regional Identity & Consent Providers via OAuth2 / OpenID Connect
- Patient Web/Mobile App -> API Gateway & Routing Service via HTTPS / WebSockets
- Clinician Portal -> API Gateway & Routing Service via HTTPS
- API Gateway & Routing Service -> Core Telehealth Service via gRPC / mTLS
- API Gateway & Routing Service -> E-Prescription Interoperability Service via gRPC / mTLS
- API Gateway & Routing Service -> AI Symptom Checker Service via gRPC / mTLS
- Core Telehealth Service -> Database Cluster via TCP / CMEK
- E-Prescription Interoperability Service -> External Pharmacies via TLS / Mutual TLS
- AI Symptom Checker Service -> AI Model Providers / Medical Devices via HTTPS (REST/gRPC with payload masking)
- Core Telehealth Service -> Regional Identity & Consent Providers via OAuth2 / OpenID Connect

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Cloud infrastructure ensuring isolated regional data residency.
- Cloud Spanner / PostgreSQL: Regional data stores with native change streams for compliance and low-latency transactions.
- Google Cloud KMS CMEK: Column-level and storage encryption with automated key rotation.
- Envoy Proxy / Istio: API gateway routing and service mesh mTLS.
- Node.js / Go & Python / FastAPI: Core microservices and AI integration.
- Spring Boot / Apache Camel: Interoperability and message translation.
- Flutter / React Native & React SPA: Cross-platform client applications.

## Rationale
The architecture strictly enforces GDPR and HIPAA data residency by isolating regional storage while maintaining interoperability and real-time telehealth capabilities. Cloud Spanner guarantees high availability, immutable audit logging for medical device compliance, and low-latency cross-border access.