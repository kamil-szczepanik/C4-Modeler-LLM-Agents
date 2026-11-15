## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system enforces strict regional data residency and compliance using isolated GCP deployments.

## Key Elements
* **Patients (EU/US):** End-users accessing services via Patient Web/Mobile App (Flutter/WASM).
* **Clinicians & Pharmacists (EU/US):** Healthcare providers using the Clinician Portal (React/TypeScript).
* **API Gateway:** GCP Cloud Endpoints / API Gateway routing regional traffic and validating OAuth2/JWT tokens.
* **Core Telehealth Service:** Go / gRPC & REST service managing consultations and *Third-Party Video Infrastructure*.
* **Consent & Identity Container:** Independent regional IAM instances enforcing data residency (R-05) and granular consents (R-04).
* **AI Symptom Service:** Python / FastAPI service interfacing with *AI LLM Provider*, logging versioned inputs/outputs to regional Cloud Storage.
* **E-Prescription Integrator:** Java / Spring Boot service translating data to HL7 FHIR (US) and national standards (EU).
* **Regional Storage & Messaging:** GCP Cloud SQL (PostgreSQL) and Pub/Sub isolated per region (`europe-west3`, `us-central1`).

## Relationships
* **Patient App to API Gateway:** HTTPS / WebSockets, falling back to audio/text streams below 300 kbit/s.
* **Internal Containers:** gRPC over internal VPC networks.
* **Core Telehealth to E-Prescription Integrator:** Asynchronous messaging via GCP Pub/Sub using regional topics.
* **AI Symptom Service to LLM Provider / Storage:** HTTPS for external LLM calls; direct writes to region-locked Cloud Storage for audit logs.

## Technology Stack
* **Cloud Infrastructure:** Google Cloud Platform (GCP) in `europe-west3` and `us-central1` for region-locked data residency.
* **Orchestration:** GKE Autopilot for dynamic, scalable container management.
* **Backend Services:** Go (Core Telehealth), Python/FastAPI (AI Symptom Service), Java/Spring Boot (E-Prescription Integrator).
* **Data & Messaging:** Cloud SQL for PostgreSQL (relational storage) and Pub/Sub (regional event streaming).
* **CI/CD:** ArgoCD GitOps pipelines for independent regional deployments.

## Rationale
This architecture guarantees strict regional data residency compliance for GDPR and HIPAA by completely isolating data storage, messaging, and identity instances per region. Furthermore, it ensures high availability and accountability for rural and regulated medical workloads through low-bandwidth client fallbacks and immutable AI audit logging.