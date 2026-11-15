## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations within 50 ms to prevent fraud while maintaining PCI-DSS Level 1 compliance. It enables fraud analysts to review flagged transactions and supports zero-downtime model updates within AWS.

## Key Elements
- Payment Gateway / External Systems
- Fraud Analysts
- API Gateway (AWS API Gateway HTTP API with Rust/Go Lambda Authorizer)
- Scoring Engine (Go, AWS ECS Fargate, Embedded Model Runtime)
- Case Management API (Node.js/Python, AWS ECS Fargate)
- Data Store (Amazon Aurora PostgreSQL)
- Event Stream (Amazon SQS)

## Relationships
- Payment Gateway -> API Gateway: Sends payment authorizations [HTTPS/REST]
- API Gateway -> Scoring Engine: Dispatches scoring requests [gRPC over VPC Link]
- Scoring Engine -> Data Store: Persists audit logs and decisions [PostgreSQL Wire Protocol / TLS]
- Fraud Analysts -> Case Management API: Reviews suspicious payments [HTTPS/REST]

## Technology Stack
- AWS API Gateway: Provides low-latency edge routing and rate limiting.
- Go (AWS ECS Fargate): Powers the Scoring Engine for high throughput and sub-50ms latency.
- Amazon Aurora PostgreSQL: Stores audit logs and case data with 7-year retention.
- Amazon SQS: Handles asynchronous event streaming for case management updates.

## Rationale
The serverless edge and containerized Go architecture guarantees sub-50ms P99 latency under heavy throughput. Strict tokenization and Aurora PostgreSQL audit logging satisfy PCI-DSS Level 1 and 7-year tamper-evident compliance requirements within budget.