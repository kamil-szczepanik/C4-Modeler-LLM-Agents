## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients while ensuring strict regional data residency. The API Gateway manages secure ingress traffic, enforces data residency, and handles resilience for unstable connections.]

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Web Frontend (PWA) built with Next.js / React
- API Gateway container using Google Cloud Load Balancing and Envoy Proxy
- Core Backend services (Go / Spring Boot)
- AI Symptom Checker (Python / FastAPI)
- Edge Load Balancer (Google Cloud Load Balancing)
- Routing & Regional Affinity Engine (Envoy Proxy)
- Security & Policy Filter (Envoy WASM Plugin)
- Resilience & Telemetry Adapter (Envoy Circuit Breaker & Stats Filter)
- Audit & Logging Interceptor (Envoy gRPC Access Log Service - ALS)

## Relationships
- Web Frontend -> Edge Load Balancer [HTTPS / WSS]
- Edge Load Balancer -> Routing & Regional Affinity Engine [gRPC]
- Routing & Regional Affinity Engine -> Core Backend services [gRPC / REST, regionalized per R-05]
- Security & Policy Filter -> Core Backend services [Internal Consent Header Propagation]
- Audit & Logging Interceptor -> Cloud Logging [Asynchronous gRPC ALS streams]

## Technology Stack
- Google Cloud Platform (GCP) across `europe-west3` and `us-central1` regions for regional data residency enforcement
- Envoy Proxy and Google Cloud Load Balancing for high-performance ingress routing and circuit breaking
- WebAssembly (WASM) for efficient, low-latency JWT validation and consent header injection
- gRPC Access Log Service (ALS) for asynchronous, non-blocking compliance auditing

## Rationale
[This architecture enforces strict regional containment to satisfy GDPR and HIPAA data residency mandates without failing over across regions. Furthermore, it integrates resilient traffic management and asynchronous logging to support rural connectivity needs and regulatory accountability.]