## Overview
[The Case Management Backend manages analyst reviews and case workflows for flagged payment transactions using AWS ECS Fargate and Go. It ensures PCI-DSS compliance and 7-year auditability while operating within a strict €25k monthly budget.]

## Key Elements
- Case API Controller (AWS ECS Fargate, Go `net/http`)
- Workflow & Assignment Service (Go business logic, AWS Cognito JWT/RBAC)
- Masking Middleware (Go sanitization component)
- Audit Logging Adapter (Go, crypto/SHA-256, AWS KMS)
- Persistence Repository (Go `database/sql`, `pgx`)
- Amazon Aurora Serverless v2 (Relational database)
- Amazon S3 Object Lock (Immutable compliance storage)
- AWS Secrets Manager (Secure credential injection)

## Relationships
- Case Analyst -> AWS API Gateway: Submits HTTPS requests [HTTPS / TLS 1.3]
- Case API Controller -> Masking Middleware: Delegates serialization and sanitization [In-memory]
- Masking Middleware -> Case Analyst: Returns sanitized payloads [HTTPS]
- Case API Controller -> Workflow & Assignment Service: Invokes business logic [In-memory]
- Workflow & Assignment Service -> Audit Logging Adapter: Dispatches audit events [In-memory]
- Audit Logging Adapter -> Amazon S3 (Object Lock): Streams cryptographically signed audit bundles [TLS / AWS SDK]
- Workflow & Assignment Service -> Amazon Aurora Serverless v2: Persists case state [TLS / PostgreSQL protocol]
- Case Management Backend -> AWS Secrets Manager: Fetches secrets at startup [HTTPS / AWS SDK via IAM Task Role]

## Technology Stack
- Go: Chosen for high performance and minimal resource overhead, fitting a three-person team.
- AWS ECS Fargate: Selected for serverless container orchestration without infrastructure management overhead.
- Amazon S3 Object Lock (Compliance Mode): Utilized for tamper-evident 7-year audit retention meeting R-06.
- AWS KMS: Provides cryptographic non-repudiation and signing for audit logs.
- AWS Secrets Manager: Eliminates plaintext configuration for database credentials and keys.
- Terraform: Enforces Infrastructure-as-Code and GitOps to prevent security drift.

## Rationale
[This architecture strictly bounds PCI-DSS scope by isolating card data and applying automated masking middleware before analyst interaction. It guarantees 7-year tamper-evident auditability via S3 Object Lock and AWS KMS while remaining lean enough for a three-person engineering team.]