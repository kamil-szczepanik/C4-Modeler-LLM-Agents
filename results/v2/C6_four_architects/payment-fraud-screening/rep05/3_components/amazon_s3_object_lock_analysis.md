## Overview
The system provides real-time card-not-present payment fraud screening and case management for a mid-size payment processor. It ensures secure, low-latency transaction scoring while maintaining strict regulatory compliance and auditability.

## Key Elements
- Fraud Analysts
- AWS Application Load Balancer (ALB)
- Fraud Scoring Service (Python, FastAPI, ONNX Runtime, Amazon ECS Fargate)
- Case Management API (Amazon ECS Fargate)
- React SPA (Amazon CloudFront, React)
- Amazon ElastiCache (Redis)
- Amazon S3 Model Registry
- Amazon SQS & AWS Lambda
- Amazon S3 Object Lock (Compliance Mode)
- Amazon Aurora PostgreSQL

## Relationships
- React SPA -> AWS ALB: Forwards client traffic via `HTTPS`
- AWS ALB -> Fraud Scoring Service / Case Management API: Routes internal traffic via `HTTP/gRPC`
- Fraud Scoring Service -> Amazon ElastiCache (Redis): Caches rules and models via `RESP`
- AWS Lambda -> Amazon S3 Object Lock: Stores immutable audit logs via `HTTPS (PutObject)`
- Fraud Analysts -> React SPA: Manages review cases via `HTTPS`

## Technology Stack
- Python / FastAPI: High-performance backend processing
- ONNX Runtime: Low-latency ML model execution
- Amazon ECS Fargate: Serverless container orchestration fitting the lean team model
- Amazon Aurora PostgreSQL: Relational storage for transactional case data
- Amazon S3 Object Lock: WORM-compliant storage for 7-year audit retention

## Rationale
This architecture meets the strict P99 latency requirement under 50 ms while enforcing PCI-DSS Level 1 compliance and 7-year tamper-evident auditability. Leveraging serverless and managed AWS services aligns with the 25,000 EUR monthly budget and operational constraints of a three-engineer team.