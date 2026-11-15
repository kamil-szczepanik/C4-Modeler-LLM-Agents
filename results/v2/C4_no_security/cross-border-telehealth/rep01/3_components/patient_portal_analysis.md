## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. The architecture enforces strict regional data residency and privacy compliance using GCP regions `europe-west3` and `us-central1`.

## Key Elements
* Patients (EU and US): Primary end-users accessing telehealth services
* Patient Portal: React and Flutter Single Page Application (SPA) with offline capabilities
* API Gateway / Region Router: Cloud Endpoints and Envoy routing cross-region traffic
* Core Telehealth Service: GKE cluster running Node.js, Go, and Python
* AI Gateway & Interoperability Adapter: GKE-hosted microservices for triage and HL7 FHIR / EU e-prescription mapping
* Data Layer: Cloud SQL PostgreSQL, Firestore, and Cloud Storage

## Relationships
* Patients (EU and US) -> Patient Portal: Access consultations and health services [HTTPS and WSS]
* Patient Portal -> API Gateway / Region Router: Routes API requests and telemetry [HTTPS and WSS via GCP Cloud CDN]
* API Gateway / Region Router -> Core Telehealth Service: Forwards authenticated traffic to backend containers [gRPC / HTTPS]

## Technology Stack
* Frontend & Client Storage: React, Flutter, IndexedDB with AES-GCM 256 encryption via Web Crypto API for secure offline resilience
* Cloud Platform: Google Cloud Platform (GCP) across `europe-west3` (EU) and `us-central1` (US) for regional data residency
* Backend Microservices: Node.js, Go, Python on Google Kubernetes Engine (GKE)
* Media Streaming: LiveKit and Janus WebRTC SFU Media Server for low-bandwidth video consultations
* Observability: OpenTelemetry for real-user monitoring and distributed tracing

## Rationale
The architecture guarantees GDPR and HIPAA compliance by isolating regional data storage and offloading encrypted state management to client-side storage for unstable rural connections. This ensures high availability and traceability while meeting rigorous cross-border healthcare interoperability standards.