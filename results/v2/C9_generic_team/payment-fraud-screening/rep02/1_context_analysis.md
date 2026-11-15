## Overview
Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud, providing sub-50ms decisions and case management for human analysts. It operates under strict PCI-DSS Level 1 compliance and budget constraints in AWS eu-west-1.

## Key Elements
- Payment Gateway / Acquirer
- Fraud Screening Engine (AWS ECS Fargate)
- Case Management UI
- AWS RDS PostgreSQL
- AWS S3
- AWS SNS / SQS

## Relationships
- Payment Gateway sends synchronous authorization requests via HTTPS/JSON to Fraud Screening Engine (3,000 TPS, 30ms timeout).
- Fraud Screening Engine fetches model rules from S3 and publishes audit logs to RDS PostgreSQL and S3.
- Fraud Analyst Workstation accesses Case Management UI asynchronously over TLS.
- AWS SNS/SQS pushes model updates to the Fraud Screening Engine.

## Technology Stack
- AWS ECS Fargate: Container orchestration chosen for operational simplicity within the 3-engineer team constraint.
- AWS S3: Versioned model storage and tamper-evident object lock audit logs.
- AWS RDS PostgreSQL: Structured storage for HMAC-chained audit logs and case management.
- AWS SNS/SQS: Asynchronous pub/sub pattern for zero-downtime model hot-swaps.
- AWS CloudWatch: Centralized metrics and structured JSON logging for observability.

## Rationale
This architecture uses proven, managed AWS primitives to maintain low operational overhead for a three-engineer team within a 25,000 EUR monthly budget. It decouples high-throughput synchronous scoring from asynchronous tasks to guarantee strict P99 latency and high availability.