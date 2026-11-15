## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and AI symptom checking for patients across the EU and US. The system enforces strict regional data residency while ensuring high availability for users with unstable internet connections.

## Key Elements
* Web & Mobile App (Flutter / TypeScript)
* API Gateway (Google Cloud API Gateway)
* Core Services Container (Spring Boot / Java)
* Video Media Server (LiveKit / WebRTC)
  * SFU Core (`Go` / `LiveKit Engine`)
  * Room & Session Manager (`Go`)
  * Adaptive Bitrate Controller (`Go`)
  * Token Verifier (`Go`)
* STUN/TURN Relay Servers (Global Anycast IPs)
* Google Secret Manager
* Cloud Operations & Prometheus Metrics Exporter

## Relationships
* Web & Mobile App -> SFU Core: Transmits media streams [WebRTC / DTLS-SRTP]
* Room & Session Manager -> Core Services Container: Validates session authorization [gRPC over mTLS]
* SFU Core -> Token Verifier: Validates incoming client JWTs locally [In-Memory]
* Adaptive Bitrate Controller -> SFU Core: Dynamically adjusts media codecs and enforces audio-only fallback [In-Memory Go API]
* Core Services Container -> Google Secret Manager: Retrieves cryptographic signing keys [Google Cloud API]

## Technology Stack
* LiveKit / WebRTC: Delivers low-bandwidth resilient video consultations under 300 kbit/s.
* Go: Implements high-performance, low-latency SFU and media control components.
* Google Secret Manager: Secures LiveKit API keys and signing secrets with automated rotation.
* Prometheus & Cloud Operations: Monitors real-time media quality, packet loss, and jitter.
* GCP Managed Instance Groups (MIGs): Handles CPU and network-bound horizontal auto-scaling.

## Rationale
This architecture guarantees strict regulatory compliance (GDPR and HIPAA) by isolating deployments in `europe-west3` and `us-central1` with regional firewalls. It ensures robust clinical continuity for rural patients via adaptive bitrate control and dedicated STUN/TURN relays.