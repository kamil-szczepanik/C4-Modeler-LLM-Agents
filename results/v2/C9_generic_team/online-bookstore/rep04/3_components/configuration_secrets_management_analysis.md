## Overview
The Online Bookstore is a scaled-down e-commerce platform designed to handle 1 million monthly active users while supporting multi-currency transactions and strict regulatory compliance. The architecture utilizes a secure, multi-region AWS cloud infrastructure to deliver high availability and performance.

## Key Elements
- Customers and Administrators/Content Moderators
- AWS S3, CloudFront, and API Gateway
- Docker containers on AWS ECS/EKS
- AWS Systems Manager Parameter Store and AWS Secrets Manager
- PostgreSQL, OpenSearch, and Redis Cache
- Third-Party Shipping APIs, Payment Gateway, and Notification Services

## Relationships
- Customers interact with SPA/SSR Frontend via HTTPS/TLS through AWS CloudFront and API Gateway
- Microservices retrieve configuration and secrets via internal Provider Interface (Adapter Pattern) interacting with AWS Systems Manager Parameter Store and AWS Secrets Manager
- Application containers connect to PostgreSQL, OpenSearch, and Redis Cache using secure TCP protocols

## Technology Stack
- **AWS Systems Manager Parameter Store**: Used for hierarchical, non-sensitive operational configurations with standard throughput and free tiers
- **AWS Secrets Manager**: Utilized strictly for sensitive credentials with AWS Lambda-driven automatic rotation
- **AWS KMS**: Provides region-scoped customer-managed encryption keys for data protection
- **Pydantic / JSON Schema**: Enforces strict startup schema validation with a fail-fast mechanism
- **OpenTelemetry**: Sidecars utilized for observability and telemetry tracking

## Rationale
This architecture ensures 99.95% availability and high performance through local configuration caching, stale-if-error fallback patterns, and decoupled dual-layer storage. Strict schema validation, automated secret rotation, and adapter pattern abstractions fulfill rigorous security, GDPR/CCPA compliance, and maintainability requirements.