## Overview
The Clinic Management System is a clinical IT platform managing patient admissions, EMRs, scheduling, and billing. It features a resilient, hybrid cloud architecture designed for high availability and strict healthcare compliance.

## Key Elements
- Users: Patients, Doctors, Billing Staff
- API Gateway: Kubernetes Ingress, Reverse Proxy
- Domain Services: Patient/EMR Service, Scheduling Service, Billing Service
- Infrastructure: Distributed Cache (Redis), Message Broker (Kafka/RabbitMQ), Secrets Manager (HashiCorp Vault)
- Observability: Prometheus, OpenTelemetry, Falco/Trivy Operator

## Relationships
- Users -> API Gateway: Access registration, scheduling, EMR, and billing [HTTPS / REST / GraphQL]
- API Gateway -> Patient/EMR Service: Routes internal domain requests [gRPC / REST via mTLS]
- API Gateway -> Scheduling Service: Routes internal domain requests [gRPC / REST via mTLS]
- API Gateway -> Billing Service: Routes internal domain requests [gRPC / REST via mTLS]

## Technology Stack
- Kubernetes: Hybrid deployment across on-premises and AWS (eu-central-1) for active-active scalability
- Redis: Distributed cache supporting centralized rate-limiting and session management
- OpenTelemetry: Distributed tracing and correlation ID injection for latency tracking
- gRPC & mTLS: High-performance internal service communication with encrypted transport

## Rationale
The hybrid Kubernetes architecture ensures 99.99% high availability and geo-redundancy. Centralized API Gateway controls enforce HIPAA/GDPR compliance and sub-second performance targets.