## Overview
This system provides real-time fraud screening for card-not-present payment authorizations within a strict PCI-DSS Level 1 compliant architecture. It processes up to 3,000 authorizations per second while maintaining sub-50ms P99 latency and supporting zero-downtime model updates.

## Key Elements
- Fraud Analysts: Human users reviewing suspicious transactions via the admin UI.
- External Payment Gateway: Sends payment authorization requests and receives scoring decisions.
- API Gateway / Ingestion Service: Handles incoming REST/OpenAPI authorization traffic.
- Scoring Engine: Evaluates transactions using embedded ML models and rules.
- Case Management & Admin UI: Web interface for fraud analysts to review flagged transactions.
- AWS ECS with Fargate: Container orchestration platform hosting all microservices.
- Amazon SQS & Amazon S3 with Object Lock: Message queuing and tamper-evident audit storage.

## Relationships
- External Payment Gateway -> API Gateway / Ingestion Service: Forwards authorization requests via HTTPS/REST.
- API Gateway / Ingestion Service -> Scoring Engine: Delegates transaction payloads via gRPC/Protobuf.
- Scoring Engine -> Amazon S3 with Object Lock: Persists immutable decision inputs and model versions via AWS SDK.
- Fraud Analysts -> Case Management & Admin UI: Accesses review cases via HTTPS.

## Technology Stack
- AWS ECS with Fargate: Chosen for container orchestration to minimize operational overhead for a three-engineer team.
- Rust / Go / Java: Selected for core microservices to guarantee sub-50ms P99 performance at scale.
- AWS CodeDeploy & Terraform: Used for automated Blue/Green deployments and Infrastructure as Code to prevent configuration drift.
- AWS OpenTelemetry (ADOT) Sidecar: Implemented for decoupled metrics and distributed tracing without application latency overhead.

## Rationale
The architecture maximizes automation and uses serverless container orchestration to operate securely and reliably with a three-engineer team under a fixed 25,000 EUR monthly budget. AWS native services and strict latency optimizations ensure PCI-DSS compliance and sub-50ms performance without exceeding operational capacity.