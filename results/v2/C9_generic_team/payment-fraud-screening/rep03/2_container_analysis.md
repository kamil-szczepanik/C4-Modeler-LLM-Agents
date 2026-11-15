## Overview
Real-Time Payment Fraud Screening system processes and evaluates card-not-present payment authorizations for fraud in real-time, while providing case management tools for fraud analysts. It operates in AWS eu-west-1, maintaining sub-50ms P99 latency and strict PCI-DSS Level 1 compliance.

## Key Elements
- Payment Gateway (External System)
- AWS API Gateway with Circuit Breaker
- Tokenization Proxy Container
- Modular Monolith Core Scoring Engine (AWS ECS Fargate)
- Case Management Service (AWS ECS Fargate)
- Amazon SQS Message Bus
- AWS S3 Object Lock (Immutable Audit Storage)
- AWS S3 Glacier (Archival Storage)
- OpenTelemetry Sidecar Container
- Configuration Validation Init Container

## Relationships
- Payment Gateway to AWS API Gateway via HTTPS/TLS 1.3
- AWS API Gateway to Tokenization Proxy via gRPC/Protobuf
- Tokenization Proxy to Core Scoring Engine via internal VPC network
- Core Scoring Engine to Amazon SQS for asynchronous case routing
- Amazon SQS to Case Management Service via polling
- Core Scoring Engine to AWS S3 Object Lock for tamper-evident audit logging
- OpenTelemetry Sidecar to monitoring backend via OTLP protocol

## Technology Stack
- AWS ECS with Fargate: Container orchestration chosen to minimize management toil for a 3-engineer team.
- Modular Monolith: Architecture pattern for the scoring engine to ensure sub-50ms latency and simplify zero-downtime deployments.
- Amazon SQS: Message queue for decoupling real-time scoring from asynchronous analyst case management.
- AWS S3 Object Lock: Immutable storage backend to satisfy 7-year tamper-evident audit constraints.
- AWS Distro for OpenTelemetry: Sidecar telemetry collection for monitoring P99 latency without affecting performance.
- OpenAPI / gRPC: Contract-first API definitions for robust service communication and schema enforcement.

## Rationale
This architecture uses serverless container orchestration on AWS ECS Fargate and a modular monolith to maximize performance and maintainability within a 25,000 EUR monthly budget and a 3-engineer team constraint. Decoupling asynchronous case management via Amazon SQS and implementing tokenization proxies ensures strict PCI-DSS compliance and sub-50ms P99 decision latency.