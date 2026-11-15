## Overview
[The Amazon Aurora Serverless v2 component securely persists case data, audit trails, and review decisions for the real-time payment fraud screening system.]
[It provides scalable, compliant relational storage while enforcing strict PCI-DSS boundaries and a 7-year audit retention policy.]

## Key Elements
- Case Data Schema (PostgreSQL-compatible relational engine)
- Audit Log Table (Append-only, tamper-evident storage using row-level security and `pgaudit` extension)
- Amazon RDS Proxy Layer (Connection pooling and multiplexing)
- AWS Secrets Manager (Credential and secret management)

## Relationships
- AWS Lambda -> Amazon RDS Proxy: Ingests streaming audit records [SQL/TLS over TCP]
- Case Management Backend -> Amazon RDS Proxy: Queries and mutates case data and audit logs [SQL/TLS over TCP]
- Amazon RDS Proxy -> Case Data Schema: Manages multiplexed database connections [TCP]
- Amazon Aurora Serverless v2 -> Amazon S3: Ships immutable audit logs with Object Lock enabled [HTTPS]

## Technology Stack
- Amazon Aurora Serverless v2 (PostgreSQL 15+ engine): Chosen for sub-second ACU autoscaling to handle traffic spikes within budget constraints.
- Amazon RDS Proxy: Chosen to pool and multiplex incoming SQL connections, preventing serverless scaling exhaustion.
- AWS KMS: Chosen for Customer Managed Key encryption at rest with annual rotation.
- PostgreSQL `pgaudit` extension: Chosen to log all DDL, DCL, and role-based access for regulatory compliance.

## Rationale
[This architecture fits the requirements by utilizing serverless auto-scaling and connection pooling to maintain sub-50ms performance and fit within the 25,000 EUR monthly budget.]
[It guarantees strict PCI-DSS compliance and 7-year tamper-evident auditability using IAM authentication, Row-Level Security, and S3 Object Lock.]