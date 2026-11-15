## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, HIPAA/GDPR compliance, and low-bandwidth resilience.

## Key Elements
* Patients and Clinicians (EU & US)
* Pharmacies and Platform Administrators
* Client Applications (Flutter / Web)
* API Gateway (Envoy / Google Cloud Endpoints)
* Core Telehealth Service (Go)
* AI Inference Service (Python / FastAPI)
* Interoperability Service (Java / Spring Boot)
* Containerized SFUs (mediasoup)
* Google Kubernetes Engine (GKE) (europe-west3, us-central1)
* PostgreSQL Databases with CMEK

## Relationships
* Client Apps to API Gateway via gRPC and HTTPS
* API Gateway to internal microservices via gRPC over Istio mTLS mesh
* Interoperability Service to National E-Prescription Gateways and US Pharmacy Systems via national formats and HL7 FHIR
* AI Inference Service to Cloud Storage via HTTPS for regional model artifacts and logs

## Technology Stack
* GCP (`europe-west3` and `us-central1`): Mandated for region-locked data residency and cloud infrastructure.
* GKE & Istio: Orchestration and service mesh enforcing mTLS and secure container communication.
* Go (Core Telehealth) & Python/FastAPI (AI Inference): High-performance microservices for backend logic and AI processing.
* HL7 FHIR & national e-prescription standards: Interoperability protocols for US and EU pharmacy integration.
* Google Cloud Operations Suite & Cloud Storage: Region-partitioned logging and secure audit storage.

## Rationale
The architecture strictly segregates workloads into regional GCP deployments to satisfy GDPR and HIPAA data residency constraints. Resilient edge caching, gRPC protocols, and mediasoup SFUs support low-bandwidth rural connections without compromising regulatory compliance or audit traceability.