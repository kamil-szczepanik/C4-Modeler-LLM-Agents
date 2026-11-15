## Overview
The system screens card-not-present payment authorizations for fraud in real time and provides a case management interface for analysts. It ensures PCI-DSS compliance, strict auditability, and high performance within a fixed infrastructure budget.

## Key Elements
- Fraud Analysts
- Payment Gateway
- ML Training Environment
- AWS API Gateway with Circuit Breaker
- Tokenization Proxy Container
- Modular Monolith Core Scoring Engine (AWS ECS Fargate)
- Case Management Service (AWS ECS Fargate)
- Amazon SQS Message Bus
- AWS S3 Object Lock
- AWS S3 Glacier
- AWS Distro for OpenTelemetry Sidecar Container
- Configuration Validation Init Container

## Relationships
- Payment Gateway -> AWS API Gateway: Submits authorization requests [HTTPS / REST]
- AWS API Gateway -> Tokenization Proxy Container: Forwards payment payloads [HTTP / JSON]
- Tokenization Proxy Container -> Modular Monolith Core Scoring Engine: Sends tokenized data [Internal HTTP / gRPC]
- Modular Monolith Core Scoring Engine -> Amazon SQS Message Bus: Asynchronously offloads audit payloads [AWS SDK / SQS API]
- Amazon SQS Message Bus -> AWS S3 Object Lock: Persists tamper-evident compliance logs [AWS SDK / S3 API]
- AWS S3 Object Lock -> AWS S3 Glacier: Transitions older audit logs via lifecycle policies [S3 Lifecycle]
- Fraud Analysts -> Case Management Service: Reviews suspicious transactions [HTTPS / REST]

## Technology Stack
- AWS ECS Fargate: Runs containerized services without server management to fit the 3-engineer team constraint
- Amazon SQS: Buffers audit logs asynchronously to protect the critical 50 ms payment path
- AWS S3 Object Lock (Compliance Mode): Enforces immutable, tamper-evident 7-year audit retention for PCI-DSS
- AWS S3 Glacier: Reduces long-term storage costs to meet the 25,000 EUR monthly budget
- AWS KMS: Encrypts audit logs with customer-managed keys and automated annual rotation

## Rationale
This architecture decouples non-critical compliance logging from the low-latency payment path using asynchronous SQS buffering. It satisfies strict 7-year immutability and PCI-DSS mandates while maintaining operational simplicity for a three-engineer team within budget.