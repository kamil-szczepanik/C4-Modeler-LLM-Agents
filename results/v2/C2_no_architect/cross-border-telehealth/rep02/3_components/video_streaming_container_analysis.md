## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It enforces strict regional data residency while ensuring high availability for patients in rural areas.

## Key Elements
- Patients & Licensed Clinicians
- API Gateway Container (GCP GKE, Istio, OPA)
- Video Streaming Container (GCP GKE, WebRTC, Prometheus/Grafana)
- Consent & Identity Management Container (GCP GKE, Istio)
- Regional WORM Storage Buckets (GCP Cloud Storage)

## Relationships
- API Gateway Container -> Video Streaming Container: Routes consultation requests [Istio mTLS]
- Video Streaming Container -> Patients: Streams real-time video with adaptive bitrate [WebRTC over DTLS-SRTP]
- Video Streaming Container -> Licensed Clinicians: Streams real-time video with adaptive bitrate [WebRTC over DTLS-SRTP]
- Video Streaming Container -> Consent & Identity Management Container: Verifies active session consent [gRPC]

## Technology Stack
- GCP GKE: Regional container orchestration deployed in `europe-west3` and `us-central1` for data residency.
- WebRTC & DTLS-SRTP: Real-time media streaming with end-to-end encryption supporting unstable connections (<300 kbit/s).
- Prometheus & Grafana: Telemetry tracking for Quality of Experience (QoE) metrics and clinical reliability.
- Istio Service Mesh: Zero-trust network security enforcing mTLS and JWT validation.

## Rationale
Regional GKE isolation and zero-trust policies satisfy strict GDPR and HIPAA compliance mandates. Adaptive WebRTC streaming guarantees clinical availability for low-bandwidth rural users.