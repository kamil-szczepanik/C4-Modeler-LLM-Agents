## Overview
The system screens card-not-present payment authorizations for fraud in real-time while providing case management for analysts. It operates within a 25,000 EUR monthly budget, meeting PCI-DSS Level 1 compliance and a 7-year auditability requirement.

## Key Elements
- AWS Application Load Balancer (ALB)
- Scoring Engine (Go container on Amazon ECS on AWS Fargate)
- Case Management Backend (Node.js / TypeScript on Amazon ECS on AWS Fargate)
- AWS WAF
- Amazon S3 (for access logging)

## Relationships
- Payment Processor -> AWS Application Load Balancer: Sends payment authorizations via gRPC/HTTPS with mTLS
- Fraud Analyst -> AWS Application Load Balancer: Accesses case management and rule updates via HTTPS
- AWS Application Load Balancer -> Scoring Engine: Routes scoring traffic via HTTP/2 on `/v1/score`
- AWS Application Load Balancer -> Case Management Backend: Routes administrative traffic via HTTP/1.1 on `/v1/cases/*`
- AWS Application Load Balancer -> Amazon S3: Stores access logs for auditability

## Technology Stack
- AWS Application Load Balancer (ALB): Ingress routing, TLS termination, and health checks
- AWS WAF: Edge protection with Managed Rules Core Rule Set (CRS) and rate-limiting
- Amazon ECS on AWS Fargate: Container orchestration for low-overhead scaling
- Amazon S3: Secure, durable storage for 7-year access log retention

## Rationale
This architecture uses managed AWS services to minimize operational overhead for a three-engineer team while staying within the 25,000 EUR budget. Path-based routing and HTTP/2 ensure P99 decision latency remains below 50 ms.