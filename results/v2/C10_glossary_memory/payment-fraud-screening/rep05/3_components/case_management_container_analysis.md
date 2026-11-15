## Overview
[Real-Time Payment Fraud Screening System screens card-not-present payment authorizations in under 50ms and provides case management for fraud analysts. It maintains PCI-DSS Level 1 compliance and a strict 7-year tamper-evident audit trail within a €25,000 monthly budget.]

## Key Elements
- Fraud Analysts & Risk/Compliance Officers [person]
- API Gateway / Ingress Container [container, AWS API Gateway or Envoy]
- Fraud Scoring Engine Container [container, Go or Rust]
- Case Management Container [container, Node.js/Python + React SPA on Amazon S3 / CloudFront]
- Model Registry Container [container, MLflow on Amazon ECS]
- Database & Storage [container, Amazon Aurora Serverless v2]
- Caching Layer [container, Amazon ElastiCache with Redis OSS]
- Case API Router [component, Node.js Express/Fastify]
- Analyst Action Service [component]
- Case Management UI [component, React SPA]
- Case Search & Filter Service [component]
- Batch Processing Coordinator [component]

## Relationships
- Fraud Analysts & Risk/Compliance Officers -> Case Management Container: HTTPS via TLS 1.3
- Case Management UI -> Case API Router: HTTPS via TLS 1.3 (JSON/REST)
- Case API Router -> Analyst Action Service: Internal function calls
- Case API Router -> Case Search & Filter Service: Internal function calls
- Case API Router -> Batch Processing Coordinator: Internal function calls
- Analyst Action Service -> Database & Storage: PostgreSQL Wire Protocol
- Case Search & Filter Service -> Database & Storage: PostgreSQL Wire Protocol
- Batch Processing Coordinator -> Database & Storage: PostgreSQL Wire Protocol

## Technology Stack
- Node.js / Python: Powers the backend API for case management and batch processing efficiently with a 3-person team.
- React SPA on Amazon S3 / CloudFront: Delivers a secure, high-performance analyst interface with strict public-to-private trust boundaries.
- Amazon ECS Fargate: Runs backend containers securely inside private VPC subnets without Kubernetes overhead.
- Amazon Aurora Serverless v2: Provides auto-scaling transactional storage with append-only tables and immutable triggers for R-06 auditability.

## Rationale
[This architecture uses managed serverless AWS services and lightweight container runtimes to meet strict sub-50ms performance and PCI-DSS requirements within budget. It empowers a 3-person engineering team to operate the platform reliably while ensuring complete auditability and zero-downtime model updates.]