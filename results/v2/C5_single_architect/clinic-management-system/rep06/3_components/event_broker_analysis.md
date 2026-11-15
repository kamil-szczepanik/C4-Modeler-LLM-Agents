## Overview
The Clinic Management System is a hybrid cloud clinical IT platform designed to handle patient admissions, electronic medical records, scheduling, and billing. It provides high availability, stringent security, and interoperability for medium-sized hospitals and clinics.

## Key Elements
- **Users**: Patient / User, Clinician / Staff, Hospital Administrator
- **External Systems**: External Lab & Imaging Systems, Insurance Payment Gateways, Identity Provider (IdP), SMS / Notification Gateway, Regulatory Compliance / Auditing Authority
- **Containers**: API Gateway (NGINX / Envoy), Web Application (React / TypeScript), Core Clinic Service (Java / Spring Boot), Scheduling Service (Go), Billing Service (Node.js), Integration Service (Apache Camel / Spring Integration), Event Broker (Apache Kafka / RabbitMQ), PostgreSQL Database (PostgreSQL with AES-256), Redis Cache (Redis)
- **Event Broker Components**: Ingestion & Routing Engine (Apache Kafka Brokers), Schema Registry (Confluent Schema Registry / Apicurio), Audit Log Interceptor (Custom Kafka Streams / Log Compaction), Replication & Mirroring Agent (Apache Kafka MirrorMaker 2 / Confluent Cluster Linking)

## Relationships
- **Core Clinic Service / Billing Service** -> **Ingestion & Routing Engine**: Publishes asynchronous domain events via `TCP / Kafka Protocol` and `AMQP / Kafka protocol`.
- **Ingestion & Routing Engine** -> **Schema Registry**: Validates event payloads via `HTTP/REST`.
- **Integration Service** -> **Ingestion & Routing Engine**: Consumes clinical events for HL7 FHIR export via `Kafka Protocol`.
- **Ingestion & Routing Engine** -> **Replication & Mirroring Agent**: Streams cross-site replication data via `TCP / Kafka Protocol`.
- **Audit Log Interceptor** -> **PostgreSQL Database**: Persists immutable event audit trails via `JDBC / TLS`.

## Technology Stack
- **Languages & Frameworks**: Java / Spring Boot, Go, Node.js, React / TypeScript for microservices and UI.
- **Messaging & Integration**: Apache Kafka / RabbitMQ with Apache Kafka Brokers, Confluent Schema Registry, and Kafka MirrorMaker 2 for asynchronous event-driven architecture and cross-site replication.
- **Storage & Security**: PostgreSQL with AES-256 encryption at rest, Redis Cache, and NGINX / Envoy API Gateway.
- **Deployment**: Hybrid cloud across `on-prem-k8s` and AWS `eu-central-1`.

## Rationale
This architecture guarantees 99.99% active-active availability across hybrid environments using Kafka replication and microservices. It fulfills strict HIPAA/GDPR compliance and 10-year data retention mandates through AES-256 encryption, immutable audit trails, and standardized HL7 FHIR interoperability.