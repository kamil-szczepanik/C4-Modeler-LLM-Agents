## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations at 3,000 TPS to protect merchant revenue while supporting case reviews and compliance. It ensures sub-50ms P99 latency, PCI-DSS Level 1 compliance, and 7-year tamper-evident auditability within a €25k monthly budget managed by three engineers.

## Key Elements
- Payment Gateway / Core Processing System
- Fraud Analyst, Risk Manager, and Compliance & Audit Officer
- Real-Time Payment Fraud Screening System
- AWS Application Load Balancer (ALB) and ECS Fargate
- Dynamic Rule & Model Registry
- External Cardholder Data Environment (CDE) / Tokenization Vault
- AWS S3 Object Lock (WORM storage)

## Relationships
- Payment Gateway to ALB: Sends authorization requests via gRPC/REST over TLS 1.3 with mTLS and OAuth2/JWT validation.
- ALB to ECS Fargate: Forwards traffic with persistent connection pooling while enforcing rate-limiting.
- Scoring Engine to External CDE: Resolves tokens via secure APIs, ensuring raw PANs never enter application memory.
- Scoring Engine to Rule & Model Registry: Cryptographically validates and hot-loads signed rules via AWS KMS.
- System to AWS S3 Object Lock: Writes decision inputs, model versions, and explanations to append-only storage.
- Users to System: Interact via secure HTTPS Web UI and internal reporting tooling.

## Technology Stack
- AWS ECS Fargate: Container execution managed to avoid Kubernetes overhead and stay within budget.
- AWS Application Load Balancer (ALB): Handles high-throughput ingress at 3,000 TPS while maintaining low P99 tail latency.
- AWS S3 Object Lock & KMS: Provides WORM-compliant tamper-evident storage for 7-year auditability and cryptographic signature verification.
- AWS X-Ray: Implements distributed tracing to isolate bottlenecks and enforce the 50ms latency SLA.

## Rationale
This architecture leverages serverless-adjacent managed containers and externalized PCI boundaries to minimize operational burden for a three-engineer team. It guarantees high availability and strict SLAs within financial constraints while strictly isolating sensitive cardholder data.