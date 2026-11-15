## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present transactions for a mid-size payment processor and manages analyst review workflows. Its core purpose is to block fraudulent authorizations with sub-50ms latency while ensuring strict PCI-DSS compliance and 7-year auditability.]

## Key Elements
- [Modular Monolith Core Scoring Engine (AWS ECS Fargate)]
- [Case Management Service (AWS ECS Fargate / AWS Lambda consumer)]
- [Amazon SQS Message Bus (Amazon SQS)]
- [AWS S3 Object Lock & AWS S3 Glacier]
- [OpenTelemetry Sidecar Container]

## Relationships
- [Modular Monolith Core Scoring Engine -> Amazon SQS Message Bus: Asynchronously routes review cases using Amazon SQS API]
- [Amazon SQS Message Bus -> Case Management Service: Triggers asynchronous case processing via SQS Long Polling]
- [Modular Monolith Core Scoring Engine & Case Management Service -> AWS S3 Object Lock: Persists immutable 7-year audit payloads via AWS SDK]

## Technology Stack
- [Amazon SQS: Provides transient decoupling and load-leveling with S3 Claims Check pattern for messages exceeding 256 KB]
- [AWS ECS Fargate: Runs core scoring and case management workloads with minimal operational overhead]
- [AWS S3 Object Lock: Ensures tamper-evident, WORM-compliant 7-year retention for auditability]
- [OpenTelemetry: Enables distributed tracing across asynchronous boundaries using traceparent context]

## Rationale
- [This architecture meets stringent performance and security requirements within a fixed budget and small team by leveraging managed AWS services. Asynchronous decoupling via SQS guarantees real-time scoring latency below 50ms while ensuring reliable downstream case management.]