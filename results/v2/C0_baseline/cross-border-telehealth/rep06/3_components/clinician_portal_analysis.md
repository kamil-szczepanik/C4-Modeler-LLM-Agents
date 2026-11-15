## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency, GDPR/HIPAA compliance, and robust interoperability.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Clinician Portal (React Single Page Application)
- API Gateway (Envoy / Kong)
- Core Telehealth Service (Python / Go on Google Kubernetes Engine)
- LiveKit / WebRTC Media Relays (TURN / STEF)
- Regional Data Storage (Cloud SQL, Cloud Spanner, Cloud KMS)

## Relationships
- Clinician Portal -> API Gateway: Manages clinician workflows and requests [HTTPS/WSS via OAuth2/OIDC, mTLS]
- Clinician Portal -> LiveKit/WebRTC Media Relays: Establishes video consultation streams [SRTP/DTLS via TURN/STEF]
- API Gateway -> Core Telehealth Service: Routes backend business logic and consent checks [gRPC / HTTPS]
- Core Telehealth Service -> Regional Data Storage: Persists encrypted health records [Postgres Protocol / Cloud KMS]

## Technology Stack
- Frontend: React SPA deployed via GCP Cloud CDN and Cloud Storage buckets for low-latency regional access.
- Backend Compute: Python / Go microservices running on Google Kubernetes Engine (GKE) across `europe-west3` and `us-central1`.
- Media Streaming: LiveKit WebRTC using SRTP/DTLS and TURN/STEF protocols to support degraded network connections.
- Security & Compliance: GCP Secret Manager, Cloud KMS, OAuth2/OIDC, and HttpOnly cookies for HIPAA and GDPR enforcement.

## Rationale
Google Cloud Platform's multi-region topology (`europe-west3` and `us-central1`) guarantees that EU and US health data remain isolated within their respective jurisdictions. Containerized microservices on GKE combined with LiveKit WebRTC ensure high availability and resilient video streaming for users in rural areas.