## Overview
[The Notification Container is a cloud-native microservice responsible for dispatching asynchronous order updates, shipping notifications, and alerts while ensuring strict GDPR/CCPA compliance and high availability across global AWS regions.]

## Key Elements
- Book Buyer & Author/Publisher Partner
- Notification Container (Amazon ECS/EKS)
- AWS SQS / SNS (Regional Message Queues & Topics)
- Amazon ElastiCache / Redis (Consent & Preference Cache)
- AWS KMS & AWS Secrets Manager
- Third-Party Shipping & Notification APIs

## Relationships
- Checkout/Payment Container -> Notification Container: Publishes cryptographically signed messages [AWS SNS/SQS]
- Notification Container -> Amazon ElastiCache/Redis: Validates real-time user consent [TCP/In-Memory]
- Notification Container -> Third-Party Shipping APIs: Dispatches fulfillment updates and alerts [HTTPS / TLS 1.3]
- Notification Container -> AWS Secrets Manager: Fetches dynamic provider API credentials [AWS API]

## Technology Stack
- Amazon ECS/EKS: Orchestrates containerized notification workers with auto-scaling based on SQS queue depth
- AWS SQS/SNS: Manages asynchronous message delivery with Dead Letter Queues (DLQ) for fault tolerance
- Amazon ElastiCache (Redis): Provides low-latency caching for real-time user preference validation
- AWS KMS & AWS Secrets Manager: Secures PII encryption at rest and dynamic credential management
- AWS X-Ray / OpenTelemetry: Enables distributed tracing across event pipelines

## Rationale
[This decoupled architecture ensures 99.95% uptime and high scalability to handle bursty traffic without degrading performance. Robust security controls, including PII encryption, least-privilege IAM, and strict egress filtering, guarantee OWASP and GDPR/CCPA compliance.]