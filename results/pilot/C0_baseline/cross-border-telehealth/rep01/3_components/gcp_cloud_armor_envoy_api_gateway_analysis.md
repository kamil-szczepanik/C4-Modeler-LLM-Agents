## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency and regulatory compliance under GDPR and HIPAA.

## Key Elements
- Patients and Licensed Clinicians (Users)
- External Pharmacies and National E-Prescription Gateways (External Systems)
- GCP Cloud Armor & Envoy API Gateway (Edge Container)
- Node.js API Gateway, Go Clinical Workspace, Go Consent & Localization Engine (Backend Containers)
- AI Symptom Checker Container (Python, FastAPI)
- mediasoup WebRTC SFU Container

## Relationships
- Patients & Clinicians -> GCP Cloud Armor & Envoy API Gateway: Client requests and video streams [HTTPS/TLS 1.3, WebRTC over UDP/TCP]
- GCP Cloud Armor & Envoy API Gateway -> Node.js API Gateway: Internal API routing [mTLS, gRPC/REST]
- Envoy API Gateway -> Go Consent & Localization Engine: Synchronous token and policy validation [gRPC, Redis Cache]
- Envoy API Gateway -> mediasoup WebRTC SFU: Signaling traffic proxying [HTTP/2, WebRTC]

## Technology Stack
- GCP Cloud Armor: Layer 7 WAF providing geo-based ACLs, DDoS protection, and rate limiting for regional compliance.
- Envoy & GCP Traffic Director: Edge proxy runtime handling dynamic routing, mTLS, and HTTP/2 connection multiplexing.
- Redis: Edge caching layer for validated OAuth2 tokens and consent scopes to minimize latency for rural users.
- GCP Certificate Authority Service: Automates short-lived certificate rotation for secure mTLS tunnels.
- Prometheus & Grafana: Observability stack scraping Envoy `/stats/prometheus` endpoints for latency and circuit breaker monitoring.

## Rationale
This architecture enforces strict regional data residency at the edge using GCP Cloud Armor and Envoy to prevent cross-border data leakage between `europe-west3` and `us-central1`. It incorporates Redis caching and HTTP/2 connection optimization to maintain high availability and performance for rural users with unstable internet connections.