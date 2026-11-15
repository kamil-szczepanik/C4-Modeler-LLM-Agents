## Overview
[The system is a real-time payment fraud screening platform that screens card-not-present transactions and manages fraud analyst review cases. Its core purpose is to prevent fraud while maintaining sub-50ms latency, 7-year auditability, and PCI-DSS Level 1 compliance.]

## Key Elements
- Fraud Analyst
- External Payment Gateway
- GitHub Actions
- API Gateway / Ingress Container (AWS ECS Fargate)
- Scoring Engine Container (AWS ECS Fargate)
- Case Management Container (AWS ECS Fargate)
- AWS SageMaker Serverless Inference (AWS SageMaker)
- Amazon Aurora Serverless (Amazon Aurora)
- QLDB / S3 Object Lock (Amazon QLDB / Amazon S3)

## Relationships
- Case Management Container -> Amazon Aurora Serverless: Reads and writes review cases [Database Protocol with TLS 1.2+]
- Case Management Container -> Amazon S3: Archives cold case records older than 12 months [HTTPS / AWS SDK]
- Aurora Serverless -> Amazon CloudWatch: Streams advanced audit logs [CloudWatch Agent / KMS]

## Technology Stack
- AWS ECS Fargate: Container orchestration for microservices, chosen for low operational overhead.
- Amazon Aurora Serverless (v2): Relational database for case management, configured with auto-pause disabled and 0.5–8 ACUs.
- AWS IAM Database Authentication: Eliminates static credentials to meet PCI-DSS Level 1 security constraints.
- Terraform / CloudFormation: Infrastructure as Code for repeatable, auditable deployments.
- AWS KMS: Customer-managed keys for database storage and log encryption.

## Rationale
[This architecture balances stringent PCI-DSS Level 1 security and 7-year auditability requirements with the resource limitations of a 3-engineer team. By leveraging fully managed AWS services like Aurora Serverless, Fargate, and SageMaker, the system achieves high availability and sub-50ms latency within a 25,000 EUR monthly budget.]