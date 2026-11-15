## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages suspicious transaction reviews. It ensures PCI-DSS compliance, sub-50ms P99 latency, and 7-year auditable decision storage within fixed budget constraints.

## Key Elements
- **Payment Gateway / Core Processing Platform**: External system initiating authorization requests.
- **Fraud Analyst**: External user managing payment reviews.
- **Identity Provider (IdP)**: External system for session authentication.
- **AWS Key Management Service (KMS) / HSM**: External system for cryptographic services.
- **API Gateway / Application Load Balancer**: AWS ALB with TLS Termination Engine and Listener Rules.
- **Fraud Scoring Engine**: Go or Rust service hosted on AWS ECS Fargate.
- **Case Management Service**: Node.js / TypeScript service hosted on AWS ECS Fargate.
- **Amazon ElastiCache Redis**: In-memory data store for real-time state.
- **Amazon Aurora PostgreSQL**: Relational database for case management.
- **Amazon S3 Immutable Vault**: Tamper-evident storage with Object Lock in Compliance Mode.
- **Amazon SQS / SNS**: Messaging and notification service.

## Relationships
- **Payment Gateway / Core Processing Platform -> API Gateway / Application Load Balancer**: Invokes payment authorization requests [HTTPS using TLS 1.3]
- **Fraud Analyst -> API Gateway / Application Load Balancer**: Sends management and review commands [HTTPS / REST, JSON]
- **Identity Provider (IdP) -> API Gateway / Application Load Balancer**: Validates JWT bearer tokens [HTTPS]
- **API Gateway / Application Load Balancer -> Fraud Scoring Engine**: Calls fraud scoring logic [gRPC over HTTP/2]
- **API Gateway / Application Load Balancer -> Case Management Service**: Routes analyst UI and API traffic [HTTPS / REST, JSON]

## Technology Stack
- **AWS ALB**: Replaces API Gateway to avoid latency jitter and meet R-04 performance constraints.
- **Go or Rust**: Selected for the Fraud Scoring Engine to guarantee sub-50ms execution times.
- **AWS ECS Fargate**: Container orchestration fitting the 3-engineer operational model without Kubernetes overhead.
- **Amazon S3 Object Lock**: Enforces tamper-evident 7-year auditability for R-06 compliance.

## Rationale
This architecture uses AWS ALB and ECS Fargate to meet the sub-50ms latency requirement at 3,000 TPS within a 25,000 EUR monthly budget. It leverages managed AWS services to maintain PCI-DSS compliance and ensure auditability with a lean three-engineer team.