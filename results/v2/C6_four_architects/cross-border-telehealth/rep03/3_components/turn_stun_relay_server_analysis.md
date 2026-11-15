## Overview
Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Ensures strict regional data residency, HIPAA/GDPR compliance, and resilient connectivity for rural patients.

## Key Elements
- Patients and Clinicians (Users)
- TURN/STUN Relay Server (Coturn container)
- STUN/TURN Allocation Manager (C++)
- Media Relay Engine (C++)
- Region-Bound Access Controller (Lua)
- Bandwidth Throttling & Adaptation Module (C++)
- Metrics Exporter Sidecar (Go)
- Load-Balanced Listener & Port Router (C++)
- Video Consultation Service (Node.js / WebRTC SFU)
- Consent & Identity Management Service (Java)
- Audit & Compliance Logger Sidecar (Fluentbit / Go)

## Relationships
- External WebRTC Clients -> Load-Balanced Listener & Port Router: Initiates STUN/TURN requests [STUN/TURN over UDP/TCP/TLS 443/53]
- STUN/TURN Allocation Manager -> Consent & Identity Management Service: Validates HMAC time-limited tokens asynchronously [REST/HTTPS]
- Media Relay Engine -> External WebRTC Clients: Relays adaptive bitrate media streams [SRTP over UDP/TCP]
- Metrics Exporter Sidecar -> Audit & Compliance Logger Sidecar: Exports relay session telemetry [Prometheus/HTTP]
- Video Consultation Service -> STUN/TURN Allocation Manager: Provisions short-term TURN auth tokens

## Technology Stack
- Coturn (C++): Core TURN/STUN engine for robust media relay under restricted firewalls
- HMAC-Based Time-Limited Tokens: Enables low-latency ICE setup without synchronous runtime bottlenecks
- Lua Scripts: Enforces strict geo-routing for regional data residency (`europe-west3` and `us-central1`)
- Prometheus/HTTP: Collects non-PII relay telemetry for compliance auditing
- GCP (europe-west3, us-central1): Cloud infrastructure ensuring isolated regional data storage

## Rationale
This architecture guarantees strict regional data isolation for GDPR and HIPAA compliance while optimizing video delivery for unstable rural connections via multi-port routing and low-latency token authentication.