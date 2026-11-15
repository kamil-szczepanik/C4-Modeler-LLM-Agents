## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMR, scheduling, and billing. It provides high availability, stringent security, and interoperability for healthcare facilities.

## Key Elements
- **Users**: Hospital Staff, Patients
- **External Systems**: External Lab and Imaging Systems
- **Containers**: API Gateway, Frontend Container, Core Domain Containers (Patient Registration, EMR, Scheduling, Billing), Integration / FHIR Adapter Container, Asynchronous Event Bus (Kafka/RabbitMQ), Audit Logging & Compliance Container, Observability Container (OpenTelemetry), Shared Configuration & Secret Management Sidecar, Database Migration Container, Data Archival Worker, Redis Distributed Rate Limiting Store

## Relationships
- Hospital Staff and Patients interact with the Frontend Container via HTTPS/TLS.
- Frontend and API clients communicate with the API Gateway via HTTPS using JWT/MFA validation.
- API Gateway routes requests to Core Domain Containers via internal gRPC/REST.
- Core Domain Containers publish and consume events via the Asynchronous Event Bus (AMQP/Kafka).
- Integration / FHIR Adapter Container connects to External Lab and Imaging Systems using HL7 FHIR protocols over HTTPS.

## Technology Stack
- **Orchestration**: Kubernetes (`on-prem-k8s`, AWS `eu-central-1`) for active-active multi-region deployment meeting 99.99% uptime.
- **Security**: AES-256 encryption at rest, TLS termination, and OAuth2/JWT for HIPAA/GDPR compliance.
- **Messaging**: Kafka/RabbitMQ for asynchronous, decoupled event-driven workflows.
- **Observability**: OpenTelemetry for end-to-end distributed tracing and metrics collection.
- **Caching & Throttling**: Redis for distributed rate limiting and low-latency access.

## Rationale
- The containerized microservices architecture with an event bus ensures loose coupling, enabling sub-second EMR performance and high fault tolerance.
- A hybrid deployment combining on-premises Kubernetes and AWS `eu-central-1` guarantees active-active high availability (99.99%) and strict regulatory compliance.