## Overview
This system is a cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture ensures strict regional data residency, regulatory compliance (GDPR, HIPAA, EU MDR), and high availability over unstable connections.

## Key Elements
- Patients and Licensed Clinicians (Users)
- National e-Prescription Gateways and US Pharmacies/EHRs, Regional Identity Providers (External Systems)
- Web App & Mobile App (Flutter / React)
- GCP API Gateway (GCP API Gateway)
- Core Telehealth Backend (Go / Spring Boot)
- AI Symptom Checker Service (Python / FastAPI)
- Video Streaming Server (WebRTC / SFU - Mediasoup)
- EU E-Prescriptions Adapter (Java / Spring Boot)
- US Healthcare Interoperability Service (Node.js / FHIR SDK)
  - FHIR API Router (Node.js / Express)
  - US Transformation Engine (Node.js / Smart-on-FHIR SDK)
  - HIPAA Audit & Compliance Logger (Node.js)
  - US E-Prescription Dispatcher (Node.js / Axios)
- GCP Cloud SQL & Cloud Storage (PostgreSQL, WORM buckets, Cloud KMS, GCP Secret Manager)

## Relationships
- Core Telehealth Backend -> US Healthcare Interoperability Service: Communicates for US health interoperability [mTLS]
- FHIR API Router -> US Transformation Engine: Internal method calls [TypeScript]
- US Transformation Engine -> HIPAA Audit Logger: Intercepts payload for compliance logging [Async/Await]
- US Transformation Engine -> US E-Prescription Dispatcher: Passes validated FHIR e-prescription bundles [Internal Event/Queue]
- US E-Prescription Dispatcher -> US Pharmacies/EHRs: Dispatches HL7 FHIR messages [Egress-filtered HTTPS, mTLS]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Target cloud provider for regional data isolation and compliance.
- Google Kubernetes Engine (GKE): Container orchestration with horizontal pod autoscaling.
- Go, Spring Boot, Node.js, Python, FastAPI: Backend container runtime technologies.
- WebRTC / SFU (Mediasoup): Low-latency video streaming supporting degraded bandwidth modes.
- HL7 FHIR over REST, SMART on FHIR: US healthcare interoperability standards.
- GCP Pub/Sub: Dead Letter Queue for reliable e-prescription dispatches.
- GCP Cloud KMS & WORM Buckets: Encryption and immutable audit storage for HIPAA compliance.

## Rationale
This architecture uses regional GCP deployments to strictly separate EU and US health data, satisfying GDPR and HIPAA constraints. Containerized microservices and decoupled egress dispatchers ensure robust performance, resilience over unstable rural connections, and auditable medical interoperability.