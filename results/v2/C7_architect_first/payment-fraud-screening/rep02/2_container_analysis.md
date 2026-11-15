## Overview
This system provides real-time fraud screening for card-not-present payment authorizations and a case management workflow for fraud analysts. It guarantees high performance, strict regulatory compliance, and auditability on AWS within a fixed budget and small team constraint.

## Key Elements
*   **API Gateway**: AWS API Gateway (REST) handling ingress, JWT validation, and token masking.
*   **Load Balancer**: AWS Network Load Balancer (NLB) with mTLS via AWS Certificate Manager Private CA.
*   **Fraud Scoring Engine**: Go microservice deployed on Amazon ECS on EC2 using compute-optimized instances (c6i).
*   **Case Management Backend**: Node.js/TypeScript service on Amazon ECS Fargate.
*   **Fraud Analyst UI**: React Single Page Application hosted in Amazon S3 and served via Amazon CloudFront.
*   **Data Stores**: Amazon DynamoDB (feature/rule store & hot case data), Amazon Aurora PostgreSQL with ledger tables (tamper-evident 7-year audit logs), and Amazon S3 with Athena.
*   **Identity & Security**: AWS Cognito for authentication, AWS Secrets Manager for secrets, and AWS KMS for encryption.
*   **Observability**: AWS X-Ray and AWS Container Insights.

## Relationships
*   **Payment Gateway / Acquirer** communicates with **AWS API Gateway** via HTTPS (REST, TLS 1.3).
*   **AWS API Gateway** routes traffic to the **Fraud Scoring Engine** via **AWS Network Load Balancer** using mTLS.
*   **Fraud Scoring Engine** queries **Amazon DynamoDB** via AWS SDK using IAM Roles for Tasks.
*   **Fraud Analyst UI** interacts with **Case Management Backend** via HTTPS.
*   **Case Management Backend** reads/writes to **Amazon DynamoDB** and **Aurora PostgreSQL**.
*   **Fraud Scoring Engine** writes tamper-evident decision logs to **Aurora PostgreSQL** and metrics to **AWS X-Ray** / **Container Insights**.

## Technology Stack
*   **Cloud Provider**: AWS (`eu-west-1`), operating within a strict €25k/month budget.
*   **Compute**: Amazon ECS on EC2 (Go Fraud Scoring Engine) for predictable <50ms P99 latency at 3,000 TPS; ECS Fargate for Case Management.
*   **Languages**: Go (scoring engine for performance); Node.js/TypeScript (case management); React (analyst UI).
*   **Security & Compliance**: PCI-DSS Level 1 compliant architecture; AWS Cognito (MFA/OIDC); AWS KMS (customer-managed keys); token masking at API layer (R-05).
*   **Resiliency**: Redis caching and active API Gateway circuit breakers for fail-open capabilities (R-07).

## Rationale
This architecture uses ECS on EC2 for the Go scoring engine to guarantee deterministic sub-50ms P99 latencies at 3,000 TPS while respecting the €25,000 monthly infrastructure budget. Strict network isolation, IAM task roles, and ledger-backed PostgreSQL ensure PCI-DSS Level 1 compliance and tamper-evident 7-year auditability for a three-engineer team.