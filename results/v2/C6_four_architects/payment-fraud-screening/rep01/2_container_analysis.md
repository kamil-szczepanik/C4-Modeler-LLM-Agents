## Overview
A real-time payment fraud screening and case management system evaluates card-not-present payment authorizations in AWS eu-west-1. It delivers sub-50ms fraud decisions while ensuring PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
* Fraud Analysts and ML Engineers (Users)
* Payment Gateway / Acquirer Systems and Card Networks / Token Vaults (External Systems)
* AWS API Gateway (Ingestion Router)
* Real-Time Scoring Engine (Go on AWS ECS Fargate)
* ML Inference Service (Python with ONNX Runtime on AWS ECS Fargate)
* Case Management Backend (Go/Node.js on AWS ECS Fargate)
* Fraud Analyst Frontend (Amazon CloudFront and S3)
* Amazon ElastiCache (Redis Feature Store)
* Amazon DynamoDB and Amazon S3 Object Lock (Data Storage & Audit Archive)
* Amazon EventBridge (Event Bus)

## Relationships
* Payment Gateway to AWS API Gateway: mTLS over HTTPS / gRPC
* AWS API Gateway to Real-Time Scoring Engine: gRPC
* Real-Time Scoring Engine to ML Inference Service: Internal gRPC
* Real-Time Scoring Engine to Amazon ElastiCache (Redis): TCP (RESP)
* Real-Time Scoring Engine and Case Management Backend to Amazon DynamoDB: HTTPS (AWS SDK)
* DynamoDB Streams to Amazon S3 Object Lock: AWS Internal Stream
* Real-Time Scoring Engine to Amazon EventBridge: HTTPS (AWS SDK)
* Amazon EventBridge to Case Management Backend: HTTPS / Webhook
* Fraud Analyst Frontend to Case Management Backend: HTTPS

## Technology Stack
* AWS ECS Fargate: Container orchestration chosen to minimize operational overhead for a 3-person team within a €25k/month budget.
* Go: Powers the Real-Time Scoring Engine and Case Management Backend to guarantee P99 latency below 50ms at 3,000 TPS.
* Python with ONNX Runtime: Powers the ML Inference Service to enable zero-downtime model updates and fast scoring execution.
* Amazon ElastiCache (Redis): Provides low-latency feature lookups for context hydration.
* Amazon DynamoDB with S3 Object Lock: Delivers scalable storage and tamper-evident 7-year auditability via WORM storage.
* Amazon EventBridge: Handles asynchronous, event-driven case routing.

## Rationale
This architecture combines lightweight AWS Fargate containers with Go and ONNX runtimes to meet strict P99 latency and high-throughput demands. It achieves PCI-DSS compliance and tamper-evident 7-year audit logging using serverless AWS services within a fixed budget and small team capacity.