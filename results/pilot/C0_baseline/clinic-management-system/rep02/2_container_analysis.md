## Overview
- Hybrid cloud Clinic Management System delivering high availability, strict HIPAA/GDPR compliance, and low-latency EMR access.
- Provides secure patient portals, physician EMRs, scheduling, and billing services across on-premise Kubernetes and AWS.

## Key Elements
- Patients, Receptionists, Physicians, Billing Specialists (Users)
- Go-based API Gateway
- Node.js Patient Portal Frontend
- React Physician EMR Frontend
- Java Spring Boot EMR Backend
- Python Billing Service
- Apache Kafka Event Broker
- PostgreSQL Databases with WORM Audit Log Storage
- External Systems: Payment Gateways, Lab/Imaging Systems, Enterprise IDP

## Relationships
- Patients/Staff to Go API Gateway via HTTPS / OAuth2/OIDC / mTLS
- API Gateway to Node.js / React frontends via HTTPS
- Frontends to Java EMR / Python Billing services via gRPC with mTLS
- Services to Apache Kafka via TLS and SCRAM-SHA-512 for event streaming
- Services to PostgreSQL via encrypted TCP (AES-256)
- External Lab/Imaging Systems to API Gateway via REST/JSON over HTTPS using HL7 FHIR standards

## Technology Stack
- Kubernetes & ArgoCD/Flagger: Hybrid container orchestration and progressive GitOps delivery
- Go, Node.js, React, Java Spring Boot, Python: Polyglot microservices runtime with distroless base images
- Apache Kafka: Asynchronous event-driven messaging and backpressure handling
- PostgreSQL & WORM Storage: Relational data persistence and 10-year immutable audit logging
- OpenTelemetry: Distributed tracing and latency monitoring

## Rationale
- Zero-trust Kubernetes microservices, mTLS, and AES-256 encryption guarantee strict HIPAA/GDPR compliance and data security.
- Active-active hybrid deployment via ArgoCD ensures 99.99% availability and sub-second P95 EMR performance.