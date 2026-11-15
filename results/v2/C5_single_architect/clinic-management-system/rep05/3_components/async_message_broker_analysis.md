## Overview
The Clinic Management System is a hybrid cloud platform designed to handle patient admissions, EMRs, scheduling, and billing for clinical environments. It ensures high availability, strict security, and long-term regulatory compliance.

## Key Elements
- **Web Application Frontend**: React / TypeScript via CDN/Nginx.
- **API Gateway**: Kong / Nginx.
- **Core Services Container**: Java Spring Boot / Node.js.
- **EMR & Audit Service**: Java Spring Boot.
- **Billing & Insurance Integration Worker**: Node.js / Java.
- **Async Message Broker**: Apache Kafka.
- **Kafka Components**: Event Ingestion & Routing Engine, Schema Registry, Consumer Offset Manager, Access Control & Audit Interceptor, Replication & Mirroring Agent (MirrorMaker 2).
- **PostgreSQL Primary DB**: Multi-region active-active with AES-256 encryption.
- **WORM-compliant storage**: Long-term data retention.

## Relationships
- **Web Application Frontend -> API Gateway**: HTTPS / REST / GraphQL.
- **API Gateway -> Core Services Container**: Internal gRPC / HTTP.
- **Core Services Container -> Async Message Broker**: Publishes domain events [Kafka Protocol / TCP].
- **EMR & Audit Service -> Async Message Broker**: Publishes immutable audit and EMR state change events [Kafka Protocol / TCP].
- **Billing & Insurance Integration Worker -> Async Message Broker**: Consumes claims events [Kafka Protocol / TCP].
- **Access Control & Audit Interceptor -> PostgreSQL Primary DB**: Persists broker audit logs and ACL metadata [JDBC / TLS].
- **Core Services Container -> PostgreSQL Primary DB**: Encrypted SQL queries [JDBC / TLS 1.3].
- **External Systems -> API Gateway**: HL7 FHIR APIs and mTLS.

## Technology Stack
- **Frontend**: React, TypeScript, Nginx for fast UI rendering.
- **Backend Services**: Java Spring Boot and Node.js for robust business logic.
- **Messaging**: Apache Kafka for decoupled, resilient asynchronous messaging and high availability.
- **Database**: PostgreSQL with multi-region active-active replication for 99.99% uptime.
- **Security**: AES-256 encryption, TLS, and Kafka ACLs for HIPAA/GDPR compliance.
- **Infrastructure**: On-premise Kubernetes and AWS (`eu-central-1`) via hybrid deployment.

## Rationale
This architecture uses a hybrid multi-region active-active deployment with Apache Kafka and PostgreSQL to meet the strict 99.99% uptime and <1s EMR performance requirements. Robust encryption, auditing components, and WORM storage ensure full HIPAA and GDPR compliance for sensitive clinical data.