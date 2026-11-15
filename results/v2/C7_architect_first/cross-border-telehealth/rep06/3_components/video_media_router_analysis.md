## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system ensures regional data residency and low-bandwidth resilience across GCP regions.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Core Telehealth Backend (Node.js, Express)
- Video Media Router / Mediasoup SFU (Signaling Handler, SFU Worker Manager, ABR Controller, Media Relayer/Transport, DTLS-SRTP Encryptor/Decryptor, Event Dispatcher)
- GCP Infrastructure (Compute Engine C2/C3 instances, Cloud Operations, Prometheus)

## Relationships
- Patients/Clinicians -> Signaling Handler: Manages signaling connections [WSS]
- Core Telehealth Backend -> Signaling Handler: Authenticates and sets up room parameters [WebSockets]
- Media Relayer/Transport -> DTLS-SRTP Encryptor/Decryptor: Secures media streams [SRTP over UDP]
- SFU Worker Manager -> ABR Controller: Monitors packet loss and adjusts streams [Internal IPC]
- ABR Controller -> Event Dispatcher: Triggers fallback notifications [Internal Event Bus]

## Technology Stack
- Mediasoup SFU: Open-source WebRTC media router for real-time video handling
- DTLS-SRTP: Secure Real-time Transport Protocol with ephemeral key negotiation for encrypted media
- GCP C2/C3 Compute Instances: Optimized compute instances with hardware AES support for cryptographic overhead
- Prometheus & GCP Cloud Operations: Real-time monitoring of packet loss, jitter, and RTT
- WebSockets (WSS) & UDP/ICE: Protocols for signaling and NAT traversal

## Rationale
This architecture uses a Mediasoup SFU with an Adaptive Bitrate Controller to maintain audio-first continuity in unstable rural conditions (<300 kbit/s). Strict regional deployment on GCP with DTLS-SRTP encryption ensures compliance with GDPR, HIPAA, and regional data residency mandates.