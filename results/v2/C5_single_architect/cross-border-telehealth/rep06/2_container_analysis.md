## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency while ensuring HIPAA and GDPR compliance.

## Key Elements
* **Global Load Balancer with Cloud Armor:** Routes traffic and enforces regional pinning.
* **API Gateway / BFF (Go, gRPC/REST):** Handles regional boundary checks and client routing.
* **Core Telehealth Service (Node.js/TypeScript):** Manages user profiles, appointments, and consent (R-04).
* **Video Consultation Service (Golang/WebRTC SFU via LiveKit):** Manages real-time video with low-bandwidth degradation.
* **AI Orchestrator (Python, FastAPI):** Integrates with external LLMs and handles traceability.
* **E-Prescription Integrator (Java/Spring Boot):** Translates data for national EU standards and US HL7 FHIR.
* **Data Storage:** Region-locked Cloud SQL (PostgreSQL), Cloud Storage, and Cloud Bigtable.

## Relationships
* **Global LB to API Gateways:** HTTPS routing with geo-routing policies.
* **API Gateways to Core/Video/AI/E-Prescription Services:** gRPC over mTLS via Istio service mesh.
* **AI Orchestrator to LLM API:** HTTPS/REST for symptom analysis.
* **E-Prescription Integrator to Pharmacies:** HL7 FHIR (US) and national standards (EU).
* **Cross-Region Services:** Google Cloud Pub/Sub with TLS and IAM payload encryption.

## Technology Stack
* **Cloud Provider:** GCP (`europe-west3` and `us-central1`) for isolated regional deployments.
* **Orchestration:** Google Kubernetes Engine (GKE) with Istio service mesh for zero-trust mTLS.
* **Backend Languages:** Go, Node.js/TypeScript, Python, and Java.
* **Real-Time Video:** LiveKit (WebRTC SFU) for handling unstable rural connections.
* **Databases:** Cloud SQL (PostgreSQL) and Cloud Bigtable for immutable audit logs.

## Rationale
Isolated regional GKE clusters with dedicated storage guarantee strict GDPR and HIPAA compliance by ensuring EU and US health data never commingle without explicit consent. Istio mTLS, regional API gateways, and specialized routing satisfy high availability, low-bandwidth resilience, and strict AI auditability.