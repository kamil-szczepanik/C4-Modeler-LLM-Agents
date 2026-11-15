## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations for mid-size processors to prevent fraud before approval. It features an integrated case management dashboard for fraud analysts to review flagged transactions securely and efficiently.

## Key Elements
* Fraud Analysts
* Payment Gateway
* AWS API Gateway (with Circuit Breaker)
* Tokenization Proxy Container
* Modular Monolith Core Scoring Engine (AWS ECS Fargate)
* Case Management Service (AWS ECS Fargate)
* Amazon SQS Message Bus
* AWS S3 Object Lock & AWS S3 Glacier
* Configuration Validation Init Container (Container)
* AWS Distro for OpenTelemetry Sidecar

## Relationships
* Payment Gateway invokes AWS API Gateway using HTTPS/TLS 1.3 for real-time authorization scoring (R-01).
* AWS API Gateway communicates with Tokenization Proxy Container via internal gRPC to tokenize raw card data (R-05).
* Tokenization Proxy Container forwards sanitized requests to Modular Monolith Core Scoring Engine via internal gRPC.
* Modular Monolith Core Scoring Engine writes tamper-evident audit logs and model decisions to AWS S3 Object Lock using AWS SDK (R-06).
* Modular Monolith Core Scoring Engine enqueues asynchronous review cases to Amazon SQS Message Bus (R-02).
* Case Management Service consumes messages from Amazon SQS via polling for fraud analyst reviews (R-02).
* Configuration Validation Init Container validates read-only mounted configurations on startup using shared schemas before releasing the shared volume marker to the Modular Monolith Core Scoring Engine.

## Technology Stack
* AWS ECS Fargate: Chosen for container orchestration to maintain a fixed infrastructure budget under 25,000 EUR per month.
* Python / Pydantic (or JSON Schema): Utilized within the Configuration Validation Init Container for lightweight, schema-driven validation.
* AWS S3 Object Lock: Implemented for tamper-evident storage to satisfy the 7-year regulatory auditability constraint (R-06).
* AWS Distro for OpenTelemetry: Deployed as a sidecar for distributed tracing and performance monitoring to meet P99 latency targets under 50 ms (R-04).
* gRPC: Selected for low-latency internal container-to-container communication.

## Rationale
This architecture uses serverless container infrastructure on AWS ECS Fargate to strictly adhere to the 25,000 EUR monthly budget while operating with a lean three-engineer team. Security and compliance controls—such as tokenization proxies, read-only configuration mounts, and immutable S3 storage—ensure full PCI-DSS Level 1 compliance and immutable 7-year auditability.