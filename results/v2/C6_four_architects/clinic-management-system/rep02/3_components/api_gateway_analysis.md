## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It provides secure, high-availability clinical operations while maintaining strict HIPAA and GDPR compliance.

## Key Elements
- Envoy / Kong API Gateway (Edge Router, Auth Filter, Rate Limiting Plugin, Audit Interceptor, Data Masking Filter)
- Identity & Policy Container (Keycloak)
- Core Services (Node.js / NestJS) & EMR Service (Java / Spring Boot)
- Integration Service (Apache Camel / Node.js)
- Cache / State Store (Redis Cluster)
- Message Broker (Apache Kafka)

## Relationships
- Clients (Doctors, Nurses, Patients) -> Edge Router: TLS 1.3 [HTTPS]
- Edge Router -> Core Services & EMR Service: Upstream requests [gRPC over mTLS]
- Auth Filter -> Identity & Policy Container: JWKS cache sync [HTTPS]
- Rate Limiting Plugin -> Redis Cluster: Token bucket tracking [RESP / TCP]
- Audit Interceptor -> Apache Kafka: Asynchronous audit logs [TCP / Kafka Protocol]
- Edge Router -> Integration Service: FHIR interoperability requests [gRPC / HTTPS]

## Technology Stack
- Envoy: Selected for native gRPC support, Wasm/Lua filters, and sub-millisecond edge routing.
- Keycloak: Provides OIDC/OAuth2 authentication and JWKS synchronization for zero-trust security.
- Redis Cluster: Ensures distributed, sub-millisecond rate-limiting evaluation to prevent traffic spikes.
- Apache Kafka: Enables asynchronous, non-blocking audit log streaming for HIPAA compliance.

## Rationale
This architecture uses an Envoy-based API Gateway with localized JWKS caching and Redis rate-limiting to meet the strict <1s P95 performance budget. Asynchronous Kafka logging and mTLS upstream routing guarantee 99.99% availability and uncompromising HIPAA/GDPR data security.