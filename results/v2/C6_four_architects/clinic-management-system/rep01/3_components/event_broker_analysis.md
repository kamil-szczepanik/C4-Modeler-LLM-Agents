## Overview
The Clinic Management System is a hybrid healthcare platform designed to manage patient admissions, EMRs, scheduling, and billing while ensuring strict HIPAA/GDPR compliance. It provides high-availability (99.99%) clinical operations across on-premise Kubernetes and AWS (`eu-central-1`).

## Key Elements
- **Users:** Patient, Clinician / Staff, Hospital Administrator
- **External Systems:** Identity Provider (IdP), Insurance Gateway, External Lab & Imaging Systems, Notification Gateway, Cloud Backup (AWS S3 Glacier)
- **Containers:** API Gateway (Kong/Envoy), Web Frontend (React/TypeScript / Nginx/CloudFront), Core Services Container (Java/Spring Boot), EMR Service (Node.js/TypeScript), Database Layer (PostgreSQL), Integration Worker (Apache Camel/Python), Event Broker (Apache Kafka), Audit Log Store (PostgreSQL / AWS S3 Glacier), Key Management Service (HashiCorp Vault / AWS KMS), Background Job Scheduler (Temporal.io), Global Load Balancer (AWS Route 53 / Envoy Global), Observability Collector (OpenTelemetry / Prometheus / Grafana Loki)
- **Event Broker Components:** Kafka Broker Nodes (KRaft), Confluent Schema Registry, Kafka Connect, Client-Side Interceptor Component, Kafka MirrorMaker 2, Topic Authorization & Access Control Component (Kafka ACLs), Broker Health & Partition Rebalancer (Kafka Cruise Control), Dead Letter Queue (DLQ) Manager

## Relationships
- **API Gateway -> Core Services Container:** Routes incoming client traffic [HTTPS/REST]
- **Core Services Container -> Database Layer:** Reads and writes clinical records [JDBC/SQL over TLS]
- **Core Services Container & Integration Worker -> Event Broker:** Streams asynchronous messages [Kafka over TLS]
- **Event Broker -> Key Management Service (KMS):** Fetches encryption keys [gRPC over mTLS]
- **Event Broker Nodes (On-Prem) -> Event Broker Nodes (AWS):** Replicates topics cross-datacenter [Kafka over mTLS via MirrorMaker 2]
- **Integration Worker -> External Lab & Imaging Systems:** Exchanges clinical data [HL7 FHIR APIs over HTTPS]

## Technology Stack
- **Languages & Frameworks:** Java (Spring Boot), Node.js (TypeScript), React (TypeScript) for core business logic and UI.
- **Messaging & Integration:** Apache Kafka (KRaft mode) with Confluent Schema Registry and Apache Kafka Connect for asynchronous decoupling.
- **Security & Compliance:** HashiCorp Vault / AWS KMS and Client-Side Interceptors for AES-256 envelope encryption; OAuth/OIDC with mTLS for access control.
- **Infrastructure & Deployment:** Hybrid Kubernetes (on-prem) and AWS (`eu-central-1`) managed via Apache MirrorMaker 2 and Kafka Cruise Control.

## Rationale
This hybrid architecture uses active-active deployment and KRaft-based Kafka brokers to achieve 99.99% availability and low-latency EMR performance. Client-side encryption, robust audit logging, and strict HL7 FHIR interoperability ensure full HIPAA/GDPR compliance and secure cross-boundary integration.