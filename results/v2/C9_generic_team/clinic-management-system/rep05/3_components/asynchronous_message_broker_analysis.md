## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals. Its core purpose is to deliver high-availability clinical operations while maintaining strict regulatory compliance for healthcare data.

## Key Elements
- Patients, Practitioners, Administrators
- API Gateway Container (JWT, Rate Limiting)
- Core Domain Containers (Microservices)
- Read-Model / Query Container (CQRS Pattern)
- Integration / Adapter Container (HL7 FHIR, REST)
- Background Worker Container (Asynchronous Worker)
- Asynchronous Message Broker (Apache Kafka)
- Session & State Management Container (Redis)
- External Systems (Insurance Providers, External Labs, IAM, Centralized Audit Logging, DR Storage)

## Relationships
- Patients & Practitioners -> API Gateway Container: Accesses clinical features via HTTPS / TLS 1.3
- API Gateway Container -> Core Domain Containers: Routes validated requests via gRPC / REST
- Core Domain Containers -> Asynchronous Message Broker: Emits domain events via Apache Kafka (TLS 1.3, SASL/SCRAM)
- Asynchronous Message Broker -> Background Worker Container: Consumes asynchronous tasks with manual offset commits
- Integration / Adapter Container -> External Labs: Connects via HL7 FHIR APIs

## Technology Stack
- Apache Kafka: Event-driven asynchronous messaging, chosen for 99.99% availability (R-06) and log compaction support
- Confluent Schema Registry (Avro/Protobuf): Event contract governance ensuring backward compatibility
- Kubernetes: Orchestration platform supporting active-active multi-zone deployments and health probes
- Redis: Session and state management for high-performance retrieval
- AES-256 and TLS 1.3: Data encryption at rest and in transit for HIPAA/GDPR compliance (R-05)

## Rationale
This architecture uses an event-driven microservices pattern with Apache Kafka and Kubernetes to guarantee high availability (≥ 99.99%) and strict partitioning by `PatientID` for causal consistency in clinical workflows. Tiered storage, manual offset commits, and TLS 1.3 ensure long-term data retention (≥ 10 years) and HIPAA/GDPR compliance without performance degradation.