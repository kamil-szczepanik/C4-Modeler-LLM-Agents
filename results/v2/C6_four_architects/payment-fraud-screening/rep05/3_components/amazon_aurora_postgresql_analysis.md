## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages cases for fraud analysts. It runs on AWS in the `eu-west-1` region within a strict 25,000 EUR monthly budget.

## Key Elements
- Fraud Analyst (Person)
- Payment Gateway / Core Ledger, Card Schemes / Tokenization Provider, Identity Provider (IdP), Notification Service (External Systems)
- AWS ALB, Amazon CloudFront, React SPA, Amazon API Gateway (Edge & Frontend)
- Fraud Scoring Service, Case Management API (Amazon ECS Fargate Containers)
- Amazon ElastiCache (Redis), Amazon S3 Model Registry, Amazon SQS, AWS Lambda, Amazon S3 Object Lock, Amazon Aurora PostgreSQL, AWS Cloud Map (Data & Integration Containers)

## Relationships
- Fraud Analyst -> Amazon CloudFront / React SPA: Accesses case management dashboard via `[HTTPS/TLS]`
- API Gateway -> Fraud Scoring Service / Case Management API: Routes authorization and case requests via `[HTTP/2, gRPC]`
- Fraud Scoring Service -> Amazon ElastiCache Redis: Fetches cached card profiles and rules via `[TCP/TLS, Redis Protocol]`
- Case Management API -> Amazon Aurora PostgreSQL: Executes CRUD operations on cases via `[TCP/TLS, PostgreSQL Wire Protocol]`
- Audit Log & Replication Daemon -> Amazon S3 Object Lock: Exports immutable audit logs via `[HTTPS/TLS]`

## Technology Stack
- AWS ECS Fargate: Runs containerized microservices without server management overhead.
- Amazon Aurora PostgreSQL: Provides scalable, managed relational storage for cases and audit data.
- Amazon ElastiCache Redis: Delivers low-latency in-memory data caching for real-time scoring.
- ONNX Runtime: Executes machine learning models with high performance.
- Amazon S3 Object Lock: Ensures tamper-evident, 7-year retention compliance.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team. It guarantees high performance, strict PCI-DSS Level 1 compliance, and robust 7-year auditability within budget.