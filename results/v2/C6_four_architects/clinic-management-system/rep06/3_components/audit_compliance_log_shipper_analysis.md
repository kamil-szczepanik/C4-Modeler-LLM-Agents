## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It ensures HIPAA/GDPR compliance, 99.99% availability, and a 10-year data retention mandate using a hybrid cloud infrastructure.

## Key Elements
- **Users**: Doctor, Nurse, Receptionist, Billing Officer, Patient, Regulatory/Audit Authority
- **External Systems**: Identity Provider (IdP), External Labs & Imaging Systems, Insurance Payment Gateway, Hospital Notification/SMS Gateway
- **Containers**: Frontend Web App (React SPA), API Gateway (Nginx / Kong), Identity & Access Proxy (OAuth2 Proxy / Keycloak Sidecar), Patient & Scheduling Service (Java / Spring Boot), EMR Service (Node.js / TypeScript), Billing & Claims Service (.NET Core), FHIR Integration Broker (Apache Camel / Python), Async Message Broker (Apache Kafka / RabbitMQ), Audit & Compliance Log Shipper, Patient DB (PostgreSQL), EMR DB (MongoDB), Distributed Cache (Redis), Audit Data Store (AWS S3 / MinIO WORM)
- **Log Shipper Components**: Log Input Collector, Compliance Filter & Transformer, Encryption & Integrity Signer, Local Buffer & Retry Manager, WORM Storage Exporter

## Relationships
- Frontend Web App -> API Gateway: Routes client requests [HTTPS]
- API Gateway -> Identity & Access Proxy: Authenticates requests [OAuth2 / OIDC]
- API Gateway -> Microservices (Patient, EMR, Billing): Forwards validated requests [REST / gRPC]
- FHIR Integration Broker -> External Labs & Imaging Systems: Exchanges health data [HL7 FHIR REST API]
- Log Input Collector -> Compliance Filter & Transformer: Gathers local logs [UNIX sockets / In-process]
- Compliance Filter & Transformer -> Encryption & Integrity Signer: Passes sanitized batches [In-process]
- Encryption & Integrity Signer -> Local Buffer & Retry Manager: Persists signed batches [Local File I/O]
- Local Buffer & Retry Manager -> WORM Storage Exporter: Replays log batches [In-process]
- WORM Storage Exporter -> Audit Data Store: Writes immutable logs [HTTPS / S3 API with TLS 1.3]

## Technology Stack
- **Frontend**: React SPA for responsive client interactions.
- **Backend Services**: Java / Spring Boot, Node.js / TypeScript, and .NET Core for domain-specific workloads.
- **Integration**: Apache Kafka / RabbitMQ for asynchronous messaging; Apache Camel / Python for HL7 FHIR interoperability.
- **Databases**: PostgreSQL (Patient DB), MongoDB (EMR DB), Redis (Distributed Cache), AWS S3 / MinIO WORM (Audit Data Store).
- **Log Shipper**: Fluent Bit and Vector for log collection, Lua-based transformation, HMAC-SHA256 signing, and disk-backed buffering.

## Rationale
This hybrid cloud architecture decouples core clinical services to ensure high availability (99.99%) and low latency. Furthermore, the specialized Audit & Compliance Log Shipper with cryptographic signing and WORM storage guarantees strict adherence to HIPAA, GDPR, and 10-year data retention mandates.