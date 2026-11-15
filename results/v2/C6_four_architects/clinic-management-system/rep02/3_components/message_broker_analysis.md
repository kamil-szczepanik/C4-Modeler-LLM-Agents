## Overview
The Clinic Management System is a clinical IT platform managing patient admissions, EMRs, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, 99.99% uptime, and long-term data management.

## Key Elements
- Apache Kafka (Message Broker container)
- Topic Management & Partitioning Engine
- Access Control & TLS Termination Module
- Schema Registry Component (Confluent Schema Registry / Apicurio)
- Broker Cluster Coordinator (KRaft)
- Log Compaction & Retention Manager
- Dead Letter Queue (DLQ) & Routing Component
- Audit Logging & Compliance Interceptor
- Keycloak (Identity & Policy Container)
- MinIO / AWS S3 (Data Layer)
- Core Services & EMR Service

## Relationships
- Core Services & EMR Service -> Schema Registry: HTTP/TLS for schema validation
- Core Services & EMR Service -> Topic Management Engine: TCP/TLS (Kafka Protocol)
- Access Control Module -> Keycloak: OAuth2/OIDC via HTTPS
- Topic Management Engine <-> Broker Cluster Coordinator: Raft consensus over TCP/TLS
- Log Compaction Manager -> MinIO/S3: HTTPS for historical log tiering
- Topic Management Engine -> DLQ Component: Internal TCP/TLS stream redirection
- Audit Logging Interceptor -> Core Services: TCP/TLS for security audit streams

## Technology Stack
- Apache Kafka: Distributed append-only log architecture for event-driven reliability
- Confluent Schema Registry / Apicurio: Enforces Avro/Protobuf clinical payload contracts
- KRaft: Metadata and leader election without ZooKeeper for high availability
- MinIO / AWS S3: Long-term cold storage for 10-year data retention compliance
- TLS / mTLS: Transport encryption for HIPAA/GDPR compliance

## Rationale
This architecture uses Apache Kafka with KRaft coordination and Schema Registry to guarantee high availability and prevent data corruption across asynchronous clinical workflows. Tiered logging to S3 and automated audit interception directly satisfy 10-year retention and stringent healthcare compliance mandates.