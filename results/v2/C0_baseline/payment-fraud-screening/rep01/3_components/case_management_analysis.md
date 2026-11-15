## Overview
The Case Management system provides fraud analysts with an ECS Fargate and S3/CloudFront interface to review suspicious payment authorizations. It ensures PCI-DSS compliance and a 7-year tamper-evident audit trail for all human-in-the-loop decisions.

## Key Elements
- Fraud Analyst (Person)
- Case Management Container (ECS Fargate running Node.js)
- Analyst SPA (React hosted in S3 and served via Amazon CloudFront)
- API Router & Auth Component (Express.js)
- Case Workflow Engine with Prioritization Queue (Node.js)
- Audit Logger Component with AWS KMS integration (Node.js)
- Data Layer (Amazon Aurora Serverless v2 PostgreSQL with Amazon RDS Proxy)
- AWS KMS and AWS Secrets Manager

## Relationships
- Fraud Analyst -> Analyst SPA: Reviews suspicious transactions [HTTPS/TLS via CloudFront]
- Analyst SPA -> API Router & Auth Component: Manages cases and submits overrides [HTTPS/REST with OAuth2/OIDC JWT]
- API Router & Auth Component -> Case Workflow Engine: Processes state transitions and prioritizes queues [In-memory function calls]
- Case Workflow Engine -> Audit Logger Component: Triggers audit events for analyst actions [In-memory function calls]
- Audit Logger Component -> AWS KMS: Generates cryptographic signatures for audit records [AWS SDK / IAM]
- Case Management Container -> Amazon RDS Proxy: Reads and writes case and audit data [PostgreSQL Wire Protocol via TLS]
- API Router & Auth Component -> AWS Secrets Manager: Injects secrets at startup [AWS SDK / IAM]

## Technology Stack
- React: Lightweight frontend SPA for rapid analyst workflows
- Node.js & Express.js: Low-overhead backend runtime for a three-engineer team
- Amazon ECS Fargate: Serverless container compute minimizing operational management
- Amazon S3 & CloudFront: Cost-effective static asset hosting staying within budget
- Amazon Aurora Serverless v2 with RDS Proxy: Auto-scaling relational storage with connection pooling
- AWS KMS: Cryptographic signing for tamper-evident 7-year audit logs

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team within a strict 25,000 EUR monthly budget. It strictly isolates sensitive card data via API tokenization while maintaining a tamper-evident audit trail for 7-year compliance.