## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It uses a hybrid cloud, event-driven architecture to achieve 99.99% availability and strict HIPAA/GDPR compliance.

## Key Elements
- Patients, Clinic Staff, Clinicians, Billing Specialists, Hospital Administrators
- Kong/Envoy API Gateway
- React SPA Web Application
- Patient Portal BFF (Node.js / Spring Boot)
- Core Services & Billing Service (Java, Spring Boot / Node.js)
- Apache Kafka Event Stream (Strimzi Operator, KRaft mode, MirrorMaker 2, Tiered Storage)
- Confluent Schema Registry & Kafka Connect
- PostgreSQL clusters & Redis Enterprise
- WORM object storage (S3 API)
- External IdP, Payment Gateway, and HL7 FHIR Lab Systems

## Relationships
- Patient/Staff -> Kong/Envoy API Gateway: Accesses UI and APIs [HTTPS/TLS]
- Core Services -> Apache Kafka Event Broker: Publishes/Consumes *Clinical Events* and *Financial Events* [Kafka Protocol over mTLS]
- Core Services -> Schema Registry: Validates Avro/Protobuf event payloads [HTTP/REST]
- Event Broker (On-Prem) -> MirrorMaker 2 -> Event Broker (AWS): Replicates topics securely [Kafka Protocol over mTLS]
- Event Broker Cluster -> WORM Object Storage: Offloads historical data via Tiered Storage Manager [HTTPS / S3 API]
- Kafka Connect -> PostgreSQL & WORM: Executes CDC and sinks audit/billing data [Kafka Protocol / S3 API]

## Technology Stack
- Apache Kafka (KRaft mode): Manages event streaming without ZooKeeper to meet high availability.
- Strimzi Operator: Automates Kafka lifecycle, MM2, and `cert-manager` integration on Kubernetes.
- Confluent Schema Registry: Enforces Avro/Protobuf schemas for data integrity and HIPAA compliance.
- Kafka Connect: Handles reliable CDC and S3 sinking.
- MirrorMaker 2: Manages asynchronous cross-site replication between `on-prem-k8s` and `eu-central-1`.
- Tiered Storage: Offloads historical data to WORM object storage to meet retention mandates without local disk exhaustion.
- mTLS & AES-256: Secures transport and at-rest data per security constraints.

## Rationale
The hybrid event-driven architecture with isolated Kafka clusters and MM2 replication guarantees 99.99% availability across on-prem and cloud environments. Automated Tiered Storage and strict mTLS/ACL security controls seamlessly satisfy the 10-year data retention and HIPAA/GDPR compliance mandates.