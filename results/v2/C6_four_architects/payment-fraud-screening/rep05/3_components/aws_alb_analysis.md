## Overview
- Real-Time Payment Fraud Screening system for mid-size payment processors, screening card-not-present transactions and managing analyst reviews.
- Designed for high throughput, strict auditability, and PCI-DSS compliance under strict budget and team constraints.

## Key Elements
- Payment Gateway / Client
- React SPA (Amazon CloudFront, React)
- AWS Application Load Balancer (AWS ALB) with AWS ACM
- Fraud Scoring Service (Python, FastAPI, ONNX Runtime, Amazon ECS Fargate)
- Case Management API (Amazon ECS Fargate)
- Amazon Aurora PostgreSQL, Amazon S3 Model Registry, Amazon S3 Object Lock
- Amazon ElastiCache (Redis), Amazon SQS, AWS Lambda

## Relationships
- Payment Gateway -> AWS ALB: Sends payment authorizations [HTTPS/gRPC, TLS 1.3 via AWS ACM]
- React SPA -> AWS ALB: Sends analyst management requests [HTTPS/REST]
- AWS ALB -> Fraud Scoring Service: Routes gRPC scoring traffic [gRPC over HTTP/2 via AWS Cloud Map]
- AWS ALB -> Case Management API: Routes REST management traffic [HTTPS/REST via AWS Cloud Map]

## Technology Stack
- AWS: Cloud infrastructure provider in region eu-west-1
- Amazon ECS Fargate: Container orchestration for microservices without server management overhead
- ONNX Runtime: High-performance machine learning inference engine for fast fraud scoring
- Amazon Aurora PostgreSQL: Relational database with encryption for transactional data
- Amazon S3 Object Lock: Tamper-evident storage for 7-year auditability compliance

## Rationale
- Microservices on ECS Fargate with gRPC/HTTP/2 meet the sub-50ms P99 latency requirement at 3,000 req/sec within budget.
- Fully managed AWS services ensure PCI-DSS Level 1 compliance and 7-year tamper-evident auditability while remaining maintainable by a three-person engineering team.