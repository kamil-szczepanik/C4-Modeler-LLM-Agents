## Overview
[The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations for a mid-size payment processor to detect fraud before approval, while providing case management for suspicious transactions.]
[It is built on AWS in eu-west-1, ensuring PCI-DSS Level 1 compliance, sub-50ms P99 latency at 3,000 TPS, and tamper-evident auditability.]

## Key Elements
* Fraud Analyst & Risk Manager (Users)
* Payment Gateway / Acquirer, Payment Network / Card Brands, Core Ledger (External Systems)
* AWS API Gateway (Ingress/TLS Termination)
* Go Scoring Engine Container on AWS ECS on Fargate
* Node.js Case Management Container on AWS ECS on Fargate
* Amazon SQS / EventBridge (Asynchronous Audit Stream)
* Amazon Aurora PostgreSQL Serverless v2 (Case State Database)
* AWS QLDB (Quantum Ledger Database)
* AWS Cognito & AWS Secrets Manager

## Relationships
* Payment Gateway to AWS API Gateway via HTTPS (TLS 1.3)
* API Gateway to Go Scoring Engine via gRPC over mTLS
* Go Scoring Engine to Amazon SQS / EventBridge via AWS SDK
* SQS to AWS QLDB for tamper-evident audit logging
* Node.js Case Management to Amazon Aurora PostgreSQL via TLS
* Fraud Analysts to Node.js Case Management via HTTPS (OAuth2/OIDC via AWS Cognito)

## Technology Stack
* AWS ECS on Fargate: Container orchestration to eliminate OS patching for a 3-person team
* Go (Golang): High-performance language for the real-time scoring engine to meet sub-50ms P99 latency
* Node.js (TypeScript): Rapid development framework for the case management API
* Amazon QLDB: Cryptographic ledger ensuring tamper-evident 7-year audit retention
* AWS Signer & ECS Blue/Green: Secure immutable container deployment for risk-free model updates

## Rationale
[This serverless and containerized AWS architecture meets strict PCI-DSS Level 1 and 7-year audit requirements using managed security services like AWS QLDB and Cognito.]
[It satisfies high-throughput, low-latency performance (3,000 TPS under 50ms) using Go on Fargate while remaining operable by a 3-person team within a €25,000 monthly budget.]