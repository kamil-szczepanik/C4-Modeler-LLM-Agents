## Overview
The Case Management Container empowers fraud analysts to review suspicious transactions and audit scoring decisions securely. It enforces PCI-DSS Level 1 compliance while supporting low-latency analyst workflows.

## Key Elements
- Fraud Analyst (Person)
- Case Management Container (AWS ECS Fargate Container)
- Amazon Aurora Serverless (Database Container)
- Amazon SQS (Message Queue Container)
- Amazon QLDB / S3 Object Lock (Immutable Ledger System)
- AWS Secrets Manager (Security Service)

## Relationships
- Fraud Analyst -> Case Management Container: Accesses review cases and audit trails [HTTPS with OIDC/OAuth2 MFA]
- Case Management Container -> Amazon Aurora Serverless: Reads and writes review cases and read-optimized audit projections [Database Protocol]
- Case Management Container -> Amazon SQS: Routes failed audit logs or feedback events to a Dead-Letter Queue [AWS SDK / SQS Protocol]
- Case Management Container -> Amazon QLDB / S3 Object Lock: Writes cryptographically signed analyst actions and overrides [AWS SDK / HTTPS]
- Case Management Container -> AWS Secrets Manager: Fetches database credentials and OIDC secrets [AWS SDK / HTTPS]

## Technology Stack
- AWS ECS Fargate: Hosts containerized application with service auto-scaling for cost control within budget.
- Amazon Aurora Serverless: Stores review cases and event-driven projections for query performance.
- Amazon SQS: Handles asynchronous dead-letter queues to prevent data loss during outages.
- AWS Secrets Manager: Secures credentials and secrets with automated rotation.
- OIDC/OAuth2: Authenticates analysts and enforces strict Role-Based Access Control (RBAC).

## Rationale
This architecture ensures robust security and strict compliance (PCI-DSS Level 1, 7-year auditability) without compromising performance or exceeding the fixed monthly budget. Asynchronous processing and read-optimized projections protect core ledgers while maximizing analyst efficiency.