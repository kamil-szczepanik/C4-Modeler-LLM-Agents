## Overview
The Clinic Management System is a hybrid-cloud healthcare platform providing patient registration, EMR, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and sub-second EMR performance.

## Key Elements
- **Users:** Patients, Clinical Staff, Administrative & Billing Staff, Hospital IT / Compliance Officers
- **External Systems:** Identity Provider, Third-Party Payment Gateway, External Lab & Imaging Systems
- **Containers:** API Gateway (Kong / Envoy / Istio), EMR & Scheduling Service (Java Spring Boot / Node.js NestJS), Billing & Claims Service (Java Spring Boot), Integration Engine (HAPI FHIR), Data Tier (PostgreSQL), Event Broker (Apache Kafka)
- **API Gateway Components:** Edge TLS Termination & Router, Auth & Policy Enforcement (OAuth2/OIDC + OPA), Rate Limiting & Traffic Shaping (Redis), Telemetry & Audit Component, Circuit Breaker & Resilience Component

## Relationships
- Patients, Clinical Staff, Administrative & Billing Staff, Hospital IT -> API Gateway: Accesses portals, records, and compliance tools [HTTPS (TLS 1.3)]
- API Gateway -> EMR & Scheduling Service: Routes validated requests [gRPC over mTLS]
- API Gateway -> Billing & Claims Service: Routes billing requests [gRPC over mTLS]
- API Gateway -> Identity Provider: Validates OAuth 2.0 / OIDC tokens [HTTPS]
- API Gateway -> Redis: Checks quotas and token revocation blacklist [TCP]

## Technology Stack
- **API Gateway:** Kong / Envoy / Istio proxy for perimeter routing and mTLS
- **Backend Services:** Java Spring Boot and Node.js NestJS for high-performance microservices
- **Database:** PostgreSQL with AES-256 encryption at rest for data persistence
- **Caching & Rate Limiting:** Redis cluster for token blacklisting and rate-limiting states
- **Observability:** OpenTelemetry and Prometheus for hybrid-cloud telemetry and PHI-sanitized audit logging
- **Deployment:** Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) with Anycast DNS

## Rationale
The hybrid architecture utilizes Anycast DNS and active-active Kubernetes clusters to guarantee 99.99% availability across regions. Edge-terminated mTLS, local JWT caching, and OPA policy enforcement achieve strict HIPAA/GDPR compliance with sub-millisecond overhead.