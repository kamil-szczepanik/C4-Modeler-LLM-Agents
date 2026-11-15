## Overview
The Core Telehealth Service orchestrates cross-border video consultations, bandwidth adaptability, and regional compliance enforcement for EU and US patients. It ensures uninterrupted clinical interactions across unstable networks while strictly maintaining regional data residency.

## Key Elements
- Consultation Session Manager (Go): Orchestrates video consultation lifecycles and states.
- Bandwidth Adaptability Controller (Go): Monitors QoS and triggers network fallback modes.
- Regional Routing & Audit Interceptor (Go / gRPC Middleware): Enforces data residency and logs access events.
- Fallback Signaling Component (Go): Pushes audio/text fallback states to clients.
- Consent & Audit Logger (Go): Captures cross-border access attempts for compliance.
- GCP GKE & Cloud SQL (PostgreSQL): Regional hosting and isolated database storage.
- GCP HTTP(S) Load Balancer & Redis: Manages persistent WebSocket connections and session affinity.

## Relationships
- API Gateway -> Consultation Session Manager: Initiates session commands [gRPC]
- Consultation Session Manager -> Bandwidth Adaptability Controller: Evaluates QoS metrics [Internal Go Channel]
- Bandwidth Adaptability Controller -> Fallback Signaling Component: Triggers fallback state [Internal Go Channel]
- Regional Routing & Audit Interceptor -> Consent & Audit Logger: Forwards access events [gRPC]
- Fallback Signaling Component -> Client Applications: Pushes fallback commands [WebSocket / HTTPS]

## Technology Stack
- Go: Chosen for high concurrency and low latency in real-time session handling.
- gRPC / Protocol Buffers: High-performance internal communication between microservices.
- WebSockets: Persistent client connectivity for real-time fallback signaling in rural areas.
- OpenTelemetry & Prometheus: Distributed tracing and real-time QoS metric export.
- GCP Cloud SQL & Cloud Storage: Regional persistence ensuring GDPR and HIPAA data residency compliance.

## Rationale
This architecture guarantees low-latency video orchestration and strict regional data isolation required by healthcare regulations. Furthermore, its resilient components ensure continuous care for patients in rural areas with unstable connections.