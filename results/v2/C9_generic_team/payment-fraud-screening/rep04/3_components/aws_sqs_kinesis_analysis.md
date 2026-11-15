## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud within strict performance and compliance constraints. It scores transactions in real time while asynchronously processing audit logs and case reviews for analysts.

## Key Elements
- Payment Gateway (External System)
- Fraud Analysts (Users)
- API Gateway / Ingress Container (OpenAPI / JSON Schema)
- Real-Time Scoring Container (AWS eu-west-1, gRPC/REST)
- Audit Logging Container (AWS)
- Case Management Container (AWS)
- AWS SQS FIFO (Asynchronous Event Bus)
- Amazon S3 with S3 Object Lock (Tamper-Evident Storage)
- AWS Secrets Manager / Parameter Store (AWS)

## Relationships
- Payment Gateway -> API Gateway / Ingress Container: Forwards authorization requests via HTTPS/REST
- API Gateway / Ingress Container -> Real-Time Scoring Container: Invokes scoring via gRPC
- Real-Time Scoring Container -> AWS SQS FIFO: Asynchronously dispatches decision events using `SendMessage`
- AWS SQS FIFO -> Audit Logging Container: Delivers decision events using `ReceiveMessage` and `DeleteMessage`
- Audit Logging Container -> Amazon S3: Stores audit records using AWS SDK with S3 Object Lock

## Technology Stack
- **Compute:** AWS ECS/Fargate for container hosting, chosen for minimal operational overhead for a 3-engineer team.
- **Messaging:** AWS SQS FIFO with S3 payload referencing, chosen to guarantee strict ordering, exact-once processing, and bypass 256 KB message limits.
- **Storage:** Amazon S3 with Object Lock, selected to enforce tamper-evident 7-year retention for PCI-DSS compliance.
- **Observability:** Amazon CloudWatch and AWS X-Ray, selected for tracking `OldestMessageAge` and distributed tracing under 50ms P99 latency constraints.
- **Infrastructure as Code:** Terraform/AWS CDK, chosen to prevent configuration drift and automate compliance deployments.

## Rationale
This architecture utilizes serverless managed AWS services to maintain high availability and PCI-DSS Level 1 compliance within a strict €25,000 monthly budget. Asynchronous decoupling via SQS guarantees sub-50ms P99 decision latencies while ensuring tamper-evident, auditable event logging operable by a three-engineer team.