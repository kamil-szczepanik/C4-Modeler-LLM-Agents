## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for mid-size payment processors to detect fraud before approval, while providing case management for suspicious payments. It operates within a strict PCI-DSS Level 1 compliance framework and a fixed infrastructure budget.

## Key Elements
- Shopper / Cardholder & Merchant (External Users)
- AWS API Gateway (Ingress and Tokenization Boundary Container)
- Scoring Engine & Case Management App (Amazon ECS Fargate Containers)
- Feature Store & Cache (Amazon ElastiCache Redis, Amazon DynamoDB)
- Audit & Streaming Pipeline (Amazon Kinesis Data Streams, Amazon Kinesis Firehose)
- Audit Storage (Amazon S3 with Object Lock in Compliance Mode)
- HTTP Route Resolver, Native JWT Authorizer, and VPC Link Integration (AWS API Gateway Components)

## Relationships
- Shopper / Cardholder & Merchant -> HTTP Route Resolver: Sends screening payloads [REST/JSON over HTTPS (TLS 1.3)]
- HTTP Route Resolver -> Native JWT Authorizer: Validates bearer tokens [Internal Evaluation]
- HTTP Route Resolver -> VPC Link Integration: Forwards sanitized payloads [gRPC over HTTP/2]
- VPC Link Integration -> Scoring Engine: Routes screened requests [Internal ALB / gRPC with mTLS]

## Technology Stack
- AWS API Gateway (HTTP API v2): Provides low-overhead HTTP/2 ingress to meet P99 latency targets.
- API Gateway Native JWT Authorizer: Validates tokens at the edge without custom compute overhead.
- AWS WAF: Deployed at the edge for OWASP protection and DDoS mitigation.
- Amazon ECS Fargate: Runs containerized internal workloads with minimal operational burden.
- Amazon S3 (Object Lock): Secures tamper-evident 7-year audit logs in Compliance Mode.

## Rationale
This architecture uses fully managed cloud services to minimize operational overhead for a three-person engineering team. It enforces low-latency, secure data processing to meet strict performance and PCI-DSS Level 1 constraints within budget.