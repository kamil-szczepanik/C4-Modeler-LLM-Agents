## Overview
The system is a real-time card-not-present payment fraud screening platform deployed on AWS to score payment authorizations, manage analyst reviews, and ensure PCI-DSS compliance. It processes 3,000 TPS with sub-50ms P99 latency while maintaining tamper-evident 7-year audit logs within a €25k monthly budget.

## Key Elements
- **Payment Gateway / Client**: External caller initiating payment authorizations.
- **Fraud Analysts**: Human reviewers managing suspicious transactions via UI.
- **AWS ALB**: Ingress load balancer handling gRPC/HTTP/2 traffic.
- **Fraud Scoring Service**: Python/FastAPI container on Amazon ECS Fargate using ONNX Runtime.
- **Case Management API**: ECS Fargate service for analyst review workflows.
- **Amazon ElastiCache (Redis)**: Low-latency feature store and cache.
- **Amazon S3 Model Registry**: S3 bucket for zero-downtime model and rule hot-reloading.
- **Amazon SQS & AWS Lambda**: Asynchronous messaging and audit processor.
- **Amazon S3 Object Lock**: Tamper-evident 7-year audit storage in Compliance Mode.
- **Amazon Aurora PostgreSQL**: Operational data store for case management.
- **AWS Cloud Map**: Lightweight internal service discovery.

## Relationships
- Payment Gateway -> AWS ALB (HTTPS/gRPC)
- AWS ALB -> Fraud Scoring Service (gRPC/HTTP/2 via AWS Cloud Map)
- Fraud Analyst -> CloudFront/React SPA -> API Gateway -> Case Management API (HTTPS/REST)
- Fraud Scoring Service <-> Amazon ElastiCache Redis (TCP/RESP)
- Fraud Scoring Service -> Amazon S3 Model Registry (HTTPS)
- Fraud Scoring Service -> Amazon SQS (HTTPS) -> AWS Lambda -> Amazon S3 Object Lock (HTTPS)
- Case Management API -> Amazon Aurora PostgreSQL (TCP/TLS)

## Technology Stack
- **Compute**: Amazon ECS Fargate (multi-AZ) chosen to minimize operational overhead for a 3-engineer team.
- **Inference**: Python with FastAPI and ONNX Runtime for high-performance <50ms P99 fraud scoring.
- **Storage**: Amazon Aurora PostgreSQL for operational data; Amazon S3 with Object Lock for tamper-evident audit logs.
- **Caching**: Amazon ElastiCache (Redis) for rapid feature retrieval.
- **Messaging**: Amazon SQS and AWS Lambda for zero-ops, asynchronous audit processing.
- **Networking/Discovery**: AWS ALB with gRPC and AWS Cloud Map for low-latency internal routing.

## Rationale
The architecture leverages serverless and managed AWS services (ECS Fargate, SQS, Lambda, S3) to operate reliably with a team of three engineers while strictly respecting the €25k monthly budget. High availability, dual-AZ deployments, fail-open circuit breakers, and decoupled async S3 Object Lock auditing guarantee sub-50ms performance, PCI-DSS compliance, and resilience against outages.