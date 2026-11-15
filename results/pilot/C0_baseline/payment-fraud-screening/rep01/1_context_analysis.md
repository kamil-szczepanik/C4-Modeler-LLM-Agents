## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud at 3,000 TPS within a sub-50ms P99 latency window and manages suspicious cases for human analysts. Operating under strict PCI-DSS Level 1 constraints, it ensures tamper-evident auditability and zero-downtime model updates.

## Key Elements
- **Merchant Integration Systems**: External clients submitting payment authorizations via gRPC/HTTPS.
- **Fraud Analysts**: Internal users reviewing flagged transactions via TLS.
- **Identity Provider**: External OIDC/IAM service for analyst Single Sign-On.
- **API Gateway / Network Load Balancer (NLB)**: AWS managed ingress terminating TLS and routing traffic.
- **Scoring Engine**: Containerized microservice processing real-time fraud scoring using cached rule sets.
- **Case Management Portal**: Web interface for analysts to investigate flagged transactions.
- **Audit Storage**: AWS S3 with Object Lock and KMS encryption for tamper-evident 7-year retention.

## Relationships
- **Merchant Systems to NLB**: Push payment authorizations via gRPC/HTTPS with mandatory mTLS and OAuth2/JWT validation.
- **Fraud Analysts to Case Management Portal**: Access review queues over TLS authenticated via OIDC.
- **Scoring Engine to Audit Storage**: Stream cryptographic hash-chained decision logs and inputs via AWS PrivateLink.
- **Scoring Engine to Tokenization Proxy**: Process ephemeral payment payloads to mask Primary Account Numbers (PAN).

## Technology Stack
- **AWS eu-west-1**: Target cloud provider delivering multi-AZ redundancy within a €25,000 monthly budget.
- **Amazon ECS/EKS on Graviton Instances**: Container orchestration utilizing cost-effective ARM-based processors for high-throughput scoring and case management.
- **Terraform**: Infrastructure-as-Code tool automating GitOps-driven zero-downtime deployments.
- **AWS KMS & S3 Object Lock**: Encryption and WORM storage ensuring PCI-DSS compliance and 7-year tamper-evident audit trails.
- **OpenTelemetry & Prometheus/Grafana**: Distributed tracing and metrics collection monitoring P99 latency.

## Rationale
The architecture prioritizes sub-50ms latency at 3,000 TPS by employing stateless scoring containers, AWS Graviton instances, and cached rule sets within a single AWS region. It strictly fulfills PCI-DSS Level 1 and 7-year audit mandates using cryptographic signing, AWS KMS encryption, and WORM-compliant S3 storage while remaining operable by a three-engineer team under a €25,000 monthly budget.