## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in real time to prevent fraud while enabling analysts to review suspicious transactions. It provides high-throughput, secure, and auditable fraud evaluation within strict financial and operational constraints.

## Key Elements
- Payment Gateways, Acquirers, and Merchant Platforms (External systems sending high-throughput traffic)
- Fraud Analysts and Risk Managers (Internal users accessing case management)
- AWS API Gateway HTTP API and AWS WAF (Ingress boundary, rate-limiting, and TLS termination)
- Scoring Engine Container (Go/Rust deployed on Amazon ECS)
- Case Management Container (Node.js/Python monolith on Amazon ECS)
- Amazon DynamoDB and Amazon ElastiCache (Redis) (Data layer)
- AWS SQS, SNS, CloudTrail, AWS Firehose, and S3 with Object Lock (Event and compliance infrastructure)

## Relationships
- Payment Gateway / Acquirer & Merchant Platforms -> AWS API Gateway: Forwards payment authorization requests [HTTPS/REST at 3,000 TPS]
- AWS API Gateway -> Scoring Engine Container: Invokes real-time fraud scoring [gRPC over HTTP/2]
- AWS API Gateway -> S3 (Audit Sink): Streams access logs asynchronously [AWS Kinesis Data Firehose with S3 Object Lock]
- Fraud Analysts -> Case Management Container: Reviews flagged transactions [HTTPS]

## Technology Stack
- AWS API Gateway & AWS WAF: Managed edge routing and DDoS protection to minimize operational toil for a 3-engineer team.
- Go/Rust on Amazon ECS: High-performance, low-latency execution for the Scoring Engine to meet the <50ms P99 SLA.
- gRPC over HTTP/2: Minimal serialization and network overhead for internal service-to-service communication.
- Amazon DynamoDB & ElastiCache (Redis): Low-latency data storage supporting high-throughput lookups within budget.
- Amazon S3 with Object Lock: Tamper-evident storage ensuring 7-year auditability compliance (R-06).

## Rationale
This architecture leverages managed AWS services to minimize operational overhead for a 3-engineer team while strictly maintaining a €25,000 monthly budget. High-performance technologies like Rust/Go and gRPC ensure P99 latency remains below 50 ms at 3,000 TPS.