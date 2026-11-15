## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud at 3,000 requests per second. It provides scoring, case management, and auditability while maintaining PCI-DSS Level 1 compliance.

## Key Elements
- Fraud Analysts (Users)
- Payment Gateway & ML Training Environment (External Systems)
- AWS API Gateway with Circuit Breaker
- Tokenization Proxy Container
- Modular Monolith Core Scoring Engine (AWS ECS Fargate)
- Case Management Service (AWS ECS Fargate)
- Amazon SQS Message Bus
- AWS S3 Object Lock & AWS S3 Glacier

## Relationships
- AWS API Gateway -> Tokenization Proxy Container: Forwards payment data via gRPC/Protobuf
- Tokenization Proxy Container -> Modular Monolith Core Scoring Engine: Sends tokenized payment data over Internal VPC Network

## Technology Stack
- AWS (eu-west-1): Cloud provider and region ensuring infrastructure reliability and cost control.
- gRPC / Protobuf: High-performance communication protocol for low-latency data transfer.
- AWS ECS Fargate: Serverless container orchestration minimizing operational overhead for a three-engineer team.
- Amazon SQS: Asynchronous message bus for decoupled processing.
- AWS S3 Object Lock & Glacier: Tamper-evident storage providing 7-year auditability.

## Rationale
The architecture combines AWS serverless containers and high-throughput gRPC communication to meet sub-50ms latency at scale within a fixed budget. Automated security controls and strict data tokenization ensure compliance while reducing operational complexity for a small engineering team.