## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict regional data residency, regulatory compliance, and high availability over unstable connections.]

## Key Elements
* Patients (EU & US) and Licensed Clinicians
* Pharmacies (EU & US), External AI Inference Provider, Identity Providers, Billing & Insurance Providers
* API Gateway (Cloud Endpoints / Envoy), Web & Mobile Apps (React / Flutter)
* Core Telehealth Service (Go / Spring Boot), Video Media Server (WebRTC / LiveKit SFU)
* AI Inference & Audit Service (Python / FastAPI), Prescription Integration Service (Node.js)
* Audit & Compliance Reporting Service (Python / BigQuery)
* Regional Databases (Google Cloud SQL for PostgreSQL in europe-west3 and us-central1)

## Relationships
* Patients / Clinicians -> API Gateway: HTTPS / WebSockets
* Web & Mobile Apps -> Core Telehealth Service: REST / gRPC via mTLS (TLS 1.3)
* Core Telehealth Service -> Regional Databases: PostgreSQL binary protocol over internal VPC peering (TLS 1.3)
* Video Media Server -> Patients: WebRTC (UDP/TCP) with Opus/VP8 codecs
* Core Telehealth Service -> External AI Inference Provider: HTTPS / REST (TLS 1.3)

## Technology Stack
* Google Cloud Platform (GCP): Targeted cloud infrastructure across europe-west3 and us-central1
* Cloud SQL for PostgreSQL: Relational database enforcing strict regional data residency and isolation
* React / Flutter: Cross-platform web and mobile application layer
* WebRTC / LiveKit SFU: Real-time video streaming with adaptive bitrate for unstable connections
* Go / Spring Boot / Python / FastAPI: Microservices implementation stack
* BigQuery: Large-scale compliance auditing and analytics sink

## Rationale
[This architecture enforces regional data segregation to guarantee GDPR and HIPAA compliance while maintaining localized data persistence. It utilizes adaptive streaming and resilient microservices to maintain availability for users with unstable internet connections.]