## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. The architecture enforces strict regional data residency, high availability, and compliance with GDPR and HIPAA mandates.

## Key Elements
* **Cloud SQL for PostgreSQL (Enterprise Plus Edition)**: Regional primary/replica relational database storing patient profiles, FHIR resources, consent logs, and AI audit records.
* **PgBouncer**: Connection pooling sidecar inside GKE pods managing database connections.
* **Memorystore for Redis (Cluster Mode)**: Regional in-memory cache handling session management and WebRTC states.
* **Google Cloud KMS**: Regional key management service for Customer-Managed Encryption Keys (CMEK).
* **Google Cloud Storage (GCS)**: Regional buckets for encrypted automated database backups and Point-in-Time Recovery (PITR) logs.
* **VPC Service Perimeters**: Network security boundary enforcing private IP isolation.

## Relationships
* **Backend Service -> PgBouncer**: PostgreSQL wire protocol over TLS 1.3 with IAM database authentication.
* **PgBouncer -> Cloud SQL (Primary/Read Replica)**: PostgreSQL wire protocol over TLS 1.3 for transactional writes, read-heavy FHIR queries, and audit logs.
* **Backend Service -> Memorystore for Redis**: RESP3 over TLS 1.3 for session and WebRTC state caching.
* **Cloud SQL -> Google Cloud KMS**: Internal gRPC over TLS for regional CMEK key retrieval.
* **Cloud SQL -> Regional GCS Bucket**: HTTPS for encrypted automated backups and PITR log exports.

## Technology Stack
* **Cloud SQL for PostgreSQL**: Selected for robust transactional integrity, FHIR resource storage, and built-in audit triggers.
* **Memorystore for Redis**: Chosen for sub-millisecond latency required by real-time WebRTC sessions and session caching.
* **PgBouncer**: Implemented to prevent connection churn during unstable client reconnections.
* **Google Cloud KMS & GCS**: Utilized for regional encryption compliance (CMEK) and disaster recovery data retention.
* **TLS 1.3 & RESP3**: Enforced for secure, encrypted internal wire communications.

## Rationale
This architecture guarantees strict regional data isolation between `europe-west3` and `us-central1` to comply with GDPR and HIPAA without cross-region replication. Multi-zone high availability, connection pooling, and Redis AOF persistence ensure continuous availability and resilience under unstable rural network conditions.