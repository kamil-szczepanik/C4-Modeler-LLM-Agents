## Overview
The Video Media Server component of the Cross-Border Telehealth Platform provides low-bandwidth resilient video and audio consultations for patients and clinicians in the EU and US. It ensures secure, compliant, and uninterrupted communication across unstable rural network connections while enforcing strict regional data residency.

## Key Elements
- WebRTC Ingress/Egress Handler (LiveKit SDK / C++)
- Adaptive Bitrate (ABR) Controller
- Session & Auth Coordinator
- Media Recorder (GStreamer / GCP Cloud Storage)
- Distributed TURN Relays
- Redis Pub/Sub Event Bus

## Relationships
- API Gateway -> Session & Auth Coordinator: Room creation and participant management [gRPC]
- Patients/Clinicians -> WebRTC Ingress/Egress Handler: Video and audio media streams [WebRTC over UDP/TCP, DTLS/SRTP]
- Session & Auth Coordinator -> Media Recorder: Real-time control events for consent management [Redis Pub/Sub]
- Media Recorder -> GCP Cloud Storage: Encrypted session archives [HTTPS / Regional CMEK]

## Technology Stack
- LiveKit SFU / WebRTC: Real-time media streaming handling packet loss and jitter
- GStreamer: Secure local and archived session media recording
- Redis: In-memory event bus for real-time control messaging (consent updates)
- GCP Cloud Storage (`europe-west3`, `us-central1`): Region-locked storage enforcing data residency
- DTLS-SRTP: End-to-end transport encryption with master secret rotation

## Rationale
This architecture uses LiveKit SFU with dynamic ABR control to maintain stable consultations in rural areas below 300 kbit/s. Regional GCP deployment, regional CMEK encryption, and real-time consent event handling ensure strict GDPR and HIPAA compliance.