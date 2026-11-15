## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict regional data residency, HIPAA/GDPR compliance, and low-bandwidth resilience.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Web/Mobile Client Applications (Flutter / React Native)
- Cloud Load Balancing / API Gateway (OAuth2/OIDC, TLS 1.3)
- Video Consultation Service (LiveKit WebRTC SFU on GKE)
- SFU Media Router (LiveKit Core)
- Session Signaling Controller (Go)
- Clinical Integration Hook (Go)
- Network Diagnostics Agent (Go)
- Post-Call Telemetry Handler (Go)
- Core Telehealth & E-Prescription (Spring Boot on GKE)
- Notification & Messaging (Node.js on Cloud Run)
- Google Cloud Pub/Sub & BigQuery
- Google Cloud KMS (CMEK) and Secret Manager

## Relationships
- Web/Mobile Client Applications -> Cloud Load Balancing / API Gateway: Routes client traffic [HTTPS / wss]
- Cloud Load Balancing / API Gateway -> Video Consultation Service: Routes real-time session traffic [gRPC over mTLS]
- SFU Media Router -> Web/Mobile Client Applications: Streams real-time media [WebRTC/UDP, SRTP/DTLS-SRTP]
- Session Signaling Controller -> Cloud Pub/Sub: Publishes emergency escalation alerts [Protobuf over gRPC]
- Post-Call Telemetry Handler -> Google Cloud Logging & BigQuery: Stores session ratings and QoS metrics [HTTPS]
- Video Consultation Service -> Security & Secret Management: Encrypts data and retrieves keys [Google Cloud KMS (CMEK), Secret Manager]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Enforces regional health data residency constraints
- GKE & Cloud Run: Hosts containerized microservices with Horizontal Pod Autoscaling
- LiveKit WebRTC SFU: Powers real-time video with dynamic codec step-down for low-bandwidth resilience
- Go & Spring Boot: Backend services for low latency and enterprise health interoperability (HL7 FHIR / national e-prescription standards)
- Confidential VMs (AMD SEV): Provides in-memory encryption for zero-trust media processing

## Rationale
The architecture combines regional GKE deployments with secure SFU media routing to comply strictly with EU/US data residency laws. Dynamic codec adjustments and resilient messaging protocols guarantee continuous, reliable care for rural patients with unstable connections.