## Overview
The Audit & Event Store is a secure, cost-effective component of the Real-Time Payment Fraud Screening Platform designed to maintain tamper-evident audit logs and transaction data for 7 years. It ensures compliance with PCI-DSS Level 1 while adhering to strict infrastructure budget and small-team constraints.

## Key Elements
- Event Ingestion Service (Go, AWS ECS Fargate): Receives audit events via gRPC/mTLS and validates schemas.
- Relational Ledger Store (AWS Aurora PostgreSQL): Stores hot audit data with `pg_audit` enabled for 90 days.
- Archival Worker (AWS Lambda, Python): Periodically archives historical data to long-term storage.
- S3 Glacier Object Lock Bucket (AWS S3): Provides WORM (Write-Once-Read-Many) storage for 7-year regulatory retention.
- Network Load Balancer (AWS NLB): Routes high-throughput internal traffic to ingestion tasks.
- AWS Secrets Manager / IAM: Manages dynamic credentials and database authentication.

## Relationships
- Fraud Scoring API -> Event Ingestion Service [gRPC/mTLS]
- Case Management Backend -> Event Ingestion Service [gRPC/mTLS]
- Event Ingestion Service -> Relational Ledger Store [SQL/TLS]
- Archival Worker -> Relational Ledger Store [SQL/TLS]
- Archival Worker -> S3 Glacier Object Lock [HTTPS/TLS]

## Technology Stack
- Go: Chosen for high-throughput, low-latency event ingestion processing.
- Python: Utilized for lightweight serverless archival batch tasks.
- AWS Aurora PostgreSQL: Provides scalable relational storage with native audit logging (`pg_audit`).
- AWS S3 Object Lock: Enforces tamper-evident, cost-effective long-term data compliance.
- AWS ECS Fargate & NLB: Enables auto-scaling container execution without managing underlying servers.

## Rationale
This architecture uses managed AWS services like S3 Object Lock and Aurora PostgreSQL to minimize maintenance overhead for a three-engineer team. Tiered storage controls costs to stay within the €25,000 monthly budget while meeting stringent PCI-DSS Level 1 and 7-year auditability mandates.