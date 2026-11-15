## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides a case management interface for analysts to review suspicious transactions. It ensures high-performance, compliant transaction processing while strictly adhering to budget and security constraints.

## Key Elements
* **Fraud Analysts & Risk Operations Managers**: Internal human users reviewing cases and managing rules.
* **API Gateway / Ingress Router**: Amazon API Gateway / ALB terminating TLS.
* **Scoring Engine**: Stateless container evaluating rules and ML models in-memory.
* **Case Management API**: Container handling analyst workflows and review queues.
* **Fraud Analyst SPA**: React single-page application hosted in Amazon S3 / CloudFront.
* **Rule & Model Distribution Service**: Container handling zero-downtime rule/model updates.
* **Audit & Persistence Store**: Amazon Aurora PostgreSQL with cryptographic chaining.
* **Feature Store**: Amazon ElastiCache Redis.
* **Asynchronous Event Bus**: Amazon EventBridge / MSK Lite.

## Relationships
* **Payment Gateway to API Gateway / Ingress Router**: HTTPS/gRPC over TLS 1.3 processing authorization requests.
* **API Gateway to Scoring Engine**: gRPC/HTTP2 over TLS enforcing mTLS within private subnets.
* **Scoring Engine to ElastiCache Redis**: RESP protocol over private VPC.
* **Scoring Engine to Event Bus**: HTTPS via AWS SDK for asynchronous decision streaming.
* **Fraud Analyst SPA to Case Management API**: HTTPS/REST with OAuth2/OIDC via AWS Cognito.
* **Rule & Model Distribution Service to Amazon S3**: HTTPS for polling cryptographically signed rule bundles (Ed25519).

## Technology Stack
* **Cloud Infrastructure**: AWS (eu-west-1 region) utilizing Amazon ECS Fargate for container orchestration within a €25,000/month budget.
* **Compute & Languages**: Java/Spring Boot or Go for high-throughput Scoring and Distribution services; Node.js or Python/FastAPI for Case Management.
* **Frontend**: React SPA hosted on Amazon S3 and delivered via Amazon CloudFront.
* **Data & Caching**: Amazon Aurora PostgreSQL with cryptographic chaining for tamper-evident audit logs; Amazon ElastiCache Redis for low-latency feature stores.
* **Security & Auth**: AWS KMS for encryption at rest; AWS Cognito for OIDC/OAuth2 with hardware-token MFA.

## Rationale
This architecture achieves sub-50ms P99 latency at 3,000 TPS through stateless, in-memory scoring coupled with ElastiCache Redis, while decoupling heavy logging via an asynchronous event bus. Strict network isolation and tokenization protect cardholder data, ensuring PCI-DSS Level 1 compliance and low audit overhead for a three-engineer team within budget.