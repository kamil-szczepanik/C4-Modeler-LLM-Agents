## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud at scale and provides a case management interface for analysts. It operates within strict compliance, latency, and budget constraints on AWS.

## Key Elements
*   **Users:** Fraud Analyst, Risk Operations Manager, Compliance Auditor
*   **External Systems:** Merchant / Payment Gateway, External Identity Provider (IdP)
*   **Containers:** API Gateway (AWS API Gateway / ALB), Real-Time Scoring Engine (Go-based ECS Fargate), Case Management Backend & UI (React + Node.js/Python on ECS Fargate)
*   **Data & Storage:** Feature Store (Amazon ElastiCache Redis), Audit Log Storage (Amazon S3 with Object Lock and Amazon Athena)

## Relationships
*   Merchant / Payment Gateway to API Gateway via REST/HTTPS
*   API Gateway to Real-Time Scoring Engine via REST/HTTPS
*   Real-Time Scoring Engine to Amazon ElastiCache Redis via Redis Protocol
*   Real-Time Scoring Engine to Amazon S3 via S3 API (HTTPS)
*   Fraud Analysts to Case Management UI via REST/HTTPS

## Technology Stack
*   **Compute:** AWS ECS Fargate for lightweight, containerized microservices and UI hosting.
*   **Scoring & Rules:** Go for the Real-Time Scoring Engine with embedded in-memory rule evaluator and static ONNX model binaries.
*   **Caching:** Amazon ElastiCache (Redis) for sub-millisecond feature lookups.
*   **Audit & Compliance:** Amazon S3 with Object Lock paired with Amazon Athena for tamper-evident 7-year audit logs.
*   **Infrastructure & DevOps:** Terraform for Infrastructure as Code and automated CI/CD pipelines.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead, enabling a three-engineer team to maintain the system within the 25,000 EUR monthly budget. Go containers, embedded rules, and Redis ensure the strict P99 latency below 50 ms at 3,000 TPS.