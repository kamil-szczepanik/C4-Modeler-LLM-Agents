## Overview
The system provides real-time fraud screening for card-not-present payment authorizations and case management for fraud analysts. It ensures sub-millisecond data retrieval and low-latency velocity checks to meet strict performance and PCI-DSS compliance mandates.

## Key Elements
- Velocity Counter Store (Redis HyperLogLog and Sorted Sets)
- Feature Cache (Pre-computed risk scores)
- Session State & Token Map (Transient risk session metadata)
- Go Fraud Scoring Engine (AWS ECS Fargate, Go, gRPC)
- Amazon ElastiCache Serverless (Redis)

## Relationships
- Go Fraud Scoring Engine -> Velocity Counter Store: Increments and reads counters via `RESP` protocol over TCP (TLS-encrypted)
- Go Fraud Scoring Engine -> Feature Cache: Fetches cached risk features via `RESP` protocol over TCP (TLS-encrypted)
- Go Fraud Scoring Engine -> Session State & Token Map: Resolves risk session tokens via `RESP` protocol over TCP (TLS-encrypted)

## Technology Stack
- Amazon ElastiCache Serverless (Redis): Provides automated scaling and low-latency in-memory operations to meet P99 < 50ms latency (R-04) and fit within the 25k EUR budget for a 3-engineer team.
- AWS KMS: Used for encryption-at-rest to ensure PCI-DSS compliance.
- Amazon CloudWatch: Monitors `EngineCPUUtilization`, slow logs, and audit logs for operational visibility and 7-year audit requirements (R-06).

## Rationale
This architecture uses serverless in-memory caching to eliminate operational toil for a small team while delivering sub-millisecond responses. Strict network isolation, TLS encryption, and tokenization satisfy PCI-DSS Level 1 constraints without breaching the strict monthly budget.