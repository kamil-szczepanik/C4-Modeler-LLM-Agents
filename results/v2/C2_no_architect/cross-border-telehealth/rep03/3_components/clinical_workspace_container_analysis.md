## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients and clinicians across the EU and US. It ensures regional data residency and low-bandwidth resilience on GCP.

## Key Elements
* Licensed Clinicians and Medical Administrators (Users)
* Clinical Workspace Container (GKE container hosting web interface and LiveKit WebRTC SFU)
* Consent & Compliance Container (Microservice with WORM BigQuery)
* Google Cloud Pub/Sub (Regional event bus with dead-letter queues)
* Vertex AI (External AI inference system)
* Local Pharmacies (External systems supporting HL7 FHIR and national EU standards)

## Relationships
* Licensed Clinicians -> Clinical Workspace Container: Manages video consultations and e-prescriptions via HTTPS, WebRTC, and OAuth2/OIDC via Identity-Aware Proxy (IAP)
* Clinical Workspace Container -> Consent & Compliance Container: Enforces granular consent and immutable audit logging via mTLS inside GKE via Istio and OAuth2
* Clinical Workspace Container -> Vertex AI: Requests AI symptom-checker inferences via gRPC/REST over mTLS
* Clinical Workspace Container -> Google Cloud Pub/Sub: Publishes async e-prescription events with regional message encryption
* Clinical Workspace Container -> Local Pharmacies: Routes e-prescriptions using REST APIs with HL7 FHIR (US) and national e-prescription standards (EU)

## Technology Stack
* Google Kubernetes Engine (GKE): Deployed in `europe-west3` and `us-central1` for localized regional scaling
* LiveKit WebRTC SFU: Embedded with dedicated node pools, local SSDs, and UDP-optimized ingress for sub-300 kbit/s degraded-mode video
* Istio Service Mesh: Enforces strict mTLS and zero-trust container-to-container communication
* Google Cloud Pub/Sub: Manages async, decoupled event-driven e-prescription routing with CMEK encryption
* GCP Identity-Aware Proxy (IAP) with OAuth2/OIDC: Enforces granular RBAC/ABAC separating clinician and administrator access

## Rationale
This architecture guarantees strict regional data residency and compliance with GDPR and HIPAA through isolated GKE clusters, regional Pub/Sub queues, and CMEK encryption. Additionally, the decoupled event-driven design and LiveKit SFU optimization ensure high availability and resilient performance for users with unstable internet connections.