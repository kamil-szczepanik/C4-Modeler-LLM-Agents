## Overview
The Clinic Management System is a hybrid cloud clinical IT solution designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. Its core purpose is to provide highly available, secure, and interoperable healthcare operations complying with HIPAA and GDPR regulations.

## Key Elements
- **Users**: Patients, Doctors, Administrators
- **External Systems**: Identity Provider, Third-Party Billing Gateway, External Lab/Imaging Systems, Notification Gateway, Cloud Backup Archive
- **Containers**: Web Frontend (React / TypeScript / NGINX), API Gateway (Kong / NGINX), Core Microservices (Go / Spring Boot), Background Worker (Go / Celery), Integration Service (Apache Camel / Node.js), Message Broker (Apache Kafka with KRaft), PostgreSQL (AES-256), Object Storage (MinIO / S3), Caching & Session Container (Redis Enterprise), Audit & Compliance Logging (FluentBit / OpenSearch), Backup & Archive Manager (Velero / AWS Backup)
- **Message Broker Components**: Kafka Broker Nodes (KRaft mode), Schema Registry, Kafka Connect, Kafka REST Proxy, Access Control List (ACL) Authorizer, Encryption & Key Manager, Partition Rebalancer / Controller, Dead Letter Queue (DLQ) Manager, Topic Mirroring Agent (MirrorMaker 2), Metrics & Telemetry Exporter

## Relationships
- **Core Microservices -> Message Broker**: Publishes domain events [TCP / TLS 1.3 (Kafka protocol)]
- **Message Broker -> Background Worker**: Consumes streaming events for asynchronous processing [TCP / TLS 1.3 (Kafka protocol)]
- **Integration Service -> Kafka REST Proxy**: Ingests external lab/imaging messages via authenticated HTTP [HTTPS / TLS 1.3]
- **ACL Authorizer -> Kafka Broker Nodes**: Validates client credentials and topic permissions [Internal gRPC / TLS 1.3]
- **Kafka Broker Nodes -> Encryption & Key Manager**: Encrypts sensitive EMR and demographic payloads at rest [Internal API / TLS 1.3]
- **Topic Mirroring Agent -> Kafka Broker Nodes**: Synchronizes partition logs bidirectionally across hybrid boundary [Kafka Protocol / TLS 1.3]
- **Message Broker -> Audit & Compliance Logging**: Streams audit trails and security events [gRPC / TLS 1.3]

## Technology Stack
- **Apache Kafka (KRaft mode)**: Selected for immutable append-only event logs, satisfying 10-year data retention and HIPAA audit requirements without ZooKeeper overhead.
- **TLS 1.3 & AES-256**: Ensures cryptographic transit security and data-at-rest protection for HIPAA/GDPR compliance.
- **Go / Spring Boot**: High-performance runtimes for Core Microservices and Background Workers ensuring low-latency EMR screen loads (< 1 s P95).
- **PostgreSQL & Redis Enterprise**: Provides robust relational persistence with AES-256 encryption and ultra-fast session caching.
- **MirrorMaker 2**: Enables active-active cross-site replication between on-premise Kubernetes and AWS (`eu-central-1`) to achieve 99.99% availability.

## Rationale
This architecture uses a hybrid cloud model with Apache Kafka to satisfy stringent 99.99% availability and 10-year data retention constraints. Component-level isolation via KRaft, strict ACLs, and end-to-end encryption ensure comprehensive HIPAA and GDPR compliance.