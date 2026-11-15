## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict data residency, regulatory compliance (GDPR/HIPAA), and adaptive video streaming for unstable rural connections.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Client Apps (Flutter / Web application)
- Video Media Server: Media Ingestion & Routing Component (LiveKit SFU Router), Adaptive Bitrate (ABR) Controller, Egress Recording Worker (Node.js/FFmpeg), and Session Telemetry Publisher
- TURN Infrastructure (Third-Party Video Relay)
- Core Telehealth Service
- Regional Cloud Storage (GCP Cloud Storage with Cloud KMS CMEK)

## Relationships
- Client Apps -> Media Ingestion & Routing Component: Establishes WebRTC media sessions [WebRTC (ICE/DTLS-SRTP)] using short-lived JWTs
- Media Ingestion & Routing Component -> ABR Controller: Triggers simulcast layer switching on bandwidth drops [Internal gRPC/Channels]
- Session Telemetry Publisher -> Core Telehealth Service: Forwards real-time session health stats [gRPC]
- Media Ingestion & Routing Component -> TURN Infrastructure: Relays media over unstable connections [WebRTC / TURN-TLS]
- Egress Recording Worker -> Regional Cloud Storage: Writes encrypted media chunks [HTTPS/TLS 1.3]

## Technology Stack
- LiveKit SFU (Go/Rust Core): Powers real-time WebRTC media routing and simulcast handling for low-bandwidth optimization.
- WebRTC with DTLS-SRTP & TURN-TLS: Secures media transit and enables fallback routing for unstable rural networks.
- Node.js/FFmpeg: Powers the Egress Recording Worker for secure media composition.
- GCP Cloud KMS: Provides region-isolated customer-managed encryption keys (CMEK) for data at rest.

## Rationale
This component architecture ensures real-time video availability in degraded network conditions below 300 kbit/s through adaptive bitrate control and simulcast. Furthermore, it strictly enforces regional data residency and encryption standards required for GDPR and HIPAA compliance.