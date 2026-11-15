## Overview
The system screens card-not-present payment authorizations for fraud in real-time and manages reviews for suspicious transactions. It ensures PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a strict budget and lean engineering team.

## Key Elements
- Fraud Analysts, ML Engineers
- Payment Gateway / Acquirer Systems, Card Networks / Token Vaults, Audit / Compliance Archive, ML Model / Rule Registry
- AWS API Gateway, Amazon CloudFront, Amazon S3
- Real-Time Scoring Engine (Go on AWS ECS Fargate)
- ML Inference Service (Python with ONNX Runtime on AWS ECS Fargate)
- Case Management Backend (Go/Node.js on AWS ECS Fargate)
- Amazon ElastiCache (Redis), Amazon DynamoDB, Amazon EventBridge
- Amazon S3 Object Lock (containing Audit Stream Processor, Object Lifecycle Manager, Audit Query API, and Integrity Verifier Go Lambdas)

## Relationships
- Payment Gateway -> AWS API Gateway: Submits authorization requests [HTTPS / REST]
- AWS API Gateway -> Real-Time Scoring Engine: Forwards scoring requests [Internal gRPC]
- Real-Time Scoring Engine -> ML Inference Service: Requests feature inference [Internal gRPC]
- Real-Time Scoring Engine -> Amazon ElastiCache: Fetches rule caches [Redis Protocol]
- Case Management Backend -> Amazon DynamoDB: Persists review cases [AWS SDK / HTTPS]
- Amazon DynamoDB -> Audit Stream Processor: Streams audit logs [DynamoDB Streams]
- Audit Stream Processor -> Object Lifecycle Manager: Writes signed logs [AWS SDK / HTTPS]
- Compliance Auditor -> Audit Query API: Queries historical decisions [HTTPS / REST API Gateway]
- Integrity Verifier -> Object Lifecycle Manager: Verifies checksums [AWS SDK / HTTPS]

## Technology Stack
- AWS ECS Fargate: Runs containerized Go and Python services without server management
- Go: Powers high-throughput backend services and Lambdas for sub-50ms latency
- Python with ONNX Runtime: Executes machine learning inference efficiently
- Amazon DynamoDB: Stores operational cases and audit streams with low latency
- Amazon S3 Object Lock: Enforces WORM storage and 7-year compliance retention
- Redis (Amazon ElastiCache): Provides fast in-memory caching for rules

## Rationale
Serverless and containerized AWS services minimize operational toil, enabling a 3-engineer team to maintain the platform within a 25,000 EUR monthly budget. Go and ONNX runtime ensure P99 decision latency stays below 50 ms at scale.