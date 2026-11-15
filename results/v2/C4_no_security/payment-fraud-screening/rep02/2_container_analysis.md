## Overview
[The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud before approval and provides case management for analyst reviews. It ensures PCI-DSS Level 1 compliance, sub-50ms P99 latency at 3,000 TPS, and a 7-year tamper-evident audit trail within a €25,000 monthly AWS budget.]

## Key Elements
- [Fraud Analyst & Risk Manager (Users)]
- [Payment Gateway / Core Processing System (External System)]
- [API Gateway / Ingestion Service Container]
- [Real-Time Scoring Engine Container]
- [Case Management Backend Container]
- [Fraud Analyst SPA (React on Amazon S3 / CloudFront)]
- [Model/Rule Deployment Pipeline Container]
- [Compliance Export Container (AWS Lambda)]
- [Primary Operational Datastore (Amazon Aurora PostgreSQL Serverless v2)]
- [Audit & Feature Store (Amazon S3 with Object Lock)]

## Relationships
- [Payment Gateway to API Gateway / Ingestion Service via gRPC/REST over TLS]
- [API Gateway to Real-Time Scoring Engine via gRPC over TLS]
- [Fraud Analyst SPA to Case Management Backend via HTTPS/REST]
- [Case Management Backend to Amazon Aurora PostgreSQL via SQL over TLS]
- [Real-Time Scoring Engine to Amazon S3 Audit Store via AWS SDK / HTTPS]
- [Compliance Export Container to Amazon S3 Audit Store via Amazon Athena]

## Technology Stack
- [Go: Used for API Gateway to ensure minimal GC pauses and high concurrency for 3,000 TPS.]
- [Rust / Java with GraalVM: Powers Real-Time Scoring Engine for ultra-low latency sub-50ms P99 responses.]
- [Amazon ECS Fargate: Runs container workloads with auto-scaling based on CloudWatch gRPC queue metrics.]
- [Amazon Aurora PostgreSQL (Serverless v2): Manages transactional data within the €25k/month budget.]
- [Amazon S3 with Object Lock: Provides WORM-compliant, tamper-evident 7-year audit logging.]
- [ArgoCD (GitOps): Automates deployments for the 3-engineer team without manual intervention.]

## Rationale
[This architecture combines high-performance languages (Go, Rust/GraalVM) and serverless AWS infrastructure to meet strict sub-50ms latency and 3,000 TPS demands cost-effectively. Utilizing S3 Object Lock and Aurora Serverless ensures PCI-DSS compliance and a 7-year tamper-evident audit trail while keeping operational overhead minimal for a three-person engineering team.]