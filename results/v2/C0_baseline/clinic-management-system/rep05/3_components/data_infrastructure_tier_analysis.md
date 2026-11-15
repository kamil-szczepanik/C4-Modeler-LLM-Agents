## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, EMRs, scheduling, and billing for healthcare facilities. It provides secure, highly available clinical IT capabilities while maintaining strict regulatory compliance.

## Key Elements
- PostgreSQL with Citus
- Redis Enterprise
- Apache Kafka
- Istio & ArgoCD
- Backup & PITR Manager
- Centralized Vault
- Encrypted Object Storage (S3/MinIO)

## Relationships
- Core Services -> PostgreSQL with Citus: Persists operational data via JDBC/TCP with TLS 1.3 and native Row-Level Security (RLS)
- Core Services -> Redis Enterprise: Caches data and checks schedules via RESP with TLS 1.3
- Core Services -> Apache Kafka: Publishes asynchronous messages using TCP with payload-level encryption
- Istio & ArgoCD -> Hybrid Kubernetes Clusters: Manages mTLS service-to-service encryption and declarative deployments
- Backup & PITR Manager -> Encrypted Object Storage (S3/MinIO): Performs WAL archiving and snapshots via HTTPS/TLS 1.3 with WORM locks
- Centralized Vault -> Data & Infrastructure Tier: Provides automated credentials, envelope encryption keys (AES-256), and ephemeral access tokens

## Technology Stack
- PostgreSQL with Citus: Sharded relational storage chosen for horizontal scalability and AES-256 at-rest encryption
- Redis Enterprise: Distributed active-active cache selected to guarantee sub-second EMR screen loads
- Apache Kafka: Event broker utilized for reliable, decoupled asynchronous messaging and integration
- Istio & ArgoCD: Service mesh and GitOps tooling chosen for mTLS and declarative hybrid cluster management
- Velero/Barman & S3/MinIO: Backup and object storage stack selected to fulfill 10-year retention and PITR mandates

## Rationale
This architecture utilizes a distributed, encrypted data tier with automated backup and multi-zone caching to satisfy HIPAA, GDPR, and 99.99% availability requirements. It decouples high-performance clinical operations from long-term storage while ensuring rapid disaster recovery capabilities.