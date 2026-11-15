## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and manages reviews for suspicious transactions. It processes 3,000 requests per second within strict PCI-DSS Level 1 compliance and budget constraints.

## Key Elements
- Payment Gateway / Core Processing Platform
- API Gateway / Ingestion Service (AWS ALB, Go, Fiber/Chi Router)
- Real-Time Scoring Engine (Python, FastAPI, ONNX Runtime)
- Case Management Backend & Web App (Node.js, Go, React SPA)
- Model & Registry, Feature Store (Amazon S3, PostgreSQL RDS, AWS ElastiCache Redis)
- Security & Infrastructure (AWS WAF, AWS Secrets Manager, AWS CloudWatch, Amazon SQS)

## Relationships
- Payment Gateway -> API Gateway / Ingestion Service: Forwards authorization requests [HTTPS / JSON, inbound mTLS]
- API Gateway / Ingestion Service -> Real-Time Scoring Engine: Forwards screening requests [gRPC with mTLS, TCP/443]
- API Gateway / Ingestion Service -> AWS CloudWatch: Emits OpenTelemetry metrics and traces [OTLP / HTTPS]

## Technology Stack
- AWS ALB & Go (Fiber/Chi): Chosen for high concurrency and ultra-low latency processing.
- Python (FastAPI) & ONNX Runtime: Chosen for high-performance ML model scoring execution.
- PostgreSQL RDS & AWS ElastiCache Redis: Chosen for sub-millisecond feature lookup and robust metadata storage.
- AWS WAF & AWS Secrets Manager: Chosen to enforce perimeter security, rate limiting, and automated credential rotation.

## Rationale
This architecture utilizes high-performance languages and managed cloud services to meet the strict P99 latency target below 50 ms under high throughput. Layered security controls, tokenization, and graceful circuit breaking ensure PCI-DSS compliance and operational resilience within budget.