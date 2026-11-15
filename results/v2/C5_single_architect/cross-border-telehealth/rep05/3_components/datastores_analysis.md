## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures regional compliance, data residency, and traceability using Google Cloud Platform.

## Key Elements
* Patients (EU and US) and Licensed Clinicians
* Google Cloud Load Balancing & Apigee (API Gateway & Routing Layer)
* Core Telehealth Service (Go on GKE)
* Video Media Server (WebRTC SFU on GKE)
* AI Inference Wrapper (Python on Vertex AI)
* Integration Service (Go / Camel-K on GKE)
* Primary Operational DB (Cloud SQL PostgreSQL per region)
* AI Audit Store (BigQuery per region)
* Consent & Encryption Key Store (Cloud KMS / Secret Manager per region)
* External Systems: EU National E-Prescription Gateways, US Surescripts, AI Model Registry

## Relationships
* `Core Telehealth Service` -> `Primary Operational DB`: Reads and writes regional data [PostgreSQL Protocol]
* `Core Telehealth Service` -> `Consent & Encryption Key Store`: Fetches regional KMS keys for field-level encryption [Cloud KMS API]
* `Primary Operational DB` -> `Consent & Encryption Key Store`: Validates patient revocation flags [Internal gRPC]
* `AI Inference Wrapper` -> `AI Audit Store`: Appends prediction logs [BigQuery API / gRPC]
* `Integration Service` -> `Primary Operational DB`: Reads/writes regional FHIR/e-prescription state [PostgreSQL Protocol]

## Technology Stack
* Google Cloud Platform (`europe-west3`, `us-central1`): Enforces geographical data residency constraints (R-05).
* Cloud SQL PostgreSQL: Manages relational operational data, user profiles, and encrypted metadata.
* BigQuery: Maintains tamper-evident, append-only logs for AI traceability and audits (R-07).
* Cloud KMS / Secret Manager: Handles regional envelope encryption and consent mappings.
* WebRTC SFU: Powers video consultations under unstable bandwidth conditions (R-06).

## Rationale
This architecture uses strictly isolated regional deployments on GCP to satisfy GDPR, HIPAA, and data residency requirements. Decoupled audit and encryption stores ensure strict traceability for AI medical device outputs while maintaining high availability.