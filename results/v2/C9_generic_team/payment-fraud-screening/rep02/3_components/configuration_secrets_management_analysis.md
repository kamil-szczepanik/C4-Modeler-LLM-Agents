## Overview
The Configuration & Secrets Management component securely provides dynamic settings and sensitive credentials to the real-time payment fraud screening platform in AWS eu-west-1. It ensures zero-downtime rule updates, strict auditability, and sub-50ms decision latency within a fixed budget of 25,000 EUR per month.

## Key Elements
* AWS Systems Manager Parameter Store: Stores non-sensitive application configurations and feature flags.
* AWS Secrets Manager: Manages sensitive credentials and API keys with native AWS Lambda rotation.
* High-Performance Scoring Engine (AWS ECS on Fargate): Consumes and caches configurations locally in-memory.
* Git-Ops / Infrastructure-as-Code Pipeline: Acts as the single source of truth and enforces CI/CD schema validation.
* Amazon CloudWatch: Monitors cache age, fallback activation, and schema validation failure metrics.

## Relationships
* High-Performance Scoring Engine polls AWS Systems Manager Parameter Store and AWS Secrets Manager using HTTPS over AWS PrivateLink.
* Git-Ops Pipeline pushes validated configurations to AWS Systems Manager Parameter Store via AWS SDK / API.
* High-Performance Scoring Engine emits operational telemetry to Amazon CloudWatch via AWS SDK.

## Technology Stack
* AWS Systems Manager Parameter Store & AWS Secrets Manager: Chosen for secure separation of concerns and compliance with PCI-DSS Level 1.
* In-Memory Caching with TTL: Implemented in the scoring engine to prevent remote latency bottlenecks and guarantee P99 latency below 50 ms.
* Git-Ops / IaC (GitHub / GitLab CI): Selected to provide version control, automated schema validation, and traceability for a 3-engineer team.
* Amazon CloudWatch Metrics & Alarms: Utilized for automated observability of cache fallbacks and configuration health.

## Rationale
This architecture decouples remote configuration fetches from the hot scoring path via local caching, ensuring high performance and availability. It supports a 3-engineer team and strict PCI-DSS auditability through Git-Ops immutability and automated monitoring.