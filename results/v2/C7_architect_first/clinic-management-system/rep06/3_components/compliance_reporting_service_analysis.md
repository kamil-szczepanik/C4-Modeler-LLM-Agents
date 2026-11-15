## Overview
The Compliance & Reporting Service manages regulatory compliance, audit logging, and reporting for the Clinic Management System. It ensures strict adherence to HIPAA and GDPR regulations while maintaining high availability and a 10-year data retention mandate.

## Key Elements
- **Compliance Dashboard API**: Spring Boot REST controller handling secure, RBAC-protected ad-hoc queries.
- **Audit Log Processor**: Asynchronous Kafka consumer handling log ingestion, normalization, and cryptographic chaining.
- **Regulatory Report Generator**: Isolated KEDA-scaled worker pool producing encrypted PDF, JSON, and CSV reports.
- **Data Retention Enforcer**: Background lifecycle worker managing the 10-year data archiving policy.
- **WORM Audit Store**: External immutable storage target with cross-region replication and object-lock.
- **CockroachDB & Redis**: Distributed SQL database with read-replicas and in-memory cache with strict TTL.
- **HashiCorp Vault**: KMS managing AES-256 keys for temporary scratch space and export encryption.

## Relationships
- *Core Business Services* -> *Audit Log Processor*: Publishes domain and access events [Kafka over TLS with mTLS].
- *API Gateway* -> *Compliance Dashboard API*: Exposes compliance queries [HTTPS/REST].
- *Compliance Dashboard API* -> *CockroachDB Read-Replicas*: Fetches masked audit metadata [JDBC/TLS].
- *Regulatory Report Generator* -> *HashiCorp Vault*: Fetches encryption keys [HTTPS/TLS].
- *Data Retention Enforcer* & *Regulatory Report Generator* -> *WORM Audit Store*: Archives finalized bundles and verifies health [gRPC/TLS].

## Technology Stack
- **Spring Boot (Java)**: Core framework for service implementation ensuring robust enterprise security features.
- **Kafka / AMQP**: Asynchronous messaging to decouple core clinical transactions from compliance logging.
- **KEDA (Kubernetes Event-driven Autoscaling)**: Dynamically scales worker pods based on queue depth to prevent resource exhaustion.
- **HashiCorp Vault**: Secures temporary scratch spaces and exports with AES-256 encryption.

## Rationale
This architecture isolates heavy reporting workloads to protect real-time EMR performance and maintain the 99.99% availability SLA. Cryptographic chaining and automated cross-region WORM replication satisfy stringent HIPAA and GDPR 10-year retention mandates.