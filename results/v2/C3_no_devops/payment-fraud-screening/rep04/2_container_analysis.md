## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud at scale while maintaining PCI-DSS Level 1 compliance. It provides sub-50ms latency scoring, case management for analysts, and immutable 7-year auditability.

## Key Elements
* Payment Processor (External System)
* Identity Provider (External System)
* AWS Application Load Balancer (Ingress)
* Scoring Engine (Stateless Go container on Amazon ECS on AWS Fargate)
* Case Management Backend (Node.js/TypeScript container on Amazon ECS on AWS Fargate)
* Auditor Query Service (AWS Athena over Amazon S3)
* Amazon DynamoDB (Feature lookups and case state)
* Amazon Aurora Serverless v2 PostgreSQL (Tamper-evident audit logs)
* Amazon SQS / SNS (Asynchronous messaging)

## Relationships
* Payment Processor to AWS Application Load Balancer via gRPC/HTTPS with mTLS
* AWS Application Load Balancer to Scoring Engine via HTTP/2
* Scoring Engine to Amazon DynamoDB via AWS PrivateLink
* Scoring Engine and Case Management Backend to Amazon Aurora Serverless v2 via TLS
* Compliance / Auditor to Auditor Query Service via HTTPS

## Technology Stack
* Go: Chosen for the Scoring Engine for optimal concurrency, low memory footprint, and sub-50ms P99 latency.
* Node.js/TypeScript: Used for the Case Management Backend to accelerate analyst workflow feature delivery.
* Amazon ECS on AWS Fargate: Selected to containerize workloads while minimizing operational overhead for a 3-engineer team within a 25k EUR/month budget.
* Amazon DynamoDB: Utilized for low-latency feature lookups and case state management.
* Amazon Aurora Serverless v2 PostgreSQL: Deployed with immutable append-only tables and AWS S3 Object Lock (Compliance Mode) for tamper-evident 7-year audit logging (R-06).

## Rationale
This architecture meets the 3,000 TPS and sub-50ms latency requirement using lightweight Go containers on ECS Fargate while staying within the 25,000 EUR budget through serverless and auto-scaling components. It satisfies strict PCI-DSS Level 1 and 7-year audit constraints via AWS PrivateLink, S3 Object Lock, and isolated managed data tiers suited for a 3-engineer team.