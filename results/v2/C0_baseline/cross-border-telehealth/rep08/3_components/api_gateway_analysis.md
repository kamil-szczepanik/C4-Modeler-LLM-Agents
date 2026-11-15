## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system enforces strict regional data residency and compliance using GCP and cloud-native microservices.

## Key Elements
- Client Applications (Flutter / Web)
- GCP External HTTP(S) Load Balancer
- API Gateway (Envoy / Google Cloud Endpoints)
- Core Telehealth Service (Go)
- AI Inference Service (Python / FastAPI)
- Interoperability Service (Java / Spring Boot)
- Containerized SFUs (mediasoup)
- Google Kubernetes Engine (GKE) with Istio mTLS mesh
- Regionalized Redis Caches

## Relationships
- Client Applications -> GCP External HTTP(S) Load Balancer: HTTPS / gRPC [TLS 1.3]
- GCP External HTTP(S) Load Balancer -> API Gateway: HTTPS / gRPC
- API Gateway -> Core Telehealth Service: gRPC over Istio mTLS mesh
- API Gateway -> AI Inference Service: gRPC over Istio mTLS mesh
- API Gateway -> Interoperability Service: gRPC over Istio mTLS mesh
- API Gateway -> Containerized SFUs: gRPC over Istio mTLS mesh

## Technology Stack
- GCP Cloud Load Balancing: Handles global geo-routing and region enforcement at the network edge.
- Envoy Proxy: Powers the API Gateway for TLS termination, routing, rate limiting, and resilience.
- Istio Service Mesh: Secures microservice communication with mTLS and SPIFFE/SPIRE identity propagation.
- Redis: Region-local caching for distributed rate limiting without cross-region dependencies.
- Prometheus & Cloud Trace: Observability, distributed tracing, and metric scraping for connection stability.

## Rationale
This architecture guarantees strict regional data separation required by GDPR and HIPAA by utilizing region-isolated infrastructure. Envoy proxy integration ensures stable communication for rural, low-bandwidth users while protecting backend AI and core services from abuse.