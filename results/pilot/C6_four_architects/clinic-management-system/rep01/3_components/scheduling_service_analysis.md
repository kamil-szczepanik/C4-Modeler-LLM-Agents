## Overview
• The Clinic Management System manages patient admissions, EMR, scheduling, and billing for healthcare institutions.
• It ensures high availability, strict HIPAA/GDPR compliance, and seamless interoperability via a hybrid cloud deployment.

## Key Elements
• Patients, Clinical Staff, Hospital Administrators
• API Gateway (Kong/Envoy), Hybrid VPN Gateway (WireGuard)
• Patient & EMR Service, Scheduling Service, Billing Service, HL7 FHIR Adapter
• PostgreSQL Cluster, Redis Enterprise, Apache Kafka StatefulSet, RabbitMQ, Elasticsearch, ClickHouse, MinIO
• Envoy Service Mesh, Observability Collector (OpenTelemetry, Prometheus)

## Relationships
• PWA Client -> API Gateway Container: HTTPS/REST, gRPC
• API Gateway Container -> Microservices: Internal routing via gRPC, OAuth2/OIDC
• Scheduling Service -> PostgreSQL Container cluster: SQL over TLS
• Scheduling Service -> Redis Enterprise: RESP protocol
• Scheduling Service -> Apache Kafka StatefulSet: TCP / Kafka binary protocol
• HL7 FHIR Adapter -> External Lab/Imaging Systems: HL7 FHIR APIs

## Technology Stack
• Node.js & Docker/Kubernetes: Core microservice runtime and container orchestration for horizontal scaling.
• PostgreSQL (CloudNativePG): Relational persistence ensuring ACID compliance for critical medical records.
• Redis Enterprise: Sub-millisecond slot availability checks and distributed locking (Redlock).
• Apache Kafka: Event-driven decoupling and asynchronous domain event streaming.
• OpenTelemetry & Prometheus: Real-time telemetry, tracing, and metric collection for 99.99% uptime.

## Rationale
• The hybrid microservices architecture ensures 99.99% high availability and active-active fault tolerance across on-premises Kubernetes and AWS eu-central-1.
• Decoupled event streaming and distributed caching guarantee sub-second performance for critical clinical workflows while strictly enforcing HIPAA/GDPR security mandates.