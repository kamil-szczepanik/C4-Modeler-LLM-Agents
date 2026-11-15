## Overview
[The system is a real-time payment fraud screening platform that processes card-not-present transactions for a mid-size payment processor. It scores authorizations in real-time, supports analyst case management, and ensures PCI-DSS compliance within strict latency, budget, and operational constraints.]

## Key Elements
* Payment Gateway / Processing Engine
* Fraud Analyst, Risk Manager / Data Scientist, Compliance & Audit Officer
* Amazon API Gateway and Application Load Balancer (ALB)
* Scoring Engine (AWS ECS Fargate on AWS Graviton2)
* Case Management UI & Backend (AWS ECS Fargate)
* Model Artifacts and Audit Logs Storage (Amazon S3)
* Ledger Database (AWS QLDB)
* Security and Management Services (AWS IAM, AWS Secrets Manager, AWS KMS, AWS CodePipeline, AWS CloudWatch & X-Ray, AWS GuardDuty)

## Relationships
* Payment Gateway -> Amazon API Gateway and ALB: Submits payment authorization requests [HTTPS, TLS 1.3]
* Amazon API Gateway and ALB -> Scoring Engine: Routes inbound traffic securely [Internal VPC protocols, mTLS with AWS ACM Private CA]
* Scoring Engine -> Model Artifacts and Audit Logs Storage: Downloads cryptographically verified ML model artifacts [HTTPS, TLS 1.3]
* Scoring Engine -> Ledger Database: Persists tamper-evident decision logs and feature weights [AWS KMS Encryption]
* Scoring Engine -> Model Artifacts and Audit Logs Storage: Persists decision logs and inputs into WORM storage [AWS KMS Encryption]
* AWS CodePipeline -> Scoring Engine: Deploys zero-downtime model updates and container rollouts [AWS ECS Deployment]

## Technology Stack
* AWS ECS Fargate on AWS Graviton2: Provides cost-optimized, scalable compute for ML inference within the €25k/month budget.
* Amazon S3: Stores immutable ML model artifacts and long-term audit logs with WORM capabilities.
* AWS QLDB: Provides tamper-evident, cryptographically verifiable ledger storage for 7-year auditability.
* AWS KMS: Enforces envelope encryption and cryptographic signing for non-repudiation of decision payloads.
* AWS CodePipeline: Automates zero-downtime deployments and canary rollouts for a 3-engineer team.
* AWS X-Ray and CloudWatch: Delivers distributed tracing to maintain sub-50ms P99 latency SLAs.

## Rationale
[This architecture guarantees sub-50ms P99 latency at 3,000 TPS while strictly enforcing PCI-DSS Level 1 compliance and a 7-year audit trail. By leveraging serverless containers, ARM-based Graviton2 instances, and automated fail-safes, it achieves high availability and rapid zero-downtime model iterations within a constrained 25,000 EUR monthly budget and a 3-engineer operational team.]