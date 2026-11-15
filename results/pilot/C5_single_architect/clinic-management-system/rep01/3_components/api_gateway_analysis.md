## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for clinical environments. It provides high-availability, secure, and interoperable clinical IT services compliant with HIPAA and GDPR mandates.

## Key Elements
- Clinic Staff and Patients (Users)
- Identity Provider, Insurance Gateways, and Lab/Imaging Systems (External Systems)
- API Gateway Container (Envoy Proxy, active-active Kubernetes ingress)
- Edge Router Component (Envoy routing tables, HTTP/2, gRPC)
- Auth Filter Component (JWT validation, RBAC)
- Rate Limiter Component (Redis, local token-bucket)
- Audit Logger Component (Apache Kafka)
- Microservices: Patient Management, EMR, Scheduling, Billing (Kubernetes)
- HL7 FHIR Integration Container (Apache Camel)
- PostgreSQL Database (AES-256) and Elasticsearch Audit Trail

## Relationships
- Single Page Application -> API Gateway: Connects for routing and authentication [HTTPS, OAuth2/OIDC]
- API Gateway -> Identity Provider: Validates tokens [HTTPS/OIDC]
- Edge Router -> Patient Management, EMR, Scheduling, Billing Microservices: Routes internal traffic [gRPC, mTLS]
- Audit Logger -> Apache Kafka: Emits structured compliance logs asynchronously [TCP]
- Rate Limiter <-> Redis: Executes distributed sliding window checks [Redis Protocol]

## Technology Stack
- Envoy Proxy: Core API Gateway technology for active-active Kubernetes ingress and high-performance edge routing.
- gRPC & HTTP/2: Upstream multiplexing protocols ensuring EMR screen loads < 1s P95.
- Redis: In-memory distributed cache backing the Rate Limiter for low-latency traffic control.
- Apache Kafka: Messaging backbone for asynchronous compliance and audit log streaming.
- PostgreSQL & Elasticsearch: Data persistence with AES-256 encryption at rest and audit tracking.

## Rationale
This architecture uses active-active Kubernetes deployment with non-blocking Envoy proxying to guarantee 99.99% uptime and sub-second performance. Strict HIPAA and GDPR compliance are continuously enforced via mTLS, JWT validation, Redis rate-limiting, and Kafka-backed audit trails.