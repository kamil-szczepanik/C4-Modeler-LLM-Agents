## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures 99.99% availability and HIPAA/GDPR compliance across a hybrid infrastructure.

## Key Elements
- Users: Patients, Clinical Staff, Administrative Staff, Compliance Officers
- External Systems: Lab & Imaging Systems, Payment Gateway & Insurance Clearinghouse, Regulatory & Auditing System
- Containers: API Gateway / BFF (Kong / Envoy), Patient Portal (Node.js / TypeScript), EMR & Scheduling Container (Java Spring Boot), Billing & Claims Container (Python / FastAPI), Analytics & Reporting Container (Apache Pinot / ClickHouse), Data & Messaging Layer
- Data Layer Components: PostgreSQL with TDE, Redis Cluster, Apache Kafka, Debezium Connect Workers, Flyway/Liquibase, Kafka Schema Registry

## Relationships
- EMR & Scheduling Container -> Data & Messaging Layer: Accesses relational storage and distributed cache [gRPC/HTTPS, AES-256, mTLS]
- Microservices -> Data & Messaging Layer: Communicates asynchronously via event choreography [Apache Kafka, TLS 1.3]
- Analytics & Reporting Container -> Data & Messaging Layer: Ingests data streams [Debezium CDC]

## Technology Stack
- PostgreSQL: Provides relational storage with AES-256 TDE and Row-Level Security for strict compliance.
- Redis Cluster: Manages transient sessions and resource clash locks using the Redlock algorithm.
- Apache Kafka: Powers event-driven microservice choreography and Saga pattern rollbacks.
- Debezium: Streams real-time database modifications from PostgreSQL WAL for analytics.
- Flyway/Liquibase: Executes zero-downtime, backward-compatible database schema migrations.
- Kafka Schema Registry: Enforces strict Avro/Protobuf schema evolution rules.

## Rationale
This architecture uses an active-active hybrid model with robust event-streaming and encryption to guarantee 99.99% uptime and a 10-year immutable audit trail. Strict security protocols like mTLS, RLS, and field-level masking ensure full HIPAA and GDPR compliance.