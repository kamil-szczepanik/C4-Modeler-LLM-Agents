## Overview
[The Online Bookstore is an e-commerce platform designed for buying physical and electronic books with integrated recommendations and reviews.]
[The system utilizes AWS-hosted microservices with asynchronous messaging to ensure scalable, fault-tolerant checkout and inventory processing.]

## Key Elements
- Site Administrator
- Book Buyer
- Global CDN & AWS WAF (AWS CloudFront / AWS WAF)
- Application Load Balancer (AWS ALB)
- Checkout Container, Shopping Cart Container, Search Container, Recommendations Container (Amazon ECS on AWS Fargate)
- Amazon Cognito (OIDC / OAuth 2.0)
- Amazon SQS/SNS with Dead-Letter Queues (Amazon SQS / SNS)
- AWS Secrets Manager & AWS KMS (AWS Secrets Manager / AWS KMS)

## Relationships
- Book Buyer -> Global CDN & AWS WAF: Browses catalogue and executes secure checkout via HTTPS
- Global CDN & AWS WAF -> Application Load Balancer (ALB): Routes validated web traffic via HTTPS
- Application Load Balancer (ALB) -> ECS Containers: Distributes internal microservice traffic via HTTP/REST
- Shopping Cart Container -> Amazon SQS/SNS with DLQs: Publishes asynchronous checkout events using TLS 1.3 and Encrypted AWS KMS channels
- Site Administrator -> Amazon SQS/SNS with DLQs: Audits failed transactions and manages DLQ redrives via AWS Console/CLI

## Technology Stack
- Cloud Infrastructure: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for regional data residency compliance (GDPR/CCPA)
- Compute: Amazon ECS on AWS Fargate for containerized microservices scaling to 1M MAU
- Messaging: Amazon SQS and SNS with Dead-Letter Queues (14-day retention) for decoupled, fault-tolerant event processing
- Security: AWS KMS Customer Managed Keys (CMK) for PII encryption at rest, TLS 1.3 for data in transit, and Amazon Cognito for OIDC/OAuth 2.0 authentication
- Observability: Amazon CloudWatch Alarms integrated with PagerDuty/Slack for automated DLQ monitoring

## Rationale
[This multi-region AWS architecture ensures 99.95% availability and sub-2-second page loads by decoupling critical checkout workflows with SQS/SNS and DLQs.]
[It strictly enforces GDPR/CCPA compliance and OWASP top-10 security mitigations using regional KMS encryption, least-privilege IAM, and automated redrive playbooks.]