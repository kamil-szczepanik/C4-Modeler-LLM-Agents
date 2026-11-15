## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It utilizes a hybrid cloud architecture to ensure high availability, stringent security, and compliance with healthcare regulations.

## Key Elements
- **Users**: Patient, Clinician / Doctor, Receptionist / Admin, Billing Specialist, Compliance / IT Auditor, Hospital Executive.
- **External Systems**: External Lab & Imaging Systems, Payment Gateway & Insurance Clearinghouse, Identity Provider (IdP), Business Analytics / Reporting Service.
- **Containers**: Frontend Container, Edge Container, Clinical Service, Scheduling Service, Billing Service, Audit & Compliance Log Service, Integration Service / FHIR Facade, Event Bus, Databases, Object Storage.
- **Event Bus Components**: Kafka Broker Cluster (KRaft Mode), Schema Registry (Avro), Kafka Connect (Debezium), DLQ & Retry Router, Event Governance & Access Control Layer (Apache Ranger / mTLS).

## Relationships
- **Frontend Container -> Edge Container**: Routes client traffic [HTTPS / gRPC].
- **Edge Container -> Microservices (Clinical, Scheduling, Billing)**: Reverse proxies authenticated requests [HTTP/2].
- **Microservices -> Event Bus (Kafka Broker Cluster)**: Publishes and consumes domain events [TCP / Kafka Wire Protocol].
- **Microservices -> Schema Registry**: Validates event schemas [HTTP/REST].
- **Microservices -> Event Governance**: Authenticates and authorizes operations [mTLS / SASL/SCRAM].
- **Kafka Broker Cluster -> DLQ & Retry Router**: Forwards unprocessable events [Kafka Wire Protocol].

## Technology Stack
- **Frontend**: TypeScript, React, Nginx/CDN for rapid responsive EMR UI (<1s P95).
- **Edge**: Kong / Envoy for API gateway routing and security enforcement.
- **Microservices**: Go (Clinical, Integration, Audit), Node.js (Scheduling), Java / Spring Boot (Billing) for optimal performance and concurrency.
- **Event Bus**: Apache Kafka (KRaft mode) with Confluent Schema Registry (Avro) and Debezium for reliable asynchronous messaging and CDC.
- **Storage**: PostgreSQL, MongoDB, Redis, and Encrypted S3-compatible Object Storage for ACID compliance and 10-year retention.

## Rationale
This architecture uses an event-driven microservices pattern with Apache Kafka to guarantee 99.99% active-active availability by decoupling critical clinical and billing workflows. Strict security controls, encrypted tiered storage, and hybrid-cloud replication satisfy HIPAA/GDPR mandates and 10-year data retention requirements without sacrificing EMR performance.