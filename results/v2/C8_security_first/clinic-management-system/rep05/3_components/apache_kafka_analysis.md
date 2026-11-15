## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and long-term data retention.

## Key Elements
- **Users**: Patient / Consumer, Clinic Staff / Receptionist, Clinician / Doctor, Billing Specialist / Administrator
- **External Systems**: Patient Portal Interface, External Lab & Imaging Systems, Insurance Claim Clearinghouse, Enterprise Identity Provider (IdP), SMS/Email Notification System
- **Containers**: Envoy Proxy API Gateway, OAuth2-Proxy / Keycloak Sidecar, EMR & Patient Service (Node.js / Fastify), Billing & Claims Service (Java Spring Boot), FHIR Interoperability Gateway (HAPI FHIR), PostgreSQL (CloudNativePG with AES-256), Apache Kafka
- **Kafka Components**: Kafka Broker (Java/Scala with KRaft), Schema Registry (Confluent), Tiered Storage Manager, Kafka MirrorMaker 2 (MM2)

## Relationships
- **Microservices to Kafka Broker**: TCP with TLS 1.3/mTLS and SASL/OAUTHBEARER authentication for event publishing/consuming.
- **Kafka Broker to Schema Registry**: HTTPS for Avro/Protobuf schema validation and data masking.
- **Kafka Broker to Tiered Storage Manager**: Native plug-in API over TLS 1.3 using AWS IRSA to offload logs to AWS S3 (`eu-central-1`).
- **Cross-Site Replication**: Kafka MirrorMaker 2 (MM2) asynchronous replication between on-prem-k8s and AWS `eu-central-1`.

## Technology Stack
- **API & Compute**: Node.js / Fastify, Java Spring Boot, Envoy Proxy for low latency and high throughput.
- **Messaging & Streaming**: Apache Kafka with KRaft mode, Strimzi Operator, and MirrorMaker 2 for resilient distributed messaging.
- **Data & Storage**: PostgreSQL (CloudNativePG) with AES-256 encryption at rest; AWS S3 with customer-managed keys (CMK) for 10-year retention.
- **Security & Interoperability**: Keycloak (OAuth2-Proxy), HAPI FHIR (HL7 FHIR APIs), TLS 1.3, and mTLS.

## Rationale
This architecture uses independent event streaming clusters linked by MirrorMaker 2 to avoid WAN latency penalties while maintaining 99.99% uptime. Strict encryption, schema validation, and tiered storage meet rigorous HIPAA, GDPR, and 10-year retention mandates without compromising EMR performance.