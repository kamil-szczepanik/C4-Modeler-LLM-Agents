## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in real time to prevent fraud while enabling analysts to review suspicious transactions. It ensures strict regulatory compliance, low latency, and continuous learning within a fixed budget and small team capacity.

## Key Elements
- Fraud Analyst (Person)
- Payment Gateway / Acquirer (External System)
- AWS Application Load Balancer (ALB)
- Fraud Scoring Engine (Java / Spring Boot, AWS ECS Fargate, ONNX/LightGBM)
- Case Management Service (Node.js / NestJS, AWS ECS Fargate)
- Feature Store / Cache (Amazon ElastiCache Redis & Amazon DynamoDB)
- Transactional Database (Amazon Aurora PostgreSQL)
- Audit Storage (Amazon S3 with Object Lock)
- Asynchronous Messaging (Amazon SQS & Amazon SNS)
- Analyst Frontend (Amazon S3 + Amazon CloudFront SPA)

## Relationships
- Payment Gateway -> AWS ALB: Forwards card-not-present payment authorizations [REST/HTTPS]
- AWS ALB -> Fraud Scoring Engine: Routes scoring requests [HTTP/2 or gRPC]
- Fraud Scoring Engine -> Feature Store / Cache: Fetches user and card behavioral features [Redis RESP / DynamoDB API via AWS SDK]
- Fraud Scoring Engine -> Asynchronous Messaging (SQS): Escalates suspicious payments requiring review [AWS SDK]
- SQS -> Case Management Service: Delivers queued review events [AWS SDK / Polling]
- Analyst Frontend -> Case Management Service: Manages review workflows via Case API Controller [REST/HTTPS (JSON over HTTP/2)]
- Case Management Service -> Transactional Database (Aurora PostgreSQL): Persists case states [TCP/Postgres, TLS]
- Case Management Service -> Audit Storage (Amazon S3 Object Lock): Stores tamper-evident decision and audit logs [HTTPS / AWS SDK]
- Case Management Service -> Asynchronous Messaging (SNS/SQS): Publishes analyst feedback for model retraining [AWS SDK / HTTPS]

## Technology Stack
- AWS ECS Fargate: Container orchestration for low-overhead, serverless scaling within a fixed budget
- Amazon Aurora PostgreSQL: Transactional relational database for reliable case management state storage
- Amazon S3 Object Lock: Tamper-evident storage ensuring 7-year auditability for regulatory compliance
- NestJS (Node.js): Modular backend framework implementing clean separation for security and sanitization interceptors
- Amazon ElastiCache Redis & Amazon DynamoDB: High-performance caching and feature storage ensuring sub-50ms P99 scoring latency

## Rationale
This architecture uses serverless container infrastructure on AWS to meet strict sub-50ms P99 performance requirements and PCI-DSS Level 1 constraints while remaining operable by a three-engineer team under a 25,000 EUR monthly budget. Dedicated S3 Object Lock audit storage and NestJS-based data masking components guarantee 7-year auditability and secure card data handling without adding excessive operational complexity.