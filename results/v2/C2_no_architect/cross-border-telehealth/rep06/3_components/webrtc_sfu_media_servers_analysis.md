## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It ensures regional data isolation, regulatory compliance, and high availability over unstable connections.

## Key Elements
- Patients and Licensed Clinicians (End Users)
- Regional GKE Clusters (`europe-west3`, `us-central1`)
- WebRTC SFU Media Servers Container
- API Gateway Container
- AI Symptom Checker Container
- Google Cloud Logging and Monitoring

## Relationships
- Patients/Clinicians -> API Gateway Container: Authenticates sessions [OAuth2/OIDC JWT, gRPC/HTTPS]
- API Gateway Container -> WebRTC SFU Media Servers: Issues short-lived TURN/STUN credentials [JWT]
- Patients/Clinicians -> WebRTC SFU Media Servers: Real-time video consultations [WebRTC, DTLS-SRTP, UDP]
- WebRTC SFU Media Servers -> Google Cloud Monitoring: Streams real-time telemetry [OpenTelemetry, WebRTC RTCStats]

## Technology Stack
- Google Kubernetes Engine (GKE): Regional container orchestration for data residency
- WebRTC & DTLS-SRTP: Real-time media streaming and encrypted transport
- GCP Premium Tier Network Paths: Optimizes UDP routing for rural users
- Customer-Managed Encryption Keys (CMEK): Secures transient local packet buffers at rest
- OpenTelemetry & Fluentbit: Telemetry export and PII stripping for logging compliance

## Rationale
This architecture isolates EU and US health data within regional Google Cloud regions (`europe-west3` and `us-central1`) to satisfy GDPR and HIPAA mandates. It utilizes WebRTC SFU media servers with adaptive bitrate streaming and audio-first fallback to ensure high availability for rural patients on unstable connections below 300 kbit/s.