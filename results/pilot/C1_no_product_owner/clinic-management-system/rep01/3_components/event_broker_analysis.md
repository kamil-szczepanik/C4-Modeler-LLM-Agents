## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, EMRs, appointments, and billing for healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and robust clinical interoperability.

## Key Elements
- Patients & Clinic Staff
- External Labs, Imaging Systems & Third-Party Insurance Gateways
- API Gateway (NGINX/Kong)
- Identity Service (Keycloak)
- Patient & EMR Service, Appointment Service, Billing Service (Spring Boot containers)
- HL7 FHIR Integration Engine (Apache Camel)
- Event Broker (Apache Kafka with Strimzi Operator, KRaft controllers, Schema Registry)
- Primary Database & Tiered Storage (PostgreSQL & S3-compatible WORM storage)
- Audit Logging Service

## Relationships
- Patient & EMR Service, Appointment Service, Billing Service -> Event Broker: Publish and consume asynchronous clinical events via TLS-secured TCP [SASL/SCRAM, mTLS]
- HL7 FHIR Integration Engine -> Event Broker: Produces standardized external lab events into ingestion topics [SASL/SCRAM]
- Audit Logging Service -> Event Broker: Consumes all topics asynchronously for security event capture [Scoped Read-Only]
- Event Broker -> MirrorMaker 2: Replicates disaster recovery pipeline data across hybrid boundaries [on-prem-k8s to `eu-central-1`]

## Technology Stack
- Apache Kafka & Strimzi Operator: Chosen for high-throughput, fault-tolerant event-driven microservices messaging.
- KRaft Consensus Mode: Replaces ZooKeeper to minimize operational overhead and metadata latency.
- TLS 1.3 & SASL/SCRAM-512: Secures transport layer and broker authentication for HIPAA compliance.
- PostgreSQL & S3-compatible WORM storage: Provides scalable persistence with a 10-year retention tier.
- Spring Boot & Apache Camel: Powers containerized microservices and HL7 FHIR integration.

## Rationale
This architecture leverages a resilient hybrid Kafka event broker with KRaft consensus and automated GitOps management to guarantee 99.99% uptime and low-latency EMR operations. Strict multi-layer security, including mTLS, topic-level ACLs, and field-level envelope encryption, fulfills rigorous HIPAA and GDPR regulatory mandates.