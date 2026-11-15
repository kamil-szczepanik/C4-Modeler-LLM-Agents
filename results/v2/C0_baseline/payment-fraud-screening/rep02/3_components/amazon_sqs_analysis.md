## Overview
This system is a real-time payment fraud screening platform that evaluates card-not-present authorizations and supports fraud case management. It ensures PCI-DSS compliance while meeting sub-50ms latency targets on AWS.

## Key Elements
- Fraud Analysts and Risk Operations Managers (Users)
- Payment Gateway / Acquirer and Card Schemes / Tokenization Service (External Systems)
- API Gateway & Tokenization Proxy (Java / Spring Cloud Gateway)
- Fraud Scoring Engine (Java / Spring Boot)
- Case Management & Rule UI (Node.js / TypeScript)
- Amazon DynamoDB and Amazon S3 with Object Lock
- Amazon SQS (Standard Queues with DLQs)
- Identity Provider and Audit / Compliance Archive

## Relationships
- Case Management & Rule UI -> Amazon SQS: Dispatches rule updates and audit logs asynchronously [AWS SDK / HTTPS]
- Amazon SQS -> Fraud Scoring Engine: Delivers rule update notifications [AWS SDK / HTTPS]
- Fraud Scoring Engine -> Amazon DynamoDB: Persists transaction states and idempotency records [AWS SDK]
- Fraud Scoring Engine -> Amazon S3: Stores tamper-evident audit logs via downstream workers [AWS SDK]

## Technology Stack
- AWS (eu-west-1): Target cloud provider ensuring managed scalability within budget constraints
- Amazon SQS (Standard Queues): Asynchronous message broker providing high throughput for rule updates and audit logging without blocking low-latency paths
- AWS KMS: Customer Managed Keys (CMK) enforcing encryption at rest for PCI-DSS compliance
- Amazon S3 with Object Lock: Tamper-evident storage satisfying the 7-year auditability requirement

## Rationale
This architecture uses SQS Standard queues to decouple high-throughput audit logging from the critical payment path, guaranteeing sub-50ms P99 latency. Fully managed AWS services minimize operational overhead, fitting within the 3-engineer team capacity and fixed monthly budget.