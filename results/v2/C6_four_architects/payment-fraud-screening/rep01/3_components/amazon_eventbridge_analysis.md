## Overview
This system provides real-time fraud screening for card-not-present payment authorizations and case management for fraud analysts. It ensures sub-50ms decision latency while maintaining strict PCI-DSS compliance and 7-year tamper-evident auditability.

## Key Elements
- Fraud Analysts, ML Engineers
- Payment Gateway / Acquirer Systems, Card Networks / Token Vaults, Audit / Compliance Archive, ML Model / Rule Registry
- AWS API Gateway
- Real-Time Scoring Engine (Go on AWS ECS Fargate)
- ML Inference Service (Python with ONNX Runtime on AWS ECS Fargate)
- Case Management Backend (Go/Node.js on AWS ECS Fargate)
- Fraud Analyst Frontend (Amazon CloudFront and S3)
- Amazon ElastiCache (Redis), Amazon DynamoDB
- Amazon S3 Object Lock
- Amazon EventBridge (Default Event Bus, Fraud Event Rules, Case Management Target, Audit Archive Target, Dead-Letter Queue)

## Relationships
- Payment Gateway -> AWS API Gateway: Submits authorization requests [HTTPS]
- Real-Time Scoring Engine -> ML Inference Service: Requests feature scoring [gRPC / HTTPS]
- Real-Time Scoring Engine -> Amazon ElastiCache: Fetches user velocity and card profiles [Redis Protocol / TCP]
- Default Event Bus -> Case Management Target: Dispatches filtered review events [AWS internal SQS]
- Default Event Bus -> Audit Archive Target: Streams decision logs [Kinesis Data Firehose / HTTPS]
- Audit Archive Target -> Amazon S3 Object Lock: Stores immutable audit records [HTTPS]

## Technology Stack
- AWS Cloud (eu-west-1): Provides a fixed-budget, scalable infrastructure adhering to regional constraints.
- Go and Python (ONNX Runtime): Delivers high-performance scoring and low-latency machine learning inference.
- Amazon ECS Fargate: Eliminates server management overhead for a three-engineer team.
- Amazon S3 Object Lock: Ensures tamper-evident, 7-year audit retention for regulatory compliance.
- Amazon EventBridge and SQS: Handles asynchronous, decoupled event routing reliably without blocking core scoring.

## Rationale
This serverless-first, asynchronous architecture protects the 50ms P99 scoring latency by offloading non-critical tasks. It satisfies PCI-DSS Level 1 and stringent audit requirements while remaining operable within budget by a three-engineer team.