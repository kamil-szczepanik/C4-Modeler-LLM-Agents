## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient records, scheduling, and billing securely. It ensures high availability, strict regulatory compliance, and sub-second clinical data retrieval.

## Key Elements
- Relational Data Store (PostgreSQL): Handles transactional workloads for patient records, scheduling, and billing.
- Audit Log Engine (WORM Storage): Provides immutable, append-only electronic medical record audit logs using AWS S3 Object Lock and on-premise WORM volumes.
- PgBouncer: Manages database connection pooling to prevent thread exhaustion under high concurrent loads.
- Enterprise IDP: Manages user identities and RBAC mapping for backend services.
- EMR Backend & Billing Service: Microservices communicating with the database tier.

## Relationships
- EMR Backend -> Relational Data Store: Persists and retrieves EMR data and audit logs [Encrypted TCP (AES-256) via mTLS]
- Billing Service -> Relational Data Store: Persists billing data [Encrypted TCP (AES-256) via mTLS]
- EMR Backend -> Audit Log Engine: Streams cryptographic audit events [gRPC]
- Database Tier -> Enterprise IDP: Authenticates access and enforces RBAC [LDAP/OAuth2]

## Technology Stack
- PostgreSQL: Relational database chosen for robust ACID compliance, row-level security, and pgaudit support.
- AWS S3 Object Lock & On-Prem WORM: Selected to meet the 10-year immutable audit retention requirement.
- PgBouncer: Implemented to optimize connection pooling and mitigate thread exhaustion under peak loads.
- Hardware Security Module (HSM): Used for database-level encryption key management with 90-day rotation.

## Rationale
This architecture uses active-active hybrid replication and rigorous data partitioning to sustain 99.99% availability and low-latency EMR retrieval (<1s P95). Strict cryptographic controls, WORM storage, and RBAC ensure full HIPAA and GDPR compliance without impacting operational throughput.