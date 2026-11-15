## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and provides case management tools for analysts. It ensures high-performance, compliant, and auditable payment processing on AWS.

## Key Elements
* Payment Gateway / Acquirer and Fraud Analyst (Users/External Systems)
* AWS Network Load Balancer (AWS NLB) and Application Load Balancer (AWS ALB)
* Fraud Scoring Engine (Go/Rust on Amazon ECS on AWS Fargate)
* Case Management Backend (Go/Rust on Amazon ECS on AWS Fargate)
* Amazon Aurora PostgreSQL and Redis
* Amazon S3 with Object Lock and AWS KMS

## Relationships
* Payment Gateway / Acquirer -> AWS Network Load Balancer: Sends authorization requests at 3,000 TPS via HTTPS/TCP
* AWS Network Load Balancer -> Fraud Scoring Engine: Routes high-throughput scoring requests via TCP
* Fraud Analyst -> AWS Application Load Balancer: Accesses case management and rule updates via HTTPS
* Fraud Scoring Engine -> Amazon Aurora PostgreSQL and Redis: Queries data and caching via TCP
* Fraud Scoring Engine -> Amazon S3 with Object Lock and AWS KMS: Stores tamper-evident audit logs via AWS SDK/HTTPS

## Technology Stack
* AWS NLB & ALB: Selected for low-latency L4/L7 ingress routing without API Gateway overhead
* Amazon ECS on AWS Fargate: Container orchestration for cost-effective scaling within the €25,000 monthly budget
* Go / Rust: High-performance languages ensuring sub-50ms P99 latency
* Amazon Aurora PostgreSQL & Redis: Relational storage and fast state caching
* Amazon S3 with Object Lock and AWS KMS: Ensures 7-year tamper-evident auditability and PCI-DSS compliance

## Rationale
This architecture meets PCI-DSS Level 1 constraints and sub-50ms latency requirements by using direct L4/L7 load balancing and memory-efficient microservices. Serverless container infrastructure and managed AWS services respect the strict monthly budget while supporting a lean three-engineer operations team.