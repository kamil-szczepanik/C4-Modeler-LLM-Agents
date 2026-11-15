## Overview
The Patient Intake Container manages patient admissions, demographic capture, and audit logging for the Clinic Management System. It ensures high-performance, secure, and compliant data processing across hybrid Kubernetes and cloud environments.

## Key Elements
- Intake API Router (Python / FastAPI with Pydantic)
- Patient Intake Service (Python business logic)
- Data Access Repository (SQLAlchemy / asyncpg)
- Event Publisher (Redpanda Client)
- Envoy / NGINX API Gateway
- Primary Database (PostgreSQL with Citus)
- Event Broker (Redpanda)

## Relationships
- Envoy / NGINX API Gateway -> Intake API Router: Routes intake requests [HTTP/2 / gRPC over mTLS]
- Intake API Router -> Patient Intake Service: Invokes workflow [In-memory / Python function call]
- Patient Intake Service -> Data Access Repository: Persists patient records [Async TCP with envelope encryption]
- Patient Intake Service -> Event Publisher: Dispatches audit events [Async TCP]
- Data Access Repository -> Primary Database: Reads and writes data [Encrypted internal TCP]
- Event Publisher -> Redpanda: Publishes intake events [Encrypted internal TCP]

## Technology Stack
- Python / FastAPI: High-performance asynchronous API endpoints
- Pydantic: Strict schema validation for intake payloads and FHIR compliance
- SQLAlchemy / asyncpg: Asynchronous relational database persistence
- OpenTelemetry: Distributed tracing across gateways, containers, and brokers
- Kubernetes & Vault/KMS: Secret management, non-root container hardening, and HPA scaling

## Rationale
This architecture uses an asynchronous Python/FastAPI stack to guarantee low-latency patient intake while maintaining rigorous HIPAA/GDPR compliance via envelope encryption, JWT validation, and automated audit events. Internal component separation ensures high availability (99.99%) and resilience across hybrid cloud deployments.