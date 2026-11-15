## Overview
The Amazon RDS PostgreSQL component serves as the secure, durable relational data store for case management data in the Real-Time Payment Fraud Screening system. It provides structured storage for analyst reviews and investigation notes while strictly complying with PCI-DSS Level 1 mandates.

## Key Elements
- **Case Management Schema**: Relational tables storing analyst reviews, investigation notes, and case statuses.
- **pgBouncer Connection Pooler**: Manages database connections from ephemeral ECS Fargate tasks.
- **pgaudit Extension**: Logs all DDL, DCL, and privileged DML statements for compliance.

## Relationships
- **Case Management App -> Case Management Schema**: Reads and writes case data via TCP/SSL (Port 5432) using `pgBouncer`.
- **Amazon RDS PostgreSQL -> AWS Backup**: Performs automated snapshots and WAL archiving via AWS API for 7-year retention.

## Technology Stack
- **PostgreSQL 15 Engine**: Relational database core selected for robust ACID guarantees and schema management.
- **AWS Secrets Manager & IAM Database Authentication**: Manages credentials securely without hardcoded passwords.
- **AWS KMS (AES-256):** Encrypts data at rest using customer-managed keys.

## Rationale
This architecture offloads high-throughput logging to S3, protecting relational integrity for low-frequency case management. It aligns with team capacity and budget by leveraging fully managed AWS services for high availability and compliance.