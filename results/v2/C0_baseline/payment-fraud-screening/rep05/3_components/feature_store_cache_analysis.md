## Overview
The Feature Store & Cache provides sub-millisecond feature lookups for the Real-Time Payment Fraud Screening system. It maintains aggregated user and card behavioral data to ensure high-performance fraud scoring.

## Key Elements
- Feature Retrieval API / Client Layer
- In-Memory Cache & Store
- Feature Ingestion Worker
- Amazon ElastiCache Redis (Standard Tier)

## Relationships
- Real-Time Scoring Engine -> Feature Retrieval API / Client Layer: Reads features via RESP over TCP (with TLS 1.3)
- Feature Ingestion Worker -> In-Memory Cache & Store: Writes feature updates asynchronously via Redis commands over TLS
- Feature Store & Cache -> AWS Secrets Manager: Fetches authentication tokens via AWS SDK (HTTPS)

## Technology Stack
- Amazon ElastiCache Redis: Chosen for sub-millisecond latency and high throughput within budget
- Redis ACLs: Enforces least-privilege read/write separation between services
- AWS KMS & TLS 1.3: Secures data at rest and in transit for PCI-DSS compliance

## Rationale
This architecture delivers P99 decision latency under 50 ms while maintaining strict PCI-DSS Level 1 compliance. It operates efficiently within budget limits for a lean engineering team.