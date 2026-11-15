## Overview
The system provides real-time fraud screening for card-not-present payment authorizations and case management for fraud analysts. It ensures sub-50ms decision latency, PCI-DSS compliance, and tamper-evident auditing within a strict budget.

## Key Elements
- Fraud Analyst & Risk Manager (Users)
- API Gateway (AWS API Gateway / ALB)
- Scoring Engine Container (Go/Rust on Amazon ECS)
- Case Management Container (Node.js/Python Monolith on Amazon ECS)
- Data Layer (Amazon DynamoDB & Amazon ElastiCache for Redis)
- Audit Ledger & Compliance (Amazon QLDB / CloudTrail Lake & AWS S3 Glacier)

## Relationships
- Scoring Engine & Case Management -> Data Layer: Fetches rules, models, and case data via HTTPS/TLS 1.3 using AWS SDK and IAM SigV4
- Data Layer -> Audit Ledger: Exports immutable transaction inputs, model versions, and decisions via native AWS event streaming
- Audit Ledger -> Amazon S3 Glacier: Archives compliance records for 7-year retention via lifecycle policies

## Technology Stack
- Amazon DynamoDB: Single-table design with Point-in-Time Recovery for transactional feature and case storage
- Amazon ElastiCache for Redis OSS: In-memory cache for low-latency rule and model weight retrieval
- Amazon QLDB / CloudTrail Lake: Native tamper-evident logging to satisfy 7-year auditability without custom toil
- Amazon S3 Glacier: Cold storage tier for long-term audit log archival within budget

## Rationale
This architecture uses managed AWS services to guarantee stringent performance, 7-year auditability, and PCI-DSS compliance. Offloading operational toil to serverless and managed components keeps maintenance sustainable for a three-person engineering team under a 25,000 EUR monthly budget.