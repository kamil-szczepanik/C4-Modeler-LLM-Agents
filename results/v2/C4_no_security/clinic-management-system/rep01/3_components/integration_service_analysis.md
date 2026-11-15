## Overview
The Clinic Management System is an enterprise healthcare platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized clinics. It ensures 99.99% availability and strict HIPAA/GDPR compliance across hybrid cloud environments.

## Key Elements
- **API Gateway**: Kong / NGINX handling ingress traffic via HTTPS / TLS 1.3.
- **Service Mesh**: Istio / Linkerd providing secure service-to-service communication via gRPC over mTLS.
- **Message Routing & Transformation Engine**: Spring Integration (Enterprise Integration Patterns) handling core routing and splitting.
- **FHIR Adapter Component**: Apache Camel REST/FHIR components transforming payloads into HL7 FHIR.
- **Dead Letter Queue (DLQ) Manager**: RabbitMQ / Kafka topics capturing failed messages with AES-256 encryption.
- **Integration Health & Replay API Component**: Spring Boot Actuator / Camel REST DSL exposing endpoints for administrative dashboards.
- **Audit & Compliance Service**: Spring Boot / Python collecting immutable audit trails.

## Relationships
- **API Gateway** -> **Message Routing & Transformation Engine**: Ingests outbound integration requests [gRPC over Istio mTLS]
- **Message Routing & Transformation Engine** -> **FHIR Adapter Component**: Dispatches formatted clinical payloads [In-memory]
- **FHIR Adapter Component** -> **External Lab & Imaging Systems**: Submits clinical data [HL7 FHIR over HTTPS, TLS 1.3]
- **Message Routing & Transformation Engine** -> **DLQ Manager**: Offloads poisoned messages [AMQP / Kafka protocol]
- **Integration Operations Widget** -> **Integration Health & Replay API Component**: Queries failure statuses and triggers replays [HTTPS / REST]
- **Integration Health & Replay API Component** -> **DLQ Manager**: Inspects and replays failed messages [AMQP / Kafka admin API]
- **Integration Health & Replay API Component** -> **Audit & Compliance Service**: Emits immutable audit logs for manual replays [gRPC / mTLS]

## Technology Stack
- **Integration Framework**: Apache Camel & Spring Integration for reliable enterprise messaging and EIP patterns.
- **Messaging Broker**: RabbitMQ / Kafka for asynchronous decoupling, DLQ management, and consumer-lag autoscaling.
- **Security & Compliance**: AES-256 for data at rest and in DLQ storage, OAuth2 / OIDC via IdP for RBAC.
- **Infrastructure**: Kubernetes (on-prem-k8s and eu-central-1) with Istio service mesh and Prometheus / OpenTelemetry observability.

## Rationale
This architecture decouples high-throughput clinical routing from administrative replay workflows, protecting system availability (R-099.99%) during high-volume bursts. It uses industry-standard HL7 FHIR and robust queuing patterns to guarantee HIPAA/GDPR compliance, zero data loss, and seamless external interoperability (R-08).