## Overview
The Case Management API Container powers fraud analyst reviews and investigations for real-time payment fraud screening. It provides secure, auditable case workflows while enforcing strict data masking to ensure PCI-DSS Level 1 compliance.

## Key Elements
- Fraud Analysts & Risk Managers (Users)
- Fraud Analyst SPA (Single Page Application)
- Case Management API Container (Node.js/TypeScript)
- Case Controller Component
- Data Masking Middleware Component
- Audit & Event Publisher Component
- Case Repository Component
- Batch Action & Workflow Engine Component
- Amazon SQS (Audit Queue)
- AWS QLDB
- AWS KMS & AWS Secrets Manager

## Relationships
- Fraud Analyst SPA -> Case Controller Component: REST/JSON over HTTPS via TLS 1.3
- Case Controller Component -> Data Masking Middleware Component: Middleware intercept
- Case Controller Component -> Batch Action & Workflow Engine Component: In-memory event emission
- Case Repository Component -> AWS QLDB: AWS SDK over TLS
- Audit & Event Publisher Component -> Amazon SQS (Audit Queue): AWS SDK over TLS
- Case Management API Container -> AWS KMS & AWS Secrets Manager: AWS IAM / TLS

## Technology Stack
- Node.js with TypeScript: Rapid development and strong typing maintained by a 3-engineer team.
- Express/Fastify: Lightweight web framework for handling REST endpoints.
- AWS ECS Fargate: Cost-effective, serverless container orchestration within the €25,000 monthly budget.
- AWS QLDB: Tamper-evident ledger storage ensuring 7-year auditability for regulatory compliance.
- Amazon SQS: Asynchronous messaging for cryptographically signed audit trails and batch workflows.
- AWS Secrets Manager & AWS KMS: Secure, ephemeral secrets loading and data encryption.

## Rationale
This architecture balances strict PCI-DSS Level 1 security and 7-year auditability with the operational constraints of a three-engineer team and a fixed budget. Utilizing serverless AWS infrastructure and modular Node.js components ensures high availability, strict data masking, and scalable case management without excessive operational overhead.