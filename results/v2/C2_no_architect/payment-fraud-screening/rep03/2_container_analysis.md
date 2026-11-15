## Overview
[The system provides real-time fraud screening for card-not-present payment authorizations, enabling rapid transaction scoring and analyst case reviews. It ensures high performance and strict regulatory compliance within a fixed budget.]

## Key Elements
- **Actors**: Cardholders, Fraud Analysts, Risk Managers / Data Scientists, Compliance & Audit Officers, Payment Gateway / Processing Engine
- **AWS Infrastructure**: AWS VPC (Private Subnets), Amazon API Gateway, Application Load Balancer (ALB)
- **Containers / Compute**: Scoring Engine (AWS ECS Fargate), Case Management UI & Backend (AWS ECS Fargate), AWS Lambda
- **Storage & Databases**: Amazon S3 (Model Artifacts and WORM Audit Logs with Object Lock), AWS QLDB
- **Management & Security**: AWS IAM, AWS Secrets Manager, AWS KMS (Customer-Managed Keys), AWS CodePipeline, AWS CloudWatch & X-Ray, AWS CloudWatch Synthetics

## Relationships
- **Payment Gateway to API Gateway**: Forwards payment authorization requests via HTTPS/TLS 1.3.
- **API Gateway to ALB**: Routes traffic over mTLS within private subnets to internal containers.
- **Scoring Engine to S3**: Downloads cryptographically verified ML model artifacts over TLS 1.3.
- **Scoring Engine to S3 / QLDB**: Persists tamper-evident decision logs, feature weights, and inputs using AWS KMS encryption.
- **Fraud Analysts to Case Management UI**: Interacts via HTTPS (OIDC/MFA authenticated) with tokenized, masked PAN data.
- **AWS CodePipeline to ECS Fargate**: Deploys zero-downtime model updates and container rollouts.

## Technology Stack
- **Compute & Orchestration**: AWS ECS Fargate, AWS Lambda for serverless tasks, ensuring zero custom orchestrator overhead for a 3-person team.
- **Data & Storage**: Amazon S3 with Object Lock (WORM compliance) and Glacier lifecycle policies, AWS QLDB for immutable audit trails.
- **Security & Compliance**: AWS IAM, AWS Secrets Manager, AWS KMS (CMK) for encryption at rest, TLS 1.3 for data in transit.
- **Observability & CI/CD**: AWS CloudWatch, AWS X-Ray, AWS CloudWatch Synthetics, AWS CodePipeline.

## Rationale
[Leveraging AWS managed services ensures the 3-person team can operate the system efficiently within the 25,000 EUR monthly budget. Strict VPC isolation, cryptographic verification, and tamper-evident storage meet PCI-DSS Level 1 and 7-year audit requirements without sacrificing sub-50ms P99 latency.]