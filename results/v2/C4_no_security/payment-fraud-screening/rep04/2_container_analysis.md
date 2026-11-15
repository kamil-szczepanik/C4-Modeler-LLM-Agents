## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and provides a case management workspace for analysts. It ensures sub-50ms decision latency at 3,000 TPS while maintaining strict PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
- **Users**: Fraud Analyst, Risk Manager
- **External Systems**: Payment Gateway / Acquirer & Merchant Platforms, Identity Provider (IdP), Regulatory & Notification Sink
- **API Gateway**: AWS API Gateway / ALB for ingress routing, tokenization enforcement, and circuit breaking
- **Scoring Engine Container**: Go/Rust-based stateless service on Amazon ECS for sub-50ms transaction evaluation
- **Case Management Container**: Node.js/Python monolith on Amazon ECS for analyst review workflows and data-masked UI
- **Data Layer**: Amazon DynamoDB for feature stores, tamper-evident audit logs, and read replicas; Amazon ElastiCache (Redis) for in-memory model/rule caching
- **Event & Compliance Infrastructure**: AWS SQS/SNS, AWS CloudTrail, and AWS Backup locked vaults

## Relationships
- **Payment Gateway to AWS API Gateway**: Forwards payment authorization requests via HTTPS/REST at 3,000 TPS.
- **API Gateway to Scoring Engine Container**: Invokes real-time fraud scoring via gRPC/REST.
- **Scoring Engine Container to Amazon ElastiCache (Redis)**: Fetches cached fraud rules and scoring models in memory.
- **Scoring Engine & Case Management Containers to Amazon DynamoDB**: Reads/writes transaction data, features, and immutable audit logs.
- **Fraud Analyst to Case Management Container**: Reviews suspicious payments via HTTPS with strict RBAC and card data masking.
- **AWS Infrastructure to Regulatory & Notification Sink**: Exports tamper-evident audit logs via asynchronous AWS SQS/SNS events.

## Technology Stack
- **Cloud Provider**: AWS (`eu-west-1` region) chosen for compliance and infrastructure maturity.
- **Compute**: Amazon ECS on EC2 with provisioned instances to prevent Fargate cold-start latency and enforce budget controls.
- **Databases**: Amazon DynamoDB for low-latency feature stores and immutable audit storage; Amazon ElastiCache (Redis) for zero-downtime rule updates.
- **Deployment & Observability**: AWS CodeDeploy for blue/green deployments; AWS X-Ray for distributed tracing; AWS CloudTrail and AWS Backup locked vaults for audit retention.

## Rationale
This architecture separates the ultra-low latency scoring engine from the analyst case management workspace, isolating failure domains to guarantee P99 latency under 50ms at 3,000 TPS. Utilizing ECS on EC2, DynamoDB read replicas, and strict tokenization at the API Gateway minimizes PCI-DSS scope, ensures 7-year auditability, and stays within the €25k monthly budget for a three-engineer team.