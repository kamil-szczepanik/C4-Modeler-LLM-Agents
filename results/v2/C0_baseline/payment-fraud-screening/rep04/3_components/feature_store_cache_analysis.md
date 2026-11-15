## Overview
[Feature Store & Cache] provides real-time, low-latency feature lookups and profile storage for the payment fraud scoring engine, ensuring sub-50ms transaction evaluations while maintaining strict PCI-DSS Level 1 compliance.

## Key Elements
* Feature Retrieval API / Router (Rust / Node.js)
* Hot Cache Layer (Amazon ElastiCache Serverless Redis)
* Historical Feature Store (Amazon DynamoDB on-demand)
* Cache Invalidation & Sync Worker (Rust)

## Relationships
* Scoring Engine -> Hot Cache Layer: Retrieves real-time aggregates and hot features via TCP / RESP with TLS 1.3
* Scoring Engine -> Historical Feature Store: Queries wider entity profiles via AWS SDK over HTTPS/2
* Audit & Streaming Pipeline -> Cache Invalidation & Sync Worker: Ingests feature/rule state updates via Amazon Kinesis Consumer (TCP/HTTP) in under 1 second

## Technology Stack
* Amazon ElastiCache Serverless Redis: Provides sub-millisecond hot feature retrieval with zero operational scaling toil to meet the R-04 performance SLA within budget
* Amazon DynamoDB on-demand: Stores historical entity profiles with automated point-in-time recovery (PITR) to satisfy reliability constraints without cluster sizing overhead
* AWS KMS: Encrypts data at rest using Customer Managed Keys with annual rotation to fulfill PCI-DSS Level 1 mandates
* AWS IAM: Enforces strict least-privilege access and database authentication to secure internal component boundaries

## Rationale
This architecture leverages serverless AWS primitives to minimize operational burden for a three-engineer team while easily sustaining 3,000 TPS under the 25,000 EUR monthly budget. Furthermore, strict VPC isolation, tokenization, and TLS 1.3 enforce necessary PCI-DSS security compliance and auditability.