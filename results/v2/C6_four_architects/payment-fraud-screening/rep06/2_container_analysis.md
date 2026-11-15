## Overview
- Real-Time Payment Fraud Screening system processing card-not-present payment authorizations for a mid-size payment processor.
- Screens transactions for fraud within strict latency limits and provides case management tools for fraud analysts.

## Key Elements
- API Gateway / Envoy (Ingress, TLS termination, fail-open circuit breaker)
- Fraud Scoring Engine (Go, gRPC)
- Case Management Backend (Java, Spring Boot)
- Model & Rule Registry Service (Python, FastAPI, S3)
- Analyst UI (React, AWS S3, CloudFront)
- Asynchronous Audit Worker (Go, AWS Lambda)
- Redis Cluster / Amazon ElastiCache (Feature store)
- PostgreSQL / Amazon Aurora (Transactional store)
- Amazon SQS / SNS (Asynchronous event bus)
- AWS S3 Object Lock (Tamper-evident archive)
- AWS Secrets Manager / Parameter Store (Config and secrets)
- AWS Cognito (Identity Provider / OIDC)

## Relationships
- Payment Gateway calls API Gateway via HTTPS/JSON
- API Gateway invokes Fraud Scoring Engine via gRPC
- Fraud Scoring Engine queries Redis Cluster via TCP/TLS
- Fraud Scoring Engine publishes telemetry to Amazon SQS
- SQS triggers Asynchronous Audit Worker Lambda via AWS internal protocols
- Audit Worker Lambda writes to AWS S3 Object Lock via HTTPS
- Fraud Scoring Engine fetches compiled models from Model Registry via gRPC/polling
- Analyst UI authenticates against AWS Cognito via OAuth2/OIDC (HTTPS)
- Analyst UI communicates with Case Management Backend via HTTPS/REST
- Case Management Backend persists cases to PostgreSQL via TLS

## Technology Stack
- Go / gRPC: Powers the Fraud Scoring Engine for sub-50ms P99 latency
- Java / Spring Boot: Powers the Case Management Backend for enterprise analyst workflows
- Python / FastAPI: Powers the Model & Rule Registry for zero-downtime rule updates
- React / CloudFront: Delivers the Analyst UI SPA
- Amazon ElastiCache (Redis): Provides low-latency feature lookups
- Amazon Aurora (PostgreSQL): Stores transactional case data
- AWS Lambda & SQS: Handles serverless asynchronous event-driven auditing
- AWS S3 Object Lock: Guarantees tamper-evident 7-year audit retention
- AWS Cognito & Secrets Manager: Ensures PCI-DSS Level 1 compliance and secure identity management

## Rationale
- The container architecture utilizes Go and serverless AWS components to guarantee sub-50ms P99 latency and high availability under a 25,000 EUR monthly budget.
- Strict isolation, encryption, and audit mechanisms satisfy PCI-DSS Level 1 compliance and 7-year auditability while remaining maintainable by a 3-engineer team.