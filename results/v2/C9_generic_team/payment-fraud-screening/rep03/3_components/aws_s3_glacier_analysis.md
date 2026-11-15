## Overview
This system provides real-time fraud screening for card-not-present payment authorizations and case management for financial fraud analysts. It ensures sub-50ms latency scoring, PCI-DSS Level 1 compliance, and strict 7-year auditability within a fixed budget of 25,000 EUR per month in AWS `eu-west-1`.

## Key Elements
- Fraud Analysts (Users)
- Payment Gateway (External System)
- ML Training Environment (External System)
- AWS API Gateway with Circuit Breaker (Container)
- Tokenization Proxy Container (Container)
- Modular Monolith Core Scoring Engine on AWS ECS Fargate (Container)
- Case Management Service on AWS ECS Fargate (Container)
- Amazon SQS Message Bus (Container)
- AWS S3 Object Lock (Container)
- AWS S3 Glacier with S3 Lifecycle Policies (Container)
- AWS Distro for OpenTelemetry Sidecar Container (Container)
- Configuration Validation Init Container (Container)

## Relationships
- Payment Gateway to AWS API Gateway: Transmits payment authorization requests via HTTPS/TLS 1.3.
- AWS API Gateway to Tokenization Proxy Container: Forwards raw card payloads internally via gRPC.
- Tokenization Proxy Container to Modular Monolith Core Scoring Engine: Sends tokenized requests via internal gRPC.
- Modular Monolith Core Scoring Engine to Amazon SQS Message Bus: Publishes scoring decisions asynchronously via AWS SDK.
- Case Management Service to AWS S3 Object Lock: Stores immutable audit logs via AWS SDK.
- Case Management Service to AWS S3 Glacier: Transitions older audit payloads using S3 lifecycle rules and retrieves them via asynchronous restore jobs.

## Technology Stack
- AWS ECS Fargate: Chosen for container orchestration with zero server management overhead for a 3-engineer team.
- Amazon SQS: Selected for asynchronous decoupling of scoring decisions and case management within cost constraints.
- AWS S3 Object Lock & S3 Glacier: Deployed for tamper-evident, cost-effective 7-year audit retention.
- AWS KMS: Utilized for encryption at rest to satisfy PCI-DSS Level 1 compliance.
- AWS Distro for OpenTelemetry: Implemented for operational metrics and observability.

## Rationale
The architecture combines serverless containers and asynchronous queues to scale within a 25,000 EUR monthly budget while meeting strict sub-50ms latency targets. Immutable storage tiers and lifecycle policies guarantee PCI-DSS compliance and 7-year auditability without manual intervention from the small engineering team.