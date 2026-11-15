## Overview
[The Clinic Management System manages patient admissions, EMR, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability, HIPAA/GDPR-compliant clinical IT operations across a hybrid cloud infrastructure.]

## Key Elements
- [Actors: Doctors, Nurses, Receptionists, Billing Staff]
- [External Systems: Identity Provider (IdP), Payment Gateway, Insurance Clearinghouse, External Lab & Imaging Systems]
- [Containers: React SPA, Kong/Envoy API Gateway, Spring Boot Core Clinical, Go Scheduling, .NET Billing & Claims, Node.js Integration/FHIR, Apache Camel Broker, CockroachDB/PostgreSQL, Apache Kafka, Redis Enterprise, Vault/KMS, Elasticsearch, OpenTelemetry/Prometheus/Loki, Istio]
- [API Gateway Components: TLS Termination Ingress, Auth & JWT Filter, Rate Limiting Engine, Routing & Load Balancing Proxy, Audit & Request Logging Interceptor, Circuit Breaker Module, Request Transformation Filter, Token Cache Manager]

## Relationships
- [SPA -> API Gateway: HTTPS / WSS]
- [API Gateway -> Core/Scheduling/Billing/FHIR Services: gRPC over mTLS via Istio]
- [Auth Filter -> Identity Provider: OIDC / JWKS verification via HTTPS]
- [Audit Interceptor -> Apache Kafka: Kafka Protocol over mTLS]

## Technology Stack
- [Frontend: React / TypeScript for responsive user interfaces]
- [API Gateway: Kong / Envoy for routing, rate limiting, and security ingress]
- [Microservices: Spring Boot (Core Clinical), Go (Scheduling), .NET (Billing), Node.js (FHIR)]
- [Database & Caching: CockroachDB / PostgreSQL for distributed storage; Redis Enterprise for state caching]
- [Messaging & Observability: Apache Kafka (Event Bus); OpenTelemetry, Prometheus, Loki (Telemetry)]
- [Security & Mesh: Vault / Cloud KMS (Secrets); Istio (Service Mesh)]

## Rationale
[This hybrid architecture leverages containerized microservices and strict API gateway controls to guarantee 99.99% active-active availability. Robust encryption, audit logging, and RBAC mechanisms ensure full compliance with HIPAA and GDPR regulations.]