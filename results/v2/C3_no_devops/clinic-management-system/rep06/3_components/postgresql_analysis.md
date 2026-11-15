## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient records, appointments, and billing for healthcare facilities while ensuring strict HIPAA and GDPR compliance. It provides high-availability (99.99%) clinical operations, electronic medical records (EMR), and billing services across on-premise Kubernetes and AWS (eu-central-1).

## Key Elements
- **API Gateway**: Kong / Node.js
- **Frontend Containers**: Patient Portal BFF (Node.js / GraphQL), Billing Operations UI (React / Nginx)
- **Backend Services**: Patient & Scheduling Service (Go), EMR Core Service (Spring Boot), Billing & Integration Service (FastAPI)
- **Data & Messaging**: PostgreSQL 16 (Primary Engine, PgBouncer, Patroni / PgBackRest Standby Nodes, pgAudit, Debezium CDC), RabbitMQ
- **External Systems**: Enterprise Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Audit Archival / SIEM System, HashiCorp Vault KMS

## Relationships
- **Patient Portal BFF / Services -> API Gateway**: Handles client requests [HTTPS / REST & GraphQL]
- **Backend Services -> PostgreSQL (PgBouncer)**: Queries and updates transactional data [SQL over TLS / SCRAM-SHA-256]
- **PostgreSQL Primary -> Streaming Standby**: Replicates transactional data [TCP Binary Streaming]
- **PostgreSQL Primary -> Debezium CDC Worker**: Publishes row changes [pgoutput / TCP]
- **Debezium -> RabbitMQ**: Streams asynchronous events [AMQP]
- **Backend Services -> External Lab & Imaging Systems**: Interoperability integrations [HL7 FHIR APIs]

## Technology Stack
- **Database**: PostgreSQL 16 with Patroni for high availability and PgBouncer for connection pooling to maintain sub-second EMR load times.
- **Security & Compliance**: pgAudit and HashiCorp Vault for dynamic secrets, LUKS/TDE for AES-256 at rest, and mTLS for data in transit.
- **Integration & Messaging**: Debezium for change data capture (CDC) and RabbitMQ for asynchronous event messaging.
- **Infrastructure**: Kubernetes (on-premise and AWS eu-central-1) enforcing Calico/Cilium network policies.

## Rationale
This architecture uses an active-active hybrid deployment pattern backed by PostgreSQL replication and connection pooling to meet stringent 99.99% availability and sub-second performance requirements. Comprehensive security controls, including pgAudit, encryption-at-rest, and RLS, ensure full HIPAA and GDPR compliance for sensitive medical data.