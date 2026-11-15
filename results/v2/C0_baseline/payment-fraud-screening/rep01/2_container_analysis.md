## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and provides case management for analysts to review suspicious transactions. It ensures strict PCI-DSS Level 1 compliance and sub-50ms P99 latency within a fixed budget and small engineering team.

## Key Elements
- **Users:** Fraud Analyst, Merchant / Payment Gateway, Compliance & Risk Officer
- **External Systems:** AWS KMS, AWS S3 Object Lock, Identity Provider (IdP)
- **Containers:** API Gateway (AWS API Gateway), Scoring Engine (AWS Lambda with Provisioned Concurrency, Go runtime), Case Management (Node.js/React on ECS Fargate), Data Layer (Amazon Aurora Serverless v2 PostgreSQL), Async Messaging (AWS SQS), Observability (AWS X-Ray)

## Relationships
- Merchant / Payment Gateway calls API Gateway via HTTPS/TLS for real-time payment authorization
- API Gateway communicates with Scoring Engine via gRPC using mTLS
- Scoring Engine asynchronously enqueues audit logs to AWS SQS
- Case Management connects to Aurora PostgreSQL for case review data
- Scoring Engine and Case Management retrieve secrets via AWS Secrets Manager and AWS KMS

## Technology Stack
- **Compute:** AWS Lambda with Provisioned Concurrency for Go-based stateless scoring; ECS Fargate for Node.js case management
- **Database & Storage:** Amazon Aurora Serverless v2 PostgreSQL for transactional and audit data; S3 Object Lock for 7-year tamper-evident audit logs
- **Messaging:** AWS SQS for decoupled asynchronous audit event streaming
- **Security & Networking:** AWS API Gateway for edge tokenization via AWS KMS; AWS Secrets Manager for dynamic secret injection; IdP with OAuth2/OIDC for RBAC
- **Observability:** AWS X-Ray for distributed tracing and latency monitoring

## Rationale
This architecture uses serverless and fully managed AWS services to eliminate operational toil, fitting the constraints of a 3-person team and a €25k/month budget. Strict isolation of tokenized data at the edge and Lambda provisioned concurrency ensure PCI-DSS Level 1 compliance and a sub-50ms P99 latency SLA.