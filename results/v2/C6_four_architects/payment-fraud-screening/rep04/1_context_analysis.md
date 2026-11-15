## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud, providing sub-millisecond scoring decisions and case management workflows for analysts. It ensures PCI-DSS compliance, strict auditability, and high performance within a constrained budget and team size.

## Key Elements
* **Payment Gateway / Acquirer**: External system sending authorization requests via REST/gRPC over HTTPS.
* **Fraud Analyst**: User reviewing suspicious cases via a Web Browser.
* **Real-Time Payment Fraud Screening System**: Core software system comprising API Gateway/ALB, Scoring Engine, Case Management API, Tokenization Proxy, and Model/Rule Synchronization Worker containers.
* **Card Networks / Tokenization Vault**: External system providing cardholder data and token resolution.
* **Compliance & Audit Archive**: External WORM storage using AWS S3 Object Lock.
* **Identity Provider (IdP)**: External authentication and RBAC provider using OAuth2/OIDC.
* **Notification Service**: External alerting service using AWS SES/SNS.
* **ML Training Platform**: External offline system supplying scoring models.
* **Data & Cache Layer**: Amazon ElastiCache (Redis) and Amazon Aurora Serverless v2.
* **Async Audit Pipeline**: Amazon SQS and AWS Lambda.

## Relationships
* **Payment Gateway** $\rightarrow$ **Fraud Screening System**: Synchronous authorization scoring via HTTPS/gRPC.
* **Fraud Analyst** $\rightarrow$ **Fraud Screening System**: Case management and rule updates via HTTPS.
* **Scoring Engine** $\leftrightarrow$ **Tokenization Proxy**: Token resolution via internal gRPC over VPC.
* **Case Management API** $\rightarrow$ **Tokenization Proxy**: Masked data retrieval via HTTPS.
* **Fraud Screening System** $\rightarrow$ **Compliance & Audit Archive**: Immutable audit record streaming via AWS SDK/TLS.
* **ML Training Platform** $\rightarrow$ **Fraud Screening System**: Model artifact synchronization via HTTPS/S3.

## Technology Stack
* **Cloud Infrastructure**: AWS in region `eu-west-1` for managed services within budget.
* **Compute**: AWS ECS Fargate for stateless microservices and AWS Lambda for asynchronous tasks.
* **Languages**: Rust or Go for the Scoring Engine to eliminate garbage-collection pauses and ensure sub-millisecond execution.
* **Databases & Caching**: Amazon ElastiCache (Redis) for feature stores and model state; Amazon Aurora Serverless v2 for transactional case data.
* **Storage & Messaging**: Amazon S3 Object Lock for 7-year WORM audit compliance; Amazon SQS for decoupled audit event streaming.
* **Identity & Security**: AWS Cognito (OAuth2/OIDC) for IdP and an internal Tokenization Proxy for PCI-DSS scope reduction.

## Rationale
The architecture leverages AWS serverless and managed container services to achieve high throughput and <50ms P99 latency within a fixed €25,000 monthly budget and a three-engineer team. Strict data isolation via a Tokenization Proxy and S3 Object Lock ensures PCI-DSS compliance and 7-year tamper-evident auditability.