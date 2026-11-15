## Overview
- Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US.
- Operates under strict GDPR and HIPAA compliance with isolated regional deployments on GCP.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- WebRTC SFU (Mediasoup / coturn) containers running in regional GKE clusters (`europe-west3`, `us-central1`)
- API Gateway (Istio Service Mesh / Envoy) and Frontend Containers
- AI Symptom Checker Container (Python, TensorFlow) and Audit Sidecar
- Google Cloud WAF and WORM Cloud Storage (Google Cloud Storage)

## Relationships
- Patients and Clinicians connect to WebRTC SFU via DTLS-SRTP (media) and DTLS/ICE (signaling/control) over WebRTC protocols
- SFU validates short-lived JWTs issued by the API Gateway for session access
- Prometheus sidecars export real-time WebRTC telemetry to Grafana

## Technology Stack
- **WebRTC SFU:** Mediasoup and coturn for real-time media streaming and NAT traversal, ensuring high availability and degraded mode support
- **Infrastructure:** Google Kubernetes Engine (GKE) across `europe-west3` and `us-central1` for strict regional data residency
- **Security:** DTLS-SRTP and JWT-based authorization for strict transport encryption and authenticated state holding

## Rationale
- Regional GKE isolation and co-located STUN/TURN servers ensure health data remains within EU and US boundaries to satisfy GDPR and HIPAA mandates.
- Mediasoup features enable graceful degradation and ICE restarts for rural patients with unstable internet connections.