## Overview
A real-time payment fraud screening system evaluates card-not-present payment authorizations within 50 ms at P99 while enabling fraud analysts to review suspicious transactions. It maintains PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a €25k monthly AWS budget.

## Key Elements
- Fraud Analyst (Person)
- Payment Gateway / Acquirer (External System)
- API Gateway / Ingestion Container (AWS API Gateway / Envoy proxy)
- High-Performance Scoring Engine (AWS ECS on Fargate)
- Feature Store (Redis)
- Async Event Bus (AWS EventBridge / SQS)
- Case Management Web Application (AWS ECS on Fargate)
- Model & Rule Registry Container
- Audit & Compliance Storage (AWS S3 with Object Lock and Parquet format)
- Configuration & Secrets Management (AWS Secrets Manager / Parameter Store)

## Relationships
- Payment Gateway to API Gateway / Ingestion Container via HTTPS/TLS
- API Gateway to High-Performance Scoring Engine via internal VPC gRPC/REST
- Scoring Engine to Feature Store via Redis Protocol
- Scoring Engine to Async Event Bus via AWS SDK (JSON/Protobuf over SQS/EventBridge)
- Async Event Bus to Case Management and Audit Storage via AWS SQS/SNS
- Fraud Analyst to Case Management Web Application via HTTPS/TLS

## Technology Stack
- AWS (eu-west-1): Cloud provider and regional infrastructure
- AWS ECS on Fargate: Stateless container hosting for predictable scaling within budget
- Redis: In-memory feature store for ultra-low latency lookups (R-04)
- AWS S3 Object Lock: Tamper-evident, cost-effective 7-year audit storage (R-06)
- AWS API Gateway / Envoy: Ingress security, rate limiting, and tokenization stripping (R-05)
- JSON Schema / Protobuf: Strongly typed, backward-compatible event contracts

## Rationale
Stateless Fargate containers combined with an in-memory Redis feature store achieve the sub-50ms latency requirement (R-04) within the €25k budget. AWS S3 Object Lock and decoupled asynchronous event processing ensure PCI-DSS compliance and 7-year tamper-evident auditability (R-06) without impacting real-time transaction performance.