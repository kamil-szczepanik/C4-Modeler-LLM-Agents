## Overview
This system provides real-time payment fraud screening for card-not-present transactions, evaluating authorizations and routing suspicious cases to analysts. It ensures PCI-DSS Level 1 compliance while maintaining sub-50ms latency at 3,000 TPS within a fixed monthly budget.

## Key Elements
- Fraud Analyst, Merchant Risk Manager, Compliance / Auditor Officer
- AWS API Gateway
- Real-Time Scoring Engine (Go / Java, AWS ECS Fargate)
- Case Management Backend (AWS ECS Fargate)
- Amazon Aurora PostgreSQL
- Amazon S3
- Amazon ElastiCache (Redis)
- Amazon SQS (Standard Queue, Dead-Letter Queue)

## Relationships
- Real-Time Scoring Engine -> Amazon SQS: Sends asynchronous telemetry/audit events [AWS SDK/SQS API via Interface VPC Endpoint]
- Case Management Backend -> Amazon SQS: Consumes messages via Long Polling and DeleteMessage [AWS SDK/SQS API via Interface VPC Endpoint]
- Real-Time Scoring Engine -> Amazon Aurora PostgreSQL / Amazon ElastiCache: Reads rules/models and writes audit logs [SQL / Redis Protocol]
- Fraud Analyst -> AWS API Gateway: Reviews flagged cases [HTTPS]

## Technology Stack
- AWS ECS Fargate: Container orchestration chosen for low operational overhead and scalability for a 3-person team.
- Amazon Aurora PostgreSQL: Relational storage providing ACID compliance for secure 7-year audit retention.
- Amazon SQS: Managed message broker utilizing batching and VPC endpoints for decoupled, high-throughput asynchronous processing.
- Amazon ElastiCache (Redis): In-memory caching layer ensuring low-latency rule lookups to meet the <50ms P99 latency constraint.

## Rationale
The architecture combines managed serverless and containerized AWS services to handle 3,000 TPS under a strict €25,000 monthly budget. Asynchronous decoupling via SQS protects payment availability and checkout performance while satisfying rigorous PCI-DSS and auditability mandates.