## Overview
[A real-time payment fraud screening system evaluates card-not-present transactions against security rules and machine learning models before approval, while providing a case management interface for fraud analysts.]

## Key Elements
- Fraud Analysts: Human reviewers managing flagged cases
- Cardholder / Merchant: Initiators of payment transactions
- Fallback Proxy Container (Envoy): Manages ingress, circuit breaking, fail-open policies, local blocklist heuristics, and data masking
- Scoring Engine Container (AWS ECS on Fargate): Evaluates fraud scoring models via gRPC / HTTP
- Case Management & Admin Container (AWS ECS on Fargate): Handles analyst workflows
- Amazon S3 (AWS S3 with Object Lock): Tamper-evident storage for 7-year audit logs
- Amazon Aurora Serverless (Amazon Aurora Serverless): Relational database for case management using TLS
- AWS Systems Manager Parameter Store (AWS SSM): Configuration and rule parameter storage

## Relationships
- Cardholder / Merchant -> Fallback Proxy Container: Submits authorization requests via HTTPS/REST
- Fallback Proxy Container -> Scoring Engine Container: Invokes fraud evaluation via gRPC / HTTP
- Fallback Proxy Container -> Amazon S3: Forwards asynchronous structured audit events via HTTPS
- Fraud Analysts -> Case Management & Admin Container: Reviews suspicious payments via HTTPS/REST

## Technology Stack
- Envoy: Core proxy technology selected for battle-tested resilience, native ExtAuthz/Lua filtering, and low resource overhead
- AWS ECS on Fargate: Container orchestration chosen to minimize infrastructure management for a 3-engineer team
- AWS Systems Manager Parameter Store: Centralized configuration management to ensure stateless deployments within budget
- Terraform / AWS CDK: Infrastructure as Code for maintaining reproducible, version-controlled environments
- Amazon S3 Object Lock: Immutable storage implementation ensuring compliance with the 7-year auditability constraint

## Rationale
[This architecture combines cloud-native managed services with resilient edge proxy patterns to maintain sub-50ms latencies and strict PCI-DSS compliance within a fixed budget. Automated testing and stateless proxy design ensure high availability and minimal operational overhead for a small engineering team.]