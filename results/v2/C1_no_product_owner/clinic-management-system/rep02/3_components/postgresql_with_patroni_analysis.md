## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for healthcare facilities. It ensures high availability (99.99%), stringent HIPAA/GDPR compliance, and 10-year data retention.

## Key Elements
- **API Gateway & Service Mesh:** Envoy and Istio
- **Core Microservices:** Patient & Scheduling Service (Node.js/Go), EMR Core Service (Java/Spring Boot), Billing & Integration Service (Python/FastAPI)
- **Database Components:** PostgreSQL 15+, Patroni Daemon, Distributed Configuration Store (Etcd), PgBouncer, pgBackRest, Prometheus Exporters
- **Infrastructure & Security:** WORM-compliant S3/MinIO, HashiCorp Vault, Kubernetes

## Relationships
- **Patient/EMR/Billing Services -> PgBouncer:** Encrypted SQL queries over TLS [TCP 6432]
- **PgBouncer -> PostgreSQL Instance:** Local socket or TLS-encrypted SQL [TCP 5432]
- **Patroni Daemon <-> Etcd:** Consensus and leader lock [HTTPS/gRPC]
- **PostgreSQL Instance -> pgBackRest:** Continuous WAL archiving and backups [Encrypted File Transfer]
- **pgBackRest -> WORM-compliant S3 / MinIO:** Stores encrypted backups for 10-year retention [HTTPS/S3 API]
- **External Systems -> Envoy:** HL7 FHIR APIs and payment processing [HTTPS]

## Technology Stack
- **PostgreSQL with Patroni:** Primary datastore ensuring active-passive high availability failover.
- **Etcd:** Distributed configuration store maintaining cluster consensus.
- **PgBouncer:** Connection pooling to handle high concurrent service loads.
- **pgBackRest:** Backup and disaster recovery tool integrated with S3/MinIO for 10-year retention.
- **HashiCorp Vault:** Manages mTLS certificates, credential rotation, and AES-256 encryption keys.
- **Prometheus Exporters:** Sidecar components for monitoring replication lag and connection pool saturation.

## Rationale
The architecture combines active-passive Patroni replication with Etcd and PgBouncer to meet the 99.99% availability and low-latency performance requirements. Strict mTLS, pgaudit, and pgBackRest encryption enforce HIPAA/GDPR compliance and secure long-term data retention.