## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and the US. It enforces strict regional data residency, GDPR/HIPAA compliance, and robust security controls.

## Key Elements
- Global HTTPS Load Balancer (Envoy-based)
- Gateway Authorization Filter
- Rate Limiting & Cost-Control Throttle (Redis Token Bucket)
- gRPC Reverse Proxy / Router
- GCP Cloud Armor (WAF & Threat Protection)

## Relationships
- Web Application & Mobile Apps -> Global HTTPS Load Balancer: Sends client requests and receives data [HTTPS / WSS, TLS 1.3]
- Global HTTPS Load Balancer -> Gateway Authorization Filter: Forwards terminated HTTP/HTTPS requests [HTTP/2]
- Gateway Authorization Filter -> Rate Limiting & Cost-Control Throttle: Checks quota and rate limits [In-memory / Redis lookup]
- Gateway Authorization Filter & Throttle -> gRPC Reverse Proxy / Router: Passes authenticated and authorized requests [Internal IPC]
- gRPC Reverse Proxy / Router -> Core Telehealth Service / AI Orchestrator: Routes external traffic internally [gRPC over mTLS]

## Technology Stack
- Google Cloud API Gateway & Global HTTPS Load Balancer: Provides low-latency edge TLS termination and regional routing for unstable rural connections.
- Google Cloud Armor: Enforces OWASP Top 10 protection, geo-fencing, and bot mitigation.
- Memorystore for Redis: Powers token bucket rate limiting to prevent API exhaustion.
- gRPC over mTLS: Minimizes serialization overhead and secures internal service-to-service communication.
- GCP Certificate Authority Service: Automates certificate rotation for mutual TLS.

## Rationale
This architecture ensures strict regional data isolation between `europe-west3` and `us-central1` by intercepting and validating all requests at the edge. It maintains high availability and security for unstable rural connections through edge termination, rate limiting, and encrypted internal routing.