## Overview
The system provides real-time fraud screening for payment authorizations and case management for analysts, operating within strict PCI-DSS Level 1 constraints. It ensures explainable, tamper-evident audit trails and high-performance decision making on AWS.

## Key Elements
- Ledger Database (AWS QLDB): Immutable transaction decision logs and feature weights.
- Scoring Engine (AWS ECS Fargate): Evaluates authorization requests at scale.
- Case Management UI & Backend (AWS ECS Fargate): Handles fraud analyst reviews and auditor reporting.
- Storage & Archival (Amazon S3): Long-term archival with Object Lock (WORM).
- Security Services (AWS IAM, AWS KMS, AWS CloudWatch): Access control, encryption, and monitoring.

## Relationships
- Scoring Engine -> Ledger Database: Persists immutable decision logs [AWS PrivateLink, TLS 1.3, IAM]
- Scoring Engine -> Amazon S3: Fetches model artifacts and stores historical data [HTTPS, AWS KMS]
- Case Management Backend -> Ledger Database: Executes read-only audit queries [IAM, PartiQL API]
- DevOps & Security -> CloudWatch: Monitors storage growth, throughput, and key policies [CloudWatch API]

## Technology Stack
- AWS QLDB: Tamper-evident ledger providing mathematical verification for 7-year auditability (R-06).
- AWS ECS Fargate: Container orchestration for low-latency scoring and case management within budget.
- Amazon S3 + Object Lock: Cost-effective long-term archival ensuring WORM compliance.
- AWS KMS: Customer-managed keys with automatic rotation for encryption at rest.

## Rationale
This architecture uses serverless and managed AWS services to guarantee strict PCI-DSS compliance, cryptographic auditability, and sub-50ms P99 latency. It balances strict financial security constraints with a fixed monthly infrastructure budget.