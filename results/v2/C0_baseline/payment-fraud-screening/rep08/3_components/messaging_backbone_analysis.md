## Overview
This system provides real-time fraud screening for card-not-present payment authorizations within a strict budgetary and compliance framework. It processes authorization requests, manages fraud analyst reviews, and maintains an auditable decision trail.

## Key Elements
- Fraud Analysts & Risk Managers
- Payment Gateway / Merchants
- API Gateway & Routing Layer (AWS API Gateway / ALB)
- Scoring Engine Container (Go / Rust on AWS Fargate Spot)
- Case Management Container (Node.js / React SPA backend with Amazon RDS PostgreSQL)
- Messaging Backbone (Amazon SQS / SNS with VPC Endpoints)
- Audit & Event Store Container (Amazon DynamoDB & S3)
- Model Storage & Management (Amazon S3 & AWS Secrets Manager)

## Relationships
- Payment Gateway -> API Gateway & Routing Layer: Forwards authorization requests [HTTPS / TLS 1.3]
- API Gateway & Routing Layer -> Scoring Engine Container: Routes authorization payloads [gRPC / HTTPS]
- Scoring Engine Container -> SNS Audit Topic: Publishes audit events asynchronously [HTTPS (SNS)]
- Scoring Engine Container -> SQS Review Queue: Routes suspicious payments for review [HTTPS (SQS)]
- Case Management Container -> SQS Review Queue: Consumes and processes review cases [HTTPS (SQS)]

## Technology Stack
- AWS Fargate Spot: Low-cost container orchestration fitting the €25,000 monthly budget
- Amazon SQS & SNS: Serverless messaging backbone with DLQs and VPC Endpoints for minimal operational overhead
- Amazon DynamoDB & S3: Tamper-evident storage ensuring 7-year auditability
- AWS KMS: Customer-managed keys for encryption at rest and payload security

## Rationale
This serverless-first architecture on AWS minimizes infrastructure management, allowing a three-engineer team to maintain operations within budget. It satisfies PCI-DSS Level 1 compliance, enforces strict 7-year auditability, and delivers high-performance fraud screening under 50 ms latency.