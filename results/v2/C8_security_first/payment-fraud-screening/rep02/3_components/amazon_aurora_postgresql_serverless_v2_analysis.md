## Overview
Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for a mid-size payment processor and manages fraud reviews. It ensures high-throughput, low-latency decisioning while meeting PCI-DSS Level 1 compliance and a 7-year auditability mandate.

## Key Elements
- Fraud Analyst & Risk Manager
- Payment Gateway / Acquirer, Payment Network / Card Brands (Visa/Mastercard), Core Ledger / Compliance Archive
- AWS API Gateway (Ingress/TLS Termination)
- Go Scoring Engine (Go (Golang), AWS ECS on Fargate)
- Node.js Case Management (Node.js (TypeScript), AWS ECS on Fargate)
- Amazon SQS / EventBridge
- Amazon Aurora PostgreSQL Serverless v2 (Case state database)
- AWS QLDB
- AWS Cognito & AWS Secrets Manager

## Relationships
- AWS API Gateway -> Go Scoring Engine: Forwards authorization requests [HTTPS/REST]
- Go Scoring Engine -> Amazon SQS / EventBridge: Publishes suspicious transaction events [AMQP/EventBridge Protocol]
- Amazon SQS / EventBridge -> Node.js Case Management: Triggers case creation for analyst review [SQS Polling / Event Delivery]
- Node.js Case Management -> Amazon Aurora PostgreSQL Serverless v2: Reads and writes case state [PostgreSQL wire protocol over TLS 1.3 with IAM Auth]
- Node.js Case Management -> AWS QLDB: Stores immutable long-term audit logs [AWS SDK / HTTPS]

## Technology Stack
- AWS (eu-west-1): Target cloud provider ensuring managed scalability and compliance tooling.
- Go (Golang) on AWS ECS on Fargate: High-performance runtime for sub-50ms P99 scoring latency.
- Node.js (TypeScript) on AWS ECS on Fargate: Efficient case management backend for analyst workflows.
- Amazon Aurora PostgreSQL Serverless v2: Scalable relational storage with RLS for case state within cost constraints.
- AWS QLDB: Tamper-evident ledger ensuring tamper-resistant 7-year auditability (R-06).

## Rationale
This architecture uses serverless containers and auto-scaling databases to handle 3,000 TPS within a 25,000 EUR monthly budget. It strictly isolates sensitive card data via encryption and IAM policies to guarantee PCI-DSS Level 1 compliance and a 7-year audit trail for a 3-engineer team.