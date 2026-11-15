## Overview
The system is a real-time card-not-present payment fraud screening platform that evaluates payment authorizations and manages analyst reviews. It ensures high availability, PCI-DSS compliance, and sub-50ms decision latencies within a fixed infrastructure budget.

## Key Elements
- **Payment Gateway / Acquirer**: External entity submitting authorization requests.
- **Fallback Proxy Container**: Manages circuit breaking and fail-open policies.
- **Scoring Engine Container**: Stateless AWS ECS on Fargate service for real-time fraud evaluation.
- **Case Management & Admin Container**: Handles analyst workflows and rule updates.
- **Amazon S3**: Object storage with Object Lock for immutable audit logs and versioned model bundles.
- **Amazon Aurora Serverless**: Persistence layer for case data and audit trails.
- **AWS Systems Manager Parameter Store**: Centralized configuration and secrets management.

## Relationships
- Payment Gateway calls Fallback Proxy Container via HTTPS/REST.
- Fallback Proxy Container invokes Scoring Engine Container via gRPC / HTTP.
- Scoring Engine Container loads model bundles from Amazon S3 via HTTPS.
- Scoring Engine and Case Management Containers read configuration from AWS Systems Manager Parameter Store via AWS API.
- Case Management Container reads and writes audit data and cases to Amazon Aurora Serverless via TLS.
- Scoring Engine Container writes tamper-evident audit records to Amazon S3 via TLS.

## Technology Stack
- **AWS ECS on Fargate**: Container orchestration for low-overhead, serverless scaling within budget.
- **Amazon S3**: Immutable model storage and 7-year audit retention via Object Lock.
- **Amazon Aurora Serverless**: Relational database for case management with minimal operational overhead.
- **Protocol Buffers**: High-performance, deterministic binary serialization for low latency.
- **AWS Systems Manager Parameter Store**: Secure configuration and secrets injection.

## Rationale
The architecture prioritizes managed AWS services to minimize operational burden for a three-engineer team while meeting strict cost constraints. Decoupling stateless scoring compute from persistence and back-office workflows guarantees sub-50ms P99 latencies and high availability.