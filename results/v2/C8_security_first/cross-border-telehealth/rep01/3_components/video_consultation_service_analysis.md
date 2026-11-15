## Overview
Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system ensures regional data residency and low-bandwidth resilience for rural users.

## Key Elements
* Patients and Clinicians
* API Gateway / Ingress (Envoy / GCP HTTPS Load Balancer)
* Video Consultation Service (Mediasoup WebRTC SFU containers on GCP GKE)
* Signaling & Room Manager Component (Node.js)
* SFU Media Worker Component (Mediasoup / C++ core)
* Bandwidth Adaptability Controller Component (Go)
* TURN/STUN Relay Infrastructure (Coturn)
* AI Symptom Checker Container (Python / FastAPI, PyTorch)
* E-Prescription Integration Container (Node.js, FHIR protocol adapters)
* Data Tier (Cloud SQL PostgreSQL, Memorystore with CMEK)
* Messaging & Observability (Google Cloud Pub/Sub, OpenTelemetry, Cloud Audit Logs)

## Relationships
* API Gateway -> Signaling & Room Manager: Forwards WebSocket signaling [WSS]
* Signaling & Room Manager -> SFU Media Worker: Provisions transport channels [IPC]
* Bandwidth Adaptability Controller -> SFU Media Worker: Adjusts Simulcast/SVC layers dynamically [In-memory API]
* SFU Media Worker <-> TURN Relay: Relays media packets under high-packet-loss conditions [ICE/UDP/TCP]
* Video Consultation Service -> Data Tier: Reads/writes session data [SQL with CMEK over internal GCP network]
* Messaging & Observability -> Video Consultation Service: Propagates revocation events and telemetry [Google Cloud Pub/Sub, OpenTelemetry]

## Technology Stack
* GCP (europe-west3, us-central1): Target cloud provider ensuring strict data residency per region.
* GKE (Google Kubernetes Engine): Container orchestration with regional node pools and HPA.
* Mediasoup WebRTC SFU & Coturn: Media routing and NAT traversal for real-time video/audio.
* Go, Node.js, Python/FastAPI: Container runtime languages for microservices.
* Cloud SQL PostgreSQL & Memorystore: Managed data persistence with CMEK encryption.
* OpenTelemetry & Cloud Audit Logs: Observability and compliance tracking.

## Rationale
Regional GKE container isolation guarantees compliance with GDPR and HIPAA by preventing cross-border data transfer without consent. Integrated TURN relays and the Bandwidth Adaptability Controller maintain reliable video and audio consultations for rural users below 300 kbit/s.