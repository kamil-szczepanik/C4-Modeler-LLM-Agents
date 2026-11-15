## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency and compliance using Google Cloud Platform.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Clinic Administrators and Support Staff
- Flutter / Web Client Applications
- API Gateway (Envoy / Google Cloud Endpoints)
- Core Telehealth Service (Go container in GKE) decomposed into:
  - Consultation & Scheduling Component
  - Consent & Audit Engine
  - Data Residency Proxy
  - Prescription & Interoperability Orchestrator
- AI Inference Service (Python / FastAPI)
- Interoperability Service (Java / Spring Boot)
- Containerized SFUs (mediasoup)
- Regional PostgreSQL Databases with CMEK and Field-Level Encryption
- Google Kubernetes Engine (GKE) in `europe-west3` and `us-central1` managed via ArgoCD

## Relationships
- Client Applications -> API Gateway: Routes requests [HTTPS / WSS]
- API Gateway -> Core Telehealth Service: Routes core business requests [gRPC over Istio mTLS mesh]
- Core Telehealth Service components -> Regional PostgreSQL Databases: Persists and retrieves encrypted data [CMEK and FLE encrypted connections]
- Prescription & Interoperability Orchestrator -> Interoperability Service: Sends prescription data [gRPC over Istio mTLS]
- Internal Go components: Communicate via in-process Go function calls using shared-nothing in-memory state

## Technology Stack
- Go: Chosen for high performance and low-latency consultation workflows in the core service
- Google Kubernetes Engine (GKE): Dual-region orchestration (`europe-west3` and `us-central1`) ensuring data residency
- PostgreSQL: Regional databases with CMEK and Field-Level Encryption for PHI/PII protection
- Istio: Service mesh providing mTLS, circuit breaking, and traffic management
- ArgoCD: Regional continuous deployment preventing configuration drift
- GCP Secret Manager: Secure runtime injection of database credentials and signing secrets

## Rationale
The architecture strictly separates regional data environments to satisfy GDPR and HIPAA data residency constraints. Go-based micro-components on GKE optimize concurrency and support graceful degradation for rural patients with unstable internet connections.