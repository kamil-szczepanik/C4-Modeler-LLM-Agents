## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict data residency, regulatory compliance, and resilience for rural users.]

## Key Elements
* Patients (EU & US) & Licensed Clinicians
* Regional GKE Clusters (`europe-west3`, `us-central1`) via Google Cloud Platform
* WebRTC Media Server Containers (Jitsi/Mediasoup SFUs)
* TURN/STUN Regional Relays
* Prometheus & Grafana Monitoring

## Relationships
* Patients and Clinicians -> WebRTC Media Server Containers via WebRTC/mTLS and DTLS-SRTP
* WebRTC Media Server Containers -> TURN/STUN Relays via UDP/ICE
* SFU Containers -> Internal Microservices via Istio mTLS

## Technology Stack
* Jitsi/Mediasoup SFU: Handles video streams, simulcast, and dynamic bitrate scaling for unstable connections (<300 kbit/s).
* DTLS-SRTP & JWT: Secures media stream encryption and session authorization.
* Prometheus & Grafana: Provides real-time observability of WebRTC transport metrics.
* Istio Service Mesh: Enforces regional mTLS for inter-pod communication.

## Rationale
[This architecture enforces regional data residency to comply with GDPR and HIPAA mandates. It guarantees low-bandwidth video stability and secure, scalable media routing for rural telehealth users.]