## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect and prevent fraud. It processes transactions under strict PCI-DSS Level 1 constraints while providing case management for fraud analysts.

## Key Elements
- API Gateway (Envoy)
- Real-Time Scoring Engine (Go, ONNX Runtime, AWS ECS Fargate)
- Case Management Backend (Node.js / Spring Boot)
- Web Application (React SPA, AWS S3, CloudFront)
- Audit Log Worker (Go)
- AWS Aurora PostgreSQL (PostgreSQL, AWS Aurora)
- Amazon SQS

## Relationships
- Payment Gateway -> API Gateway (Envoy): Submits payment authorization requests via mTLS/HTTPS
- API Gateway (Envoy) -> Real-Time Scoring Engine: Forwards scoring requests via gRPC/HTTP2
- API Gateway (Envoy) -> Case Management Backend: Routes administrative and analyst traffic via HTTPS
- Case Management Backend -> AWS Aurora PostgreSQL: Persists case data and decisions via TLS/PostgreSQL Protocol

## Technology Stack
- Envoy: High-performance C++ API Gateway for mTLS termination, local rate limiting, and circuit breaking
- AWS ECS Fargate: Serverless container execution for cost efficiency and minimal operational overhead
- Go & ONNX Runtime: High-performance scoring execution meeting sub-50ms latency requirements
- AWS Aurora PostgreSQL: Secure, managed relational database supporting 7-year audit retention

## Rationale
This architecture uses serverless containers and managed AWS services to fit a 25,000 EUR monthly budget and a 3-person engineering team. Envoy and Go components ensure sub-50ms P99 latency at 3,000 requests per second while maintaining strict PCI-DSS Level 1 compliance.