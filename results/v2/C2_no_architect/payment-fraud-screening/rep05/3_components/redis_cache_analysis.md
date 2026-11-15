## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud at 3,000 TPS while enabling analyst case reviews. It ensures strict PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a 25,000 EUR monthly AWS budget operated by three engineers.

## Key Elements
- Cardholders and Fraud Analysts (Users)
- Payment Gateway (External System)
- API Gateway (AWS ECS Fargate Container)
- Scoring Engine Container (AWS ECS Fargate Container)
- Case Management Container (AWS ECS Fargate Container, AWS Cognito)
- Amazon ElastiCache Redis OSS Multi-AZ Cluster (`cache.m6g.large`)
- S3 Glacier Object Lock Storage (AWS S3 Glacier, AWS KMS)

## Relationships
- Payment Gateway -> API Gateway: Forwards payment authorizations via HTTPS/TLS 1.3
- API Gateway -> Scoring Engine Container: Routes authorization payloads via internal gRPC
- Scoring Engine Container -> Amazon ElastiCache Redis Cluster: Queries fallback ruleset via Redis OSS protocol with TLS in transit
- Scoring Engine Container -> S3 Glacier Object Lock Storage: Persists immutable decision audit logs via AWS SDK / KMS

## Technology Stack
- AWS ECS (Fargate): Container orchestration minimizing operational overhead for a three-person team
- Amazon ElastiCache Redis OSS (`cache.m6g.large`): Provisioned multi-AZ caching ensuring deterministic sub-50ms latency and budget control
- AWS KMS & AWS Secrets Manager: Enforces encryption at rest (AES-256) and dynamic secret injection for PCI-DSS compliance
- AWS S3 Glacier with Object Lock: Provides tamper-evident 7-year audit retention

## Rationale
This architecture uses provisioned AWS managed services to guarantee predictable costs and deterministic sub-50ms P99 latency. Multi-AZ redundancy and a Redis fallback cache secure high availability and uptime requirements.