## Overview
The system screens card-not-present payment authorizations in real-time for fraud before approval and provides case management for analysts. It targets AWS eu-west-1, adhering to PCI-DSS Level 1 compliance and a 25,000 EUR monthly budget.

## Key Elements
- Fraud Operations Analysts & Risk Managers (Users)
- Payment Gateway / Merchant Systems (External System)
- Model Registry / Feature Store (External System)
- AWS Application Load Balancer (ALB)
- Scoring Engine Container (Rust, Axum, Tokio)
- Case Management Container (Python, FastAPI)
- Audit Logger Sidecar Container
- Amazon ElastiCache (Redis)
- Amazon Aurora Serverless v2
- Amazon S3 with Object Lock (Compliance Mode)

## Relationships
- Payment Gateway --[HTTPS / TLS 1.2+]-> AWS Application Load Balancer
- AWS Application Load Balancer --[HTTP / Internal VPC]-> Scoring Engine Container
- AWS Application Load Balancer --[HTTP / Internal VPC]-> Case Management Container
- Scoring Engine Container --[TCP / Redis Protocol]-> Amazon ElastiCache (Redis)
- Scoring Engine Container --[SQL / TLS]-> Amazon Aurora Serverless v2
- Audit Logger Sidecar Container --[HTTPS / AWS SigV4 via VPC Gateway Endpoint]-> Amazon S3 with Object Lock

## Technology Stack
- Rust with Axum & Tokio: High-performance scoring engine guaranteeing sub-50ms P99 latency.
- Python with FastAPI: Rapid development framework for analyst case management workflows.
- Amazon Aurora Serverless v2: Auto-scaling relational storage for transactional data within budget.
- Amazon ElastiCache (Redis): In-memory data store for low-latency feature and rule retrieval.
- Amazon S3 with Object Lock (Compliance Mode): Tamper-evident, 7-year retention storage for immutable audit logs.
- AWS KMS: Customer managed keys providing envelope encryption (SSE-KMS) for data protection.

## Rationale
The architecture combines high-throughput, low-latency Rust services with cost-effective serverless storage to meet performance and strict 25,000 EUR budget constraints. Immutable S3 storage and strict VPC boundaries fulfill PCI-DSS Level 1 and 7-year audit requirements for a three-engineer team.