## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients on GCP. It strictly enforces regional data residency and compliance using isolated regional databases.

## Key Elements
- Regional Relational Database (Google Cloud SQL PostgreSQL)
- Regional Relational Database Read Replica
- Connection Pooling (PgBouncer)
- Key Management Service (Cloud KMS)
- Monitoring & Operations Suite (Cloud Operations Suite)

## Relationships
- Regional Relational Database -> Cloud KMS: Encrypts data at rest using region-specific keys [gRPC / Cloud IAM]
- API Gateway / BFF -> Regional Relational Database: Queries transactional and consent data via connection pool [TLS]
- Regional Relational Database -> Regional Relational Database Read Replica: Replicates data asynchronously for read-scale [Internal PostgreSQL Replication]

## Technology Stack
- Google Cloud SQL PostgreSQL: Selected for robust transactional integrity and regional isolation
- Cloud KMS: Implements Customer-Managed Encryption Keys (CMEK) for regional cryptographic control
- PgBouncer: Manages connection spikes and prevents thread exhaustion
- pgAudit: Generates immutable access and transaction logs for compliance

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by isolating EU and US data regionally. It delivers high availability and low latency required for rural and cross-border telemedicine workflows.