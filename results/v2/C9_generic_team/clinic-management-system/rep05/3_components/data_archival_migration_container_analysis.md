## Overview
The Clinic Management System is a hybrid-cloud healthcare IT platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high availability (99.99%) and strict HIPAA/GDPR compliance for medium-sized hospitals and clinics.

## Key Elements
- **API Gateway Container**: Manages incoming traffic, JWT validation, and rate limiting.
- **Core Domain Containers**: Microservices handling patient registration, scheduling, EMR, and billing logic.
- **Data Archival & Migration Container**: Executes asynchronous data offloading for 10-year retention.
- **Asynchronous Message Broker**: Apache Kafka / RabbitMQ managing inter-service communication.
- **Data Stores**: Primary transactional database and air-gapped DR Storage Targets.

## Relationships
- **Clients -> API Gateway Container**: HTTPS / REST / GraphQL with mutual TLS and multi-factor authentication.
- **API Gateway Container -> Core Domain Containers**: Internal gRPC / HTTP with Envoy Sidecar proxies.
- **Core Domain Containers -> Asynchronous Message Broker**: Pub/Sub messaging for event-driven workflows.
- **Data Archival & Migration Container -> DR Storage Targets**: Encrypted storage transfer using TLS 1.3 with SHA-256 cryptographic checksums.

## Technology Stack
- **Languages & Runtimes**: Containerized microservices deployed on Kubernetes (on-prem-k8s and AWS eu-central-1).
- **Serialization**: Apache Parquet / Avro with schema registry integration for long-term EMR readability.
- **State Management**: Redis for high-water mark offset persistence and session management.
- **Security**: AES-256 encryption at rest, TLS 1.3 in transit, SHA-256 checksums, and cryptographic manifest verification.

## Rationale
This hybrid architecture decouples resource-intensive archival tasks from core transactional workflows, ensuring sub-second EMR load performance. Asynchronous batch processing, write-verify-delete lifecycles, and cryptographic checks guarantee data integrity and strict 10-year regulatory compliance without sacrificing 99.99% system availability.