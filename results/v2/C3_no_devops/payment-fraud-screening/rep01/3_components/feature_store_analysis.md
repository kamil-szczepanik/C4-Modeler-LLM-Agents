## Overview
The Feature Store component provides low-latency real-time and historical feature data to power sub-millisecond payment fraud screening. It ensures high availability and strict PCI-DSS compliance while supporting real-time model updates.

## Key Elements
* Feature API Handler (Go)
* Feature Aggregator (Go)
* Feature Cache (Redis Core)
* Feature Backfill Worker (Go)
* AWS ElastiCache for Redis
* Amazon RDS for PostgreSQL
* Amazon SQS

## Relationships
* Fraud Scoring Engine -> Feature API Handler: Fetches real-time features [gRPC / Low-latency TCP with mTLS]
* Feature Aggregator -> Feature Cache: Updates real-time features [Redis RESP over TLS]
* Feature API Handler -> Feature Cache: Reads feature values [Redis RESP over TLS]
* Feature Backfill Worker -> Amazon RDS for PostgreSQL: Queries baseline historical features [JDBC over TLS]
* Feature Backfill Worker -> Feature Cache: Seeds historical aggregates [Redis RESP over TLS]
* Feature Aggregator -> Amazon SQS: Consumes real-time payment events [AWS SDK over HTTPS]

## Technology Stack
* Go: High-performance concurrency for API handling, aggregation, and backfilling within strict latency budgets
* AWS ElastiCache for Redis: In-memory store providing sub-millisecond retrieval and AES-256 encryption at rest
* Amazon RDS for PostgreSQL: Durable relational storage for baseline historical features
* Amazon SQS: Message queue for processing real-time payment event streams
* gRPC & Redis RESP: Low-overhead binary protocols for internal component communication

## Rationale
This component architecture achieves P99 latency below 50ms using in-memory caching while maintaining PCI-DSS Level 1 compliance through rigorous data isolation and encryption. It operates reliably within a 25,000 EUR monthly budget and supports a three-engineer team via standard, maintainable Go worker patterns.