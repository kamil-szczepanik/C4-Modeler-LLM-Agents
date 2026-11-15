## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. It ensures strict regional data isolation, compliance with GDPR, HIPAA, and EU MDR, and robust performance on unstable connections.

## Key Elements
* Patients (EU and US) and Licensed Clinicians
* API Gateway & Routing Layer (Google Cloud Load Balancing, Apigee)
* Core Telehealth Service (Go on GKE)
* Video Media Server (WebRTC SFU on GKE)
* AI Inference Wrapper (Python on Vertex AI)
* Integration Service (Go / Camel-K on GKE)
* Audit & Traceability Ledger (Cloud Pub/Sub, BigQuery)
* Datastores (Cloud SQL PostgreSQL per region)
* External Systems: Identity & Consent Provider, EU National E-Prescription Gateways, US Surescripts, AI Model Registry

## Relationships
* Patients and Clinicians interact with the API Gateway via HTTPS and WebRTC.
* API Gateway routes traffic regionally to GKE containers in `europe-west3` and `us-central1`.
* Video Media Server streams WebRTC video between participants, supporting adaptive bitrate.
* Integration Service communicates with EU National E-Prescription Gateways and US Surescripts using HL7 FHIR and national standards.
* AI Inference Wrapper logs inputs and model versions to Cloud Pub/Sub and BigQuery.
* Core Telehealth Service reads and writes to regional Cloud SQL PostgreSQL instances.

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Enforces regional data residency constraints.
* Google Kubernetes Engine (GKE): Hosts microservices for container orchestration.
* Go: Used for Core Telehealth and Integration services for high performance.
* Python: Powers the AI Inference Wrapper on Vertex AI.
* WebRTC SFU: Enables resilient video streaming below 300 kbit/s.
* Cloud SQL (PostgreSQL): Secures relational data with regional partitioning.
* Cloud Pub/Sub and BigQuery: Provides immutable logging for EU MDR traceability.

## Rationale
This architecture guarantees strict regional data isolation between the EU and US to satisfy GDPR and HIPAA mandates. It also ensures EU MDR traceability and resilient video consultations via WebRTC and localized GKE deployments.