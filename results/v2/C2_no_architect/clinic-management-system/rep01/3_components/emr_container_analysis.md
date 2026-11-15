## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to streamline patient care and clinical operations. Its core purpose is to securely manage patient admissions, electronic medical records (EMR), scheduling, and billing while ensuring strict HIPAA/GDPR compliance and 99.99% availability.

## Key Elements
- **Clinicians & Patients**: Primary users accessing clinical services.
- **API Gateway**: Kubernetes Ingress routing client traffic.
- **EMR Container**: Microservice managing electronic medical records and clinical data.
- **PostgreSQL Databases**: Primary data store utilizing Patroni/etcd with active-passive replication.
- **Apache Kafka / RabbitMQ**: Event broker for asynchronous messaging.
- **HashiCorp Vault**: Secrets management and AES-256 key rotation.
- **Immutable Audit Storage Sink**: Secure storage for compliance logs.
- **External Labs/Imaging Vendors**: Third-party clinical systems.

## Relationships
- **API Gateway -> EMR Container**: Routes client requests using HTTPS and mTLS via SPIFFE/SPIRE.
- **EMR Container -> PostgreSQL Databases**: Reads and writes clinical data using SQL with row-level security.
- **EMR Container -> Event Broker**: Publishes and consumes domain events asynchronously using Apache Kafka/RabbitMQ.
- **EMR Container -> External Labs/Imaging Vendors**: Exchanges lab and imaging data via HL7 FHIR protocols over HTTPS.
- **EMR Container -> HashiCorp Vault**: Retrieves encryption keys and manages database credentials securely.

## Technology Stack
- **Kubernetes (on-prem-k8s & eu-central-1)**: Hybrid cloud container orchestration ensuring high availability and rolling updates.
- **PostgreSQL with Patroni/etcd**: Robust relational database ensuring reliable active-passive failover for clinical records.
- **HashiCorp Vault**: Centralized secrets management enforcing AES-256 encryption at rest.
- **HL7 FHIR / REST / gRPC**: Interoperability and internal microservice communication protocols.
- **OpenTelemetry & Prometheus**: Distributed tracing and metrics collection to enforce P95 performance targets.

## Rationale
This architecture guarantees sub-second EMR access and strict compliance through containerized isolation, fine-grained RBAC/ABAC, and cryptographic audit trails. High availability and resilient hybrid-cloud deployment ensure continuous clinical operations even during vendor or infrastructure outages.