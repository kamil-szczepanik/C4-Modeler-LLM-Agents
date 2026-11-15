## Overview
The Clinic Management System is a hybrid clinical IT platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures 99.99% availability, strict HIPAA/GDPR compliance, and robust data retention of 10 years or more.

## Key Elements
- Primary Write Database [component]: PostgreSQL multi-node synchronous replication cluster
- Read-Only Replica Cluster [component]: Asynchronously replicated read-nodes for analytics
- Audit Log Store [component]: Append-only, tamper-evident storage subsystem with WORM compliance
- Database Connection Pooler [component]: PgBouncer instances for connection management
- Clinical Core Service [container]: Java / Spring Boot backend service
- Administrative & Analytics Service [container]: Python / FastAPI + Celery reporting service
- Identity Provider (IdP) [externalSystem]: OpenID Connect (OIDC) / OAuth2 authentication

## Relationships
- Clinical Core Service -> Database Connection Pooler [PostgreSQL wire protocol over mTLS]
- Database Connection Pooler -> Primary Write Database [PostgreSQL wire protocol over mTLS]
- Administrative & Analytics Service -> Read-Only Replica Cluster [PostgreSQL wire protocol over mTLS]
- Clinical Core Service -> Audit Log Store [Encrypted append-only stream over mTLS]

## Technology Stack
- PostgreSQL: Core relational database technology chosen for robust ACID compliance and clustering support
- PgBouncer: Connection pooling technology selected to mitigate thread exhaustion and handle high concurrent clinician traffic
- HashiCorp Vault: Secret management technology used for dynamic database credential rotation
- S3-compatible WORM Storage: Cold-tier archival technology utilized to enforce the $\ge$ 10-year retention mandate

## Rationale
This architecture ensures high availability through active-active hybrid patterns and read-replica offloading, protecting <1s EMR load performance. Security and compliance are rigorously maintained via mTLS, AES-256 encryption, role-based access control, and tamper-evident audit logging.