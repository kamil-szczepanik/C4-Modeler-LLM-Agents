## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud in under 50ms and manages cases for fraud analysts. It operates under strict PCI-DSS Level 1 compliance and a 7-year auditability constraint within a €25,000 monthly AWS budget.

## Key Elements
* Payment Gateway / Acquirer (External Partner)
* Tokenization Vault (External System)
* AWS API Gateway / ALB (Perimeter Security & Routing Container)
* Scoring Engine (Go/Rust, AWS ECS Fargate Container)
* Case Management API (AWS ECS Fargate Container)
* Rule & Model Registry (Amazon S3)
* Amazon DynamoDB & WORM Compliance Storage
* Fraud Analysts & Fraud Engineers (Internal Users)

## Relationships
* Payment Gateway / Acquirer -> AWS API Gateway / ALB: Sends pre-tokenized authorization requests [mTLS / HTTPS]
* AWS API Gateway / ALB -> Scoring Engine: Forwards scoring requests [gRPC / mTLS]
* Scoring Engine -> Rule & Model Registry: Fetches rules and models [HTTPS / S3 API]
* Scoring Engine -> WORM Compliance Storage: Stores tamper-evident audit logs [HTTPS]
* Fraud Analysts -> Case Management API: Reviews flagged cases [HTTPS / JSON]

## Technology Stack
* AWS API Gateway & ALB with AWS WAF v2: Perimeter security, mTLS termination, and JWT validation for low latency
* AWS ECS Fargate: Container orchestration matching a 3-engineer operational capacity
* Go / Rust: High-performance backend runtime for sub-50ms P99 latency requirements
* Amazon DynamoDB: Low-latency storage for real-time case management
* Terraform: Infrastructure as Code for automated, budget-compliant deployments

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while easily scaling to 3,000 requests per second. Strict perimeter mTLS, tokenization offloading, and immutable audit logs guarantee PCI-DSS Level 1 compliance and 7-year auditability within the €25k budget.