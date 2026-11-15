## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to prevent fraud while enabling analysts to review suspicious transactions. It maintains strict compliance, low-latency processing, and high availability within a fixed budget.

## Key Elements
- Payment Gateway / Acquirer Systems
- Fraud Analysts
- Amazon Application Load Balancer (ALB)
- Fraud Scoring Engine (ECS Fargate)
- Case Management Service (ECS Fargate)
- Amazon DynamoDB and Amazon Aurora Serverless v2
- AWS WAF and AWS Certificate Manager (ACM)

## Relationships
- Payment Gateway / Acquirer Systems -> Amazon Application Load Balancer (ALB): Submits payment authorization requests [HTTPS (REST/JSON)]
- Fraud Analysts -> Amazon Application Load Balancer (ALB): Reviews cases and updates rules [HTTPS]
- Amazon Application Load Balancer (ALB) -> Fraud Scoring Engine: Routes scoring requests [gRPC over mTLS]
- Amazon Application Load Balancer (ALB) -> Case Management Service: Routes case management requests [gRPC over mTLS]

## Technology Stack
- AWS Application Load Balancer (ALB): Selected for low-latency network overhead and native gRPC routing support.
- ECS Fargate: Provides serverless container orchestration to minimize operational overhead for a three-engineer team.
- AWS WAF: Deployed at the edge for rate-limiting, DDoS mitigation, and OWASP Top 10 protection.
- AWS Certificate Manager (ACM): Manages TLS 1.3 certificates for secure perimeter encryption.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational complexity for a small engineering team while meeting strict latency and PCI-DSS compliance constraints. Targeted edge security and optimized gRPC routing ensure high throughput and rapid failover under heavy transaction loads.