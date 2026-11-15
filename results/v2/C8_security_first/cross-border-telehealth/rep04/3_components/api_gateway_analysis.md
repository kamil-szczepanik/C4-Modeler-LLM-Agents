## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, privacy regulations (GDPR/HIPAA), and robust availability for rural users.

## Key Elements
- Patients (EU/US) & Licensed Clinicians
- Google Cloud Load Balancing & Cloud Armor
- Envoy Proxy & Wasm/Lua Auth Filter
- Redis-backed Rate Limiter
- Core Telehealth Service (Node.js / Go)
- E-Prescription Integration Service (Java / Spring Boot)
- AI Symptom Checker Service (Python / FastAPI)
- Janus WebRTC SFU Media Streaming Container

## Relationships
- Patients & Clinicians -> Google Cloud Load Balancing: HTTPS and WSS connections secured via TLS 1.3 [TCP/HTTPS]
- Google Cloud Load Balancing -> Envoy Proxy: Internal VPC routing [Proxy Protocol]
- Envoy Proxy -> Auth Filter: In-memory synchronous validation [Function Call]
- Envoy Proxy -> Rate Limiter: Quota checks [gRPC / Local Loopback]
- Envoy Proxy -> Core Telehealth, E-Prescription, & AI Services: Internal routing with injected JWT claims and W3C trace headers [gRPC over mTLS]
- Envoy Proxy -> Janus WebRTC SFU: Media signaling and streaming [WSS / WebRTC]

## Technology Stack
- Google Cloud Platform (`europe-west3`, `us-central1`): Target cloud infrastructure ensuring regional data residency.
- Envoy Proxy & Google Cloud Load Balancing: Edge routing, TLS termination, WAF protection, and circuit breaking for degraded networks.
- Wasm/Lua Plugins: Edge authentication, JWT validation, and dynamic consent enforcement.
- Redis: Fast edge-based rate limiting to protect downstream AI services.
- gRPC over mTLS: Secure, high-performance internal microservice communication.

## Rationale
This architecture uses regional GCP deployment and strict Envoy routing to ensure EU and US health data never cross borders without explicit consent. Edge-based rate limiting, circuit breaking, and mTLS guarantee high availability for unstable connections while maintaining strict GDPR, HIPAA, and EU MDR compliance.