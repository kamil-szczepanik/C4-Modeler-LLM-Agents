## Overview
The system provides real-time fraud screening for card-not-present payment authorizations and case management for fraud analysts within a mid-size payment processor. It ensures sub-50ms decision latency while maintaining PCI-DSS compliance and a 7-year tamper-evident audit trail on AWS.

## Key Elements
- Fraud Analysts
- Payment Gateway / Acquirer
- Fraud Analyst UI (React SPA via Amazon S3 / CloudFront)
- API Gateway & Ingress (Java / Spring Cloud Gateway)
- Real-Time Scoring Engine (Java / Spring Boot + ONNX)
- Case Management Backend (Node.js / TypeScript)
- Model & Rule Management Service (Python / FastAPI)
- Audit Worker
- Amazon Kinesis Data Streams
- Amazon Aurora PostgreSQL (Primary writer and Read Replicas)
- Amazon ElastiCache (Redis)

## Relationships
- Fraud Analyst UI -> API Gateway & Ingress via [HTTPS/TLS]
- API Gateway & Ingress -> Real-Time Scoring Engine via [gRPC / TLS]
- Real-Time Scoring Engine -> Amazon Kinesis Data Streams via [AWS SDK / TLS]
- Audit Worker -> Amazon Aurora PostgreSQL via [TLS/TCP, SQL]
- Case Management Backend -> Amazon Aurora PostgreSQL via [TLS/TCP, SQL via PgBouncer]

## Technology Stack
- AWS (eu-west-1): Target cloud infrastructure supporting high throughput within budget.
- Java / Spring Boot & ONNX: Provides high-performance real-time model scoring under 50ms P99.
- Node.js / TypeScript: Powers lightweight and efficient case management backend services.
- Amazon Aurora PostgreSQL: Delivers scalable relational storage with `pgcrypto` and Read Replicas.
- Amazon Kinesis: Handles high-throughput asynchronous audit logging events.

## Rationale
This architecture uses scalable AWS serverless and managed components to handle 3,000 authorizations per second while staying under the 25,000 EUR monthly budget. It separates read and write workloads to guarantee low-latency fraud decisions and strict 7-year tamper-evident auditability.