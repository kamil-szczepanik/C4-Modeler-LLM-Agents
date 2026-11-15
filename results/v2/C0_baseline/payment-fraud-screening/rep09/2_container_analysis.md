## Overview
[Real-Time Payment Fraud Screening System screens card-not-present payment authorizations for fraud and manages analyst reviews. It ensures PCI-DSS Level 1 compliance, explainable auditability, and <50ms P99 latency at 3,000 TPS within a €25,000 monthly AWS budget.]

## Key Elements
[Fraud Analyst, Risk Officer, Fraud Operations Manager, Payment Gateway, Identity Provider (IdP), SIEM / Compliance Archive, API Gateway (Envoy), Real-Time Scoring Engine (Go + ONNX on ECS Fargate), Case Management Backend, Web Application (React SPA), Audit Log Worker, Redis (ElastiCache), AWS Aurora PostgreSQL (Immutable Ledgers), Amazon SQS, AWS S3 / CloudFront]

## Relationships
[Payment Gateway to API Gateway via mTLS/HTTPS, API Gateway to Real-Time Scoring Engine via gRPC/HTTP2, Real-Time Scoring Engine to Redis via TCP/RESP, Real-Time Scoring Engine to Audit Log Worker via Amazon SQS, Audit Log Worker to AWS Aurora PostgreSQL via IAM-authenticated TLS, Web Application to Case Management Backend via REST/GraphQL over HTTPS, Case Management Backend to Identity Provider via OAuth 2.0 / OIDC]

## Technology Stack
[AWS ECS on Fargate for container orchestration with low operational overhead, Go and ONNX Runtime for high-performance stateless scoring, Node.js/Spring Boot for case management workflows, Redis (ElastiCache) for low-latency feature caching, AWS Aurora PostgreSQL with immutable tables for 7-year tamper-evident audit storage, React SPA on S3 and CloudFront for analyst UI, Terraform and GitHub Actions for zero-downtime GitOps deployments]

## Rationale
[This architecture separates high-throughput real-time scoring from human review workflows to meet strict P99 latency SLAs. Using managed AWS services and stateless containers optimizes operational simplicity for a three-engineer team while strictly enforcing PCI-DSS data boundaries.]