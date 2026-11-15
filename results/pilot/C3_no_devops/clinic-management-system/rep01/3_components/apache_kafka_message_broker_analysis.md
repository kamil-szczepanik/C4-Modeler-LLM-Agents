## Overview
The Clinic Management System is an event-driven healthcare platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, robust security, and seamless interoperability while maintaining compliance with HIPAA and GDPR regulations.

## Key Elements
- Patients, Receptionists, Clinical Staff, Billing Specialists
- External Systems: External Labs/Imaging, Insurance Clearinghouses, Payment Gateways, Product Analytics, Identity Provider
- Containers: API Gateway, Patient Portal Service, Scheduling Service, EMR Service, Billing Service, HL7 FHIR Integration Service, Analytics Service, PostgreSQL Database, Apache Kafka Message Broker, External Vault/HSM
- Kafka Components: Kafka Broker (JVM-based stateful process), KRaft controller nodes, local log segment storage volumes, Kafka Streams PII-masking processor, Schema Registry

## Relationships
- Patient Portal Service -> Apache Kafka Message Broker: Publishes asynchronous events [Internal TLS]
- Scheduling Service -> Apache Kafka Message Broker: Publishes asynchronous events [Internal TLS]
- EMR Service -> Apache Kafka Message Broker: Publishes asynchronous events [Internal TLS]
- Billing Service -> Apache Kafka Message Broker: Publishes asynchronous events [Internal TLS]
- Kafka Streams -> Analytics Service: Publishes sanitized projection events [Internal TLS]
- Microservices -> External Vault/HSM: Manages encryption keys [mTLS]

## Technology Stack
- Hybrid Kubernetes (on-prem-k8s, eu-central-1): Supports active-active deployment and high availability.
- Apache Kafka: Event broker for decoupled, asynchronous workflow triggers with replication factor 3 and `min.insync.replicas=2`.
- Mutual TLS (mTLS) & SASL/SCRAM: Secures client and inter-broker communication.
- AES-256 & External Vault/HSM: Encrypts data at rest with automated key rotation.
- Avro Serialization & Schema Registry: Enforces strict schema rules for event streams.

## Rationale
This architecture ensures 99.99% high availability and active-active scaling through distributed Kubernetes clusters and Apache Kafka. It satisfies strict HIPAA, GDPR, and 10-year data retention mandates via end-to-end encryption, mTLS, application-layer tokenization, and strict ACL isolation.