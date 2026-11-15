## Overview
[The system screens card-not-present payment authorizations for fraud in real-time, enabling analysts to review suspicious transactions securely. It utilizes an AWS-hosted architecture ensuring strict PCI-DSS compliance, sub-50ms latency, and 7-year auditability.]

## Key Elements
- Feature Data Engine (In-Memory KV Store)
- Rule & Model Cache
- Replication & Persistence Manager
- Session & Rate-Limiting Store
- Amazon ElastiCache Multi-AZ Redis
- Fraud Scoring Engine
- Case Management API
- AWS CloudWatch & AWS Secrets Manager

## Relationships
- Fraud Scoring Engine -> Feature Data Engine: In-memory feature retrieval [TCP / RESP over TLS]
- Fraud Scoring Engine -> Rule & Model Cache: Dynamic rule fetching [TCP / RESP over TLS]
- Fraud Scoring Engine -> Session & Rate-Limiting Store: Updates sliding-window transaction velocity counters [TCP / RESP over TLS]
- Case Management API -> Session & Rate-Limiting Store: Manages analyst session states [TCP / RESP over TLS]
- ElastiCache -> Amazon S3 Glacier: Archives automated daily encrypted snapshots [HTTPS]

## Technology Stack
- Amazon ElastiCache Multi-AZ Redis: Delivers low-latency feature lookups and rule caching with high availability.
- Redis Core Engine & Strings/JSON: Powers sliding-window aggregations and zero-downtime hot-reloading of scoring models.
- AWS KMS: Encrypts data at rest using customer-managed keys for PCI-DSS compliance.
- AWS Secrets Manager: Manages automated Redis AUTH token rotation.
- Amazon CloudWatch: Monitors ElastiCache performance metrics and audit logs.

## Rationale
[The architecture uses managed AWS services to minimize operational overhead for a three-engineer team while meeting strict budget limits. In-memory caching and encryption protocols ensure sub-50ms P99 latency and PCI-DSS compliance.]