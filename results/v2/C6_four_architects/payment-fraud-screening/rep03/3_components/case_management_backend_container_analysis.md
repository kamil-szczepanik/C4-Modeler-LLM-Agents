## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and provides a case management interface for analysts. It operates on AWS within strict PCI-DSS Level 1 compliance constraints and a 25,000 EUR monthly budget.

## Key Elements
- Fraud Analysts (System Users)
- AWS Application Load Balancer (ALB)
- Scoring Engine Container (Go, ONNX Runtime, AWS ECS Fargate)
- Case Management Backend Container (Node.js, TypeScript, AWS ECS Fargate)
- Tokenization Proxy Container (AWS Nitro Enclaves)
- Amazon DynamoDB
- Amazon S3 Object Lock
- Identity Provider
- ML Feature Store / Threat Intelligence Provider

## Relationships
- AWS Application Load Balancer -> Case Management Backend Container [HTTPS/REST, TLS 1.3]
- Scoring Engine Container -> Amazon S3 Object Lock [AWS SDK, Append-only audit logs]
- Case Management Backend Container -> Amazon DynamoDB [Read/Write cases, VPC Endpoints]
- Case Management Backend Container -> Tokenization Proxy Container [gRPC over internal VPC, mTLS]
- Scoring Engine Container -> ML Feature Store [gRPC, TLS 1.3 via VPC Endpoints]

## Technology Stack
- Node.js & TypeScript (Case Management backend for maintainability)
- Go & ONNX Runtime (Scoring Engine for sub-50ms P99 latency)
- AWS ECS Fargate (Container orchestration for operational simplicity)
- Amazon DynamoDB (Scalable case data persistence)
- Amazon S3 Object Lock (Tamper-evident 7-year audit logging)
- AWS Nitro Enclaves (Card tokenization and data isolation)

## Rationale
This architecture uses serverless container infrastructure on AWS Fargate to minimize operational overhead for a three-engineer team. Dedicated Go services and ONNX Runtime guarantee strict sub-50ms performance while Nitro Enclaves and S3 Object Lock enforce PCI-DSS compliance.