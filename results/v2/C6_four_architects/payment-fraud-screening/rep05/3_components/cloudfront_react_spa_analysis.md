## Overview
This system provides real-time fraud screening for card-not-present payment authorizations and a case management interface for fraud analysts. It ensures sub-50ms P99 decision latencies while maintaining strict PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.

## Key Elements
- **Fraud Analysts**: End users reviewing suspicious transactions via the UI.
- **CloudFront / React SPA**: Frontend container hosted on Amazon S3 and distributed via Amazon CloudFront.
- **Fraud Scoring Service**: High-throughput inference container running on Amazon ECS Fargate with Python, FastAPI, and ONNX Runtime.
- **Case Management API**: Backend container on Amazon ECS Fargate managing analyst workflows.
- **Data Stores**: Amazon Aurora PostgreSQL, Amazon S3 Model Registry, Amazon S3 Object Lock, and Amazon ElastiCache (Redis).
- **Messaging & Routing**: Amazon SQS, AWS Lambda, Amazon API Gateway, and AWS Application Load Balancer (ALB).

## Relationships
- Fraud Analysts -> CloudFront / React SPA: Accesses review UI [HTTPS]
- CloudFront / React SPA -> API Gateway: Sends API requests [HTTPS/REST]
- API Gateway -> Fraud Scoring Service / Case Management API: Routes traffic [HTTPS/REST]
- Fraud Scoring Service -> Amazon ElastiCache (Redis): Reads cached profiles [RESP/TCP]
- Fraud Scoring Service -> Amazon Aurora PostgreSQL: Persists audit logs and decisions [PostgreSQL Wire Protocol]

## Technology Stack
- **Compute**: Amazon ECS Fargate for containerized microservices, AWS Lambda for asynchronous tasks, ensuring zero server management for a 3-engineer team.
- **AI/ML Runtime**: ONNX Runtime within FastAPI to execute fraud models in-memory, avoiding Python GIL bottlenecks to meet R-04 performance.
- **Data & Caching**: Amazon Aurora PostgreSQL for structured data and 7-year audit logs; Amazon ElastiCache (Redis) for sub-millisecond feature retrieval.
- **Storage & Compliance**: Amazon S3 with Object Lock for tamper-evident audit trails and static asset hosting via Amazon CloudFront.

## Rationale
The architecture combines serverless and managed AWS services to operate well within the 25,000 EUR monthly budget while supporting a lean 3-engineer team. In-memory ONNX inference and Redis caching guarantee sub-50ms latency at 3,000 TPS to satisfy strict performance and compliance requirements.