## Overview
The Clinic Management System is a hybrid cloud-based clinical IT platform designed to manage patient admissions, EMRs, scheduling, and billing. It provides high availability, stringent security, and interoperability for medium-sized hospitals and clinics.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists, Compliance Officers
- SPA Frontend (React, TypeScript, Nginx)
- EMR Core Service (Spring Boot, Java)
- Billing & Claims Service (Spring Boot, Java)
- Audit & Compliance Service (Spring Boot, Java)
- Integration Gateway (Apache Camel, Spring Cloud Gateway)
- Apache Kafka Broker Cluster (KRaft mode, Strimzi Operator)
- Schema Registry (Confluent Schema Registry, Avro/Protobuf)
- Kafka Connect, Kafka Interceptor, Kafka ACL & RBAC Authorizer (Apache Ranger)
- PostgreSQL with Patroni (primary-replica)
- Redis Cluster

## Relationships
- SPA Frontend -> Integration Gateway: Routes API requests [HTTPS/JSON]
- Integration Gateway -> EMR Core Service & Billing Service: Dispatches domain requests [gRPC/REST]
- EMR Core Service & Billing Service -> Apache Kafka Broker Cluster: Streams clinical and billing events [TCP, Kafka Wire Protocol]
- Kafka Connect -> PostgreSQL: Persists audit trails and long-term data [JDBC/TCP]
- Schema Registry -> Apache Kafka: Enforces schema validation [HTTP/REST]
- External Lab & Imaging Systems -> Integration Gateway: Exchanges health data [HL7 FHIR REST APIs]

## Technology Stack
- Spring Boot & Java: Powers backend microservices for rapid domain processing
- Apache Kafka (KRaft mode) with Strimzi Operator: Delivers scalable event streaming with high availability on Kubernetes
- PostgreSQL with Patroni & Redis Cluster: Provides reliable transactional persistence and low-latency caching
- Confluent Schema Registry & Apache Ranger: Ensures strict data governance, schema evolution, and RBAC security
- React & TypeScript: Delivers a responsive, type-safe single-page application frontend

## Rationale
This architecture combines active-active hybrid cloud resilience with KRaft-based event streaming to guarantee 99.99% uptime and sub-second EMR performance. Component-level data masking, mTLS encryption, and tiered storage natively satisfy strict HIPAA, GDPR, and 10-year retention mandates.