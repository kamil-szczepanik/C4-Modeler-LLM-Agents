## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and provides case management for human analysts. It operates within strict latency, budget, and compliance constraints on AWS.

## Key Elements
- Payment Gateway / Core Processing System
- AWS Application Load Balancer (ALB) & AWS WAFv2 (Ingress)
- Fraud Scoring Engine (Go microservice on Amazon ECS Fargate with ONNX Runtime sidecar)
- Case Management App (Node.js/React monolith on Amazon ECS Fargate)
- Data Stores: Amazon DynamoDB, Amazon RDS PostgreSQL, Amazon S3 with Object Lock
- Event Bus: Amazon EventBridge
- Fraud Analysts and ML Engineers

## Relationships
- Payment Gateway -> AWS Application Load Balancer: Sends authorization requests [gRPC over mTLS 1.3]
- AWS Application Load Balancer -> AWS WAFv2: Inspects request headers and payloads [Internal AWS]
- AWS Application Load Balancer -> Fraud Scoring Engine: Forwards validated requests via target groups [gRPC over HTTP/2]
- Fraud Scoring Engine -> Amazon DynamoDB: Reads feature stores and writes audit logs [AWS PrivateLink]
- Case Management App -> Amazon RDS PostgreSQL: Manages analyst review cases [SQL over TLS]

## Technology Stack
- Ingress/Security: AWS Application Load Balancer, AWS WAFv2, AWS Certificate Manager for TLS 1.3/mTLS (cost-effective, predictable pricing for 3,000 req/s)
- Compute: Amazon ECS Fargate (container orchestration tailored for a 3-engineer team)
- Scoring Core: Go microservice with ONNX Runtime sidecar (meets <50 ms P99 latency SLA)
- Storage & Audit: Amazon DynamoDB, Amazon RDS PostgreSQL, Amazon S3 with Object Lock (ensures 7-year tamper-evident auditability and PCI-DSS compliance)
- Automation: Terraform (enables repeatable, zero-manual-drift deployments)

## Rationale
This architecture leverages AWS serverless and managed containers (ECS Fargate, ALB) to meet the 3,000 req/s and <50 ms P99 latency SLAs within a fixed €25k/month budget. Strict mTLS, WAF log scrubbing, and S3 Object Lock satisfy PCI-DSS Level 1 compliance and 7-year tamper-evident audit requirements.