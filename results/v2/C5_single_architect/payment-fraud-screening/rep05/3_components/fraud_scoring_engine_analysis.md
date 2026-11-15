## Overview
The Fraud Scoring Engine is a high-performance system designed to screen card-not-present payment authorizations for fraud in real time. It enables sub-millisecond feature lookup, deterministic rule evaluation, and tamper-evident auditing within AWS eu-west-1.

## Key Elements
* API Handler Component (Go / Fiber)
* Feature Aggregator Component (Go)
* Scoring Engine Core (Rust)
* Audit Logger Component (Go)
* Rule & Model Loader Component (Rust)
* Redis
* Amazon Aurora PostgreSQL
* Amazon S3 with Object Lock and AWS KMS

## Relationships
* API Handler -> Feature Aggregator [In-process Function Call]
* Feature Aggregator -> Scoring Engine Core [In-process Function Call]
* Scoring Engine Core -> Audit Logger [Channel / Async Queue]
* Rule & Model Loader -> Scoring Engine Core [In-process Shared Memory / Atomic Swap]
* Feature Aggregator -> Redis [TCP]
* Scoring Engine Core -> Amazon Aurora PostgreSQL [TCP]
* Audit Logger -> Amazon S3 with Object Lock and AWS KMS [AWS SDK]

## Technology Stack
* Go / Fiber: Utilized for I/O-bound components to ensure high-throughput request handling.
* Rust: Chosen for CPU-bound scoring to meet strict performance and memory safety constraints.
* Redis: Provides low-latency storage for real-time feature lookups.
* Amazon Aurora PostgreSQL: Stores persistent transactional and case management data.
* Amazon S3 with Object Lock and AWS KMS: Ensures tamper-evident, 7-year compliant audit storage.

## Rationale
This architecture combines Go for efficient I/O processing and Rust for high-speed, memory-safe scoring to easily achieve the P99 latency target below 50 ms. Utilizing managed AWS services within a modular component structure ensures PCI-DSS Level 1 compliance and zero-downtime model updates within budget.