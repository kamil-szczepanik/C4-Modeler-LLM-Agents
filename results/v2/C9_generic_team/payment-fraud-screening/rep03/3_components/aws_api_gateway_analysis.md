## Overview
The system screens card-not-present payment authorizations for fraud in real-time and provides case management for fraud analysts. It ensures sub-50ms decision latency at 3,000 transactions per second under strict PCI-DSS Level 1 compliance.

## Key Elements
- Payment Gateway
- AWS API Gateway
- Tokenization Proxy Container
- Modular Monolith Core Scoring Engine (AWS ECS Fargate)
- Case Management Service (AWS ECS Fargate)
- Amazon SQS Message Bus
- AWS S3 Object Lock and AWS S3 Glacier
- OpenTelemetry Sidecar Container
- Configuration Validation Init Container

## Relationships
- Payment Gateway -> AWS API Gateway: Sends payment authorization requests [HTTPS/TLS 1.3]
- AWS API Gateway -> Tokenization Proxy Container: Forwards payment data [gRPC/Protobuf]
- Tokenization Proxy Container -> Modular Monolith Core Scoring Engine: Sends tokenized payloads [gRPC/Protobuf]
- Modular Monolith Core Scoring Engine -> Amazon SQS Message Bus: Queues asynchronous review cases [AMQP/SQS Protocol]
- Case Management Service -> AWS S3 Object Lock: Stores immutable audit logs [HTTPS]

## Technology Stack
- AWS API Gateway: Manages external ingress, rate-limiting, and payload size restriction to protect downstream services within budget.
- AWS ECS Fargate: Hosts containerized core scoring and case management engines with minimal operational overhead.
- gRPC and Protobuf: Ensures high-performance, low-latency inter-container communication.
- Amazon SQS: Handles asynchronous message queuing and fallback processing to prevent payment blocking.
- AWS S3 Object Lock: Guarantees tamper-evident, 7-year auditability for regulatory compliance.

## Rationale
This architecture uses serverless edge routing and containerized microservices on AWS to achieve high-throughput, low-latency fraud screening within strict budget constraints. Automated infrastructure and lightweight protocols ensure compliance and reliability while remaining maintainable by a three-engineer team.