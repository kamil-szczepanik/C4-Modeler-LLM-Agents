## Overview
The Scoring Engine Container processes real-time card-not-present payment authorizations to detect fraud within strict performance and budget constraints. It evaluates requests to return approval decisions and generates explainable audit trails while maintaining high availability.

## Key Elements
- **API Handler Component**: Go/Rust service terminating incoming HTTP/gRPC traffic from the AWS ALB.
- **Feature Assembler Component**: Enriches requests using ElastiCache Redis and the Tokenization/Vault Service.
- **Execution Core Component**: Evaluates rules and lightweight compiled scoring models in-memory.
- **Audit Dispatcher Component**: Asynchronously serializes tamper-evident audit payloads to Amazon SQS / Kinesis Data Firehose.

## Relationships
- **AWS ALB -> API Handler Component**: Forwards payment authorization requests [HTTP/gRPC]
- **Feature Assembler Component -> ElastiCache Redis**: Fetches cached rules and velocity checks [Redis Protocol]
- **Feature Assembler Component -> Tokenization / Vault Service**: Requests tokenized card references [Secure APIs]
- **Execution Core Component -> Audit Dispatcher Component**: Passes audit payloads asynchronously [In-memory Go channels / crossbeam]
- **Audit Dispatcher Component -> Amazon SQS / Kinesis Data Firehose**: Streams decision inputs and explanations [HTTP]

## Technology Stack
- **Go / Rust**: Provides sub-50ms P99 latency and high throughput for the Scoring Engine Container.
- **AWS ECS Fargate**: Serverless container orchestration fitting the 25,000 EUR monthly budget and 3-engineer team constraint.
- **Amazon ElastiCache Redis**: Delivers ultra-low latency in-memory data access for feature assembly and model caching.
- **AWS Secrets Manager & IAM**: Secures model weights and credentials with zero-plaintext configuration.

## Rationale
This component architecture isolates hot-path execution from asynchronous auditing to guarantee strict sub-50ms latency at scale. Using serverless containers and managed AWS services keeps operational overhead minimal for a three-person engineering team while ensuring PCI-DSS Level 1 compliance and 7-year auditability.