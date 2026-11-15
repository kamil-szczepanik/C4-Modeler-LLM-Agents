## Overview
The Clinic Management System is a hybrid-cloud healthcare platform designed to manage patient admissions, electronic medical records, appointment scheduling, and billing. Its core purpose is to provide highly available, secure, and interoperable clinical IT operations compliant with HIPAA and GDPR regulations.

## Key Elements
- **Users**: Patients, Doctors, Nurses, Clinic Staff, Hospital Administrators, Billing Specialists.
- **External Systems**: Payment Gateway, Insurance Verification Service, External Lab & Imaging Systems, Public Health Registries.
- **Containers**: API Gateway (Nginx / Envoy), Identity & Access Management (Keycloak / OAuth2 Proxy), Core Services (Spring Boot / Java), Integration Service (Node.js / Apache Camel), Message Broker (Apache Kafka), Data Tier (PostgreSQL), Storage (WORM Object Storage).
- **Message Broker Components**: Ingestion Router (Kafka KRaft), Schema Registry, DLQ Manager, Encryption Key Manager (KMS), Topic Replicator (MirrorMaker 2), Broker Authorization & ACL Enforcement Engine, Operational Audit & Compliance Exporter, Stream Processing / State Handler (Kafka Streams), Broker Health & Metrics Exporter.

## Relationships
- **Core Services -> Ingestion Router**: Publishes domain events via mTLS and Kafka Protocol.
- **Ingestion Router -> Schema Registry**: Validates event schemas via HTTP/REST over TLS.
- **Ingestion Router -> Encryption Key Manager**: Fetches data encryption keys via internal gRPC over TLS.
- **Ingestion Router -> Topic Replicator**: Streams replicated topics for hybrid DR via Kafka TLS.
- **Ingestion Router -> Broker Authorization & ACL Enforcement Engine**: Validates client publish/consume permissions via internal API/Plugin.
- **Ingestion Router -> Operational Audit & Compliance Exporter**: Forwards non-payload access telemetry asynchronously.
- **Ingestion Router -> Stream Processing / State Handler**: Routes raw event streams via internal Kafka Protocol.
- **Stream Processing / State Handler -> DLQ Manager**: Diverts failed processing messages via Kafka Topic.
- **Ingestion Router -> Broker Health & Metrics Exporter**: Exposes Prometheus metrics via HTTP Scrape over TLS.

## Technology Stack
- **Apache Kafka (KRaft mode)**: Selected for message brokering to eliminate ZooKeeper overhead and support high throughput.
- **Confluent Schema Registry**: Enforces strict payload validation for HL7 FHIR and billing events.
- **Kafka Streams**: Manages event aggregations and windowing for complex clinical workflows.
- **PostgreSQL & WORM Object Storage**: Provides structured data persistence and 10-year immutable audit retention.
- **AES-256 with Client-Side Envelope Encryption**: Secures data at rest across hybrid deployments.

## Rationale
This hybrid-cloud architecture combines on-premises Kubernetes and AWS (`eu-central-1`) to achieve 99.99% active-active availability. Strict security protocols, Kafka-based event sourcing, and envelope encryption guarantee HIPAA and GDPR compliance while maintaining sub-second performance.