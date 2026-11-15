## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data residency and compliance using isolated GCP cloud infrastructure.

## Key Elements
- **Clients**: Patient and Clinician applications (Web/Mobile)
- **API Gateway / BFF**: Node.js and GraphQL container handling client routing and requests (HTTPS/WebSockets)
- **Consultation Service**: Go container managing WebRTC signaling for video calls
- **Prescription & Interoperability Service**: Java/Spring Boot container handling HL7 FHIR (US) and EU e-prescription standards
- **AI Symptom Orchestrator**: Python and FastAPI container managing AI engine requests and immutable logging
- **Consent & Audit Service**: Java/Spring Boot container managing user permissions and compliance audits
- **Data & Cache Stores**: Google Cloud SQL (PostgreSQL), Google Memorystore (Redis), and Google Cloud Storage (GCS)
- **Security & Infrastructure**: Istio Service Mesh, GCP KMS, GCP Secret Manager, and ArgoCD

## Relationships
- **Clients to API Gateway / BFF**: HTTPS and WebSockets for client-facing traffic and real-time communication
- **API Gateway to Backend Containers**: gRPC over TLS via Istio Service Mesh (mTLS) for internal routing
- **Consultation Service to Memorystore (Redis)**: Internal TCP for WebRTC session states and caching
- **Backend Services to Cloud SQL & GCS**: Secure local drivers for regional data persistence and storage
- **AI Symptom Orchestrator to GCP Cloud Logging**: API calls for WORM audit log retention (EU MDR traceability)

## Technology Stack
- **Compute**: Google Kubernetes Engine (GKE) deployed in region-isolated clusters (`europe-west3` and `us-central1`) for GDPR and HIPAA compliance
- **Service Mesh**: Istio for zero-trust networking and mandatory mTLS enforcement
- **Databases & Caching**: Google Cloud SQL (PostgreSQL) with CMEK encryption, and Google Memorystore (Redis) with TLS
- **Storage**: Google Cloud Storage (GCS) with strict regional locking and WORM logging
- **CI/CD & GitOps**: ArgoCD with region-specific overlays for infrastructure consistency
- **Security**: GCP KMS for envelope encryption and GCP Secret Manager via Workload Identity

## Rationale
Region-isolated GKE clusters and storage ensure EU health data remains in `europe-west3` and US data in `us-central1`, satisfying GDPR and HIPAA constraints. Istio mTLS, CMEK encryption, and immutable WORM logging provide the security, consent tracking, and traceability required for medical devices and cross-border healthcare.