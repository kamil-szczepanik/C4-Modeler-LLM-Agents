## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring high availability for rural users with unstable connections.

## Key Elements
- Patients (EU / US) & Licensed Clinicians
- Regional API Gateways (Kong / GCP API Gateway)
- Consultation Service split pods: Signaling Controller, Session Quality Monitor, Consultation Workflow Manager (Go on GKE)
- Media Relay / SFU Container (LiveKit / Mediasoup)
- Consent Management Service (Go / Node.js)
- Regional Cloud Spanner (GCP)
- Google Kubernetes Engine (GKE) Regional Clusters (`europe-west3`, `us-central1`)

## Relationships
- Regional API Gateways -> Signaling Controller: Forwards API requests and validates tokens [gRPC over mTLS]
- Signaling Controller -> Media Relay / SFU Container: Relays SDP offers/answers and ICE candidates [gRPC]
- Consultation Workflow Manager -> Consent Management Service: Validates patient data-sharing consent prior to session initialization [gRPC over mTLS]
- Session Quality Monitor -> Regional Cloud Spanner: Persists connection telemetry and audit logs [Go Cloud Spanner Client]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Enforces regional data residency constraints for EU and US health data.
- Google Kubernetes Engine (GKE): Hosts independently scalable consultation pods with Pod Disruption Budgets for high availability.
- Go: Powers the decoupled consultation microservices for high concurrency and low latency.
- LiveKit / Mediasoup: Manages WebRTC media relay and SFU capabilities with DTLS-SRTP encryption.
- SPIFFE/SPIRE: Secures intra-cluster communication with zero-trust mTLS.

## Rationale
This decoupled microservices architecture isolates erratic WebRTC traffic spikes from transactional workflows, preventing CPU starvation and ensuring reliable video consultations in degraded network modes. Furthermore, region-locked GKE clusters and Cloud Spanner instances strictly enforce GDPR and HIPAA data residency requirements.