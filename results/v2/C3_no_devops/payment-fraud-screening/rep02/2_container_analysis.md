## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud at scale while providing case management tools for analysts. It ensures PCI-DSS Level 1 compliance and sub-50ms decision latencies within strict budget constraints.

## Key Elements
- **Payment Gateway / Core Processing Platform & Card Networks**: External systems submitting authorizations and receiving decisions.
- **Fraud Analysts, Risk Managers, & Data Scientists**: Human users reviewing cases and managing models.
- **API Gateway / Ingestion Service**: Go container exposed via AWS ALB handling 3,000 req/sec.
- **Real-Time Scoring Engine**: Python/FastAPI container with ONNX Runtime.
- **Explainability Service**: Python/FastAPI container generating SHAP values.
- **Case Management Web App & Backend**: React SPA hosted on S3/CloudFront with a Node.js/Go backend.
- **Model & Rule Registry & Feature Store**: Amazon S3, PostgreSQL (RDS), and AWS ElastiCache Redis.
- **Security & Infrastructure Services**: AWS Cognito, AWS Secrets Manager, and Amazon SQS.

## Relationships
- **External Systems to API Gateway**: HTTPS/JSON requests for payment screening.
- **Ingestion Service to Scoring Engine**: gRPC with mutual TLS (mTLS) for low-latency scoring.
- **Scoring Engine to Redis & PostgreSQL**: TCP for feature retrieval and offline logging.
- **Case Management App to Backend**: HTTPS/REST or GraphQL with AWS Cognito OAuth 2.0 / OIDC authentication.
- **Audit Logging**: Asynchronous publishing via Amazon SQS to S3 Object Lock storage.

## Technology Stack
- **Compute & Orchestration**: AWS cloud infrastructure in `eu-west-1` optimized for a 3-person team.
- **Languages & Frameworks**: Go for ingestion; Python/FastAPI with ONNX Runtime for inference and explainability.
- **Databases & Caching**: PostgreSQL (RDS) for metadata/audit logs; AWS ElastiCache Redis for real-time features.
- **Security Protocols**: TLS 1.3, mTLS for internal gRPC, AWS Secrets Manager, and S3 Object Lock Compliance Mode.

## Rationale
This container architecture leverages stateless, horizontally scalable services and managed AWS components to meet the 50ms P99 latency and PCI-DSS Level 1 requirements. It maintains a low operational overhead suitable for a three-engineer team while strictly adhering to the 25,000 EUR monthly budget.