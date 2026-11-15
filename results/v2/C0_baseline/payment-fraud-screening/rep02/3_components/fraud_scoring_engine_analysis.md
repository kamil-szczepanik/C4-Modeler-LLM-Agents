## Overview
The Fraud Scoring Engine screens card-not-present payment authorizations in real-time to detect fraud while supporting analyst case reviews. It balances strict PCI-DSS compliance, explainability, and sub-50ms latency within a fixed infrastructure budget.

## Key Elements
- **API Gateway & Tokenization Proxy**: Java with Spring Cloud Gateway
- **Fraud Scoring Engine (Container)**: Java with Spring Boot, deployed on AWS ECS (Fargate)
- **Decision Orchestrator Component**: Spring Bean coordinating the request lifecycle
- **Feature Aggregator Component**: Java with Caffeine Cache
- **Rule Evaluation Component**: Drools / Java with DRL rule hot-reloading from local disk
- **Model Scoring Component**: ONNX Runtime for Java with local ONNX model hot-reloading
- **Decision Explanation Assembler Component**: Merges rule triggers and feature importance vectors
- **Audit Payload Assembler Component**: Appends cryptographic HMAC via AWS KMS
- **External Storage & Messaging**: Amazon DynamoDB, Amazon S3 with Object Lock, Amazon SQS

## Relationships
- **API Gateway & Tokenization Proxy -> Fraud Scoring Engine**: Fraud evaluation requests via gRPC over internal VPC security groups with mTLS
- **Decision Orchestrator -> Feature Aggregator, Rule Evaluation, Model Scoring**: In-process concurrent method calls
- **Decision Orchestrator -> Decision Explanation Assembler -> Audit Payload Assembler**: In-process method calls
- **Audit Payload Assembler -> Amazon SQS**: Asynchronous audit payload emission using AWS SDK
- **Fraud Scoring Engine -> Amazon S3**: Secure model and rule artifact synchronization via HTTPS with cryptographic SHA-256 signature verification

## Technology Stack
- **Java / Spring Boot / Spring Cloud Gateway**: Core language and framework for scalable microservices and API routing.
- **gRPC**: Low-latency communication protocol for internal service-to-service requests.
- **Drools**: Rule engine for executing compiled decision tables in memory.
- **ONNX Runtime for Java**: Lightweight machine learning model execution directly in native memory.
- **Caffeine Cache**: High-performance in-memory caching for low-latency feature aggregation.
- **AWS ECS (Fargate)**: Container orchestration with auto-scaling to support a three-engineer team limit.
- **Amazon S3 with Object Lock & Amazon DynamoDB**: Tamper-evident, long-term audit storage and metadata persistence.
- **AWS KMS**: Cryptographic key management for HMAC signing and encryption-at-rest.

## Rationale
This architecture uses in-memory execution (ONNX and Drools) and non-blocking asynchronous auditing via SQS to achieve sub-50ms P99 latency at 3,000 TPS within a 25k EUR budget. Strict cryptographic signing, mTLS, and AWS KMS integration ensure PCI-DSS compliance and 7-year tamper-evident auditability.