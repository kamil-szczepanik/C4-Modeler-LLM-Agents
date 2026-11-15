## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and interoperability standards.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Web App & Mobile App (Flutter / React)
- Regional GCP API Gateways (Managed Google Cloud API Gateway / ESPv2 in `europe-west3` and `us-central1`)
- Core Telehealth Backend (Go / Spring Boot)
- AI Symptom Checker Service (Python / FastAPI)
- Video Streaming Server (WebRTC / SFU Mediasoup)
- EU E-Prescriptions Adapter (Java / Spring Boot) & US Healthcare Interoperability Service (Node.js / FHIR SDK)
- GCP Cloud SQL, Cloud Storage, Cloud KMS, and Secret Manager

## Relationships
- Web App & Mobile App -> Regional GCP API Gateways: Sends regional client traffic [HTTPS, WebSockets]
- Regional GCP API Gateways -> Anthos Service Mesh: Enforces ingress traffic management [mTLS]
- GCP API Gateway -> EU E-Prescriptions Adapter / US Healthcare Interoperability Service [mTLS, gRPC]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for scalability and compliance tooling.
- Managed Google Cloud API Gateway (ESPv2): Handles regional routing, protocol translation, and schema validation.
- Anthos Service Mesh (Istio): Secures microservices communication with mTLS.
- Cloud Armor: Provides WAF protection and threat mitigation at regional edges.
- PostgreSQL & WORM storage: Ensures persistent, encrypted health data storage.

## Rationale
Physically isolating gateways and backends into regional instances (`europe-west3` and `us-central1`) guarantees strict adherence to EU and US data residency laws. The chosen cloud-native GCP stack leverages managed security, mesh networking, and robust protocols to maintain compliance, scalability, and performance under unstable network conditions.