## Overview
[A secure, scalable background worker service component processing asynchronous tasks and third-party integrations for the global e-commerce platform.]

## Key Elements
* Queue Consumer Component (TypeScript, `aws-sdk`, `sqs-consumer`)
* Order Processing Engine (TypeScript)
* Shipping Integrator Component (TypeScript, `axios`)
* Task Scheduler Component (TypeScript, `node-cron`, AWS EventBridge)
* Outbox Dispatcher Component (TypeScript)

## Relationships
* Queue Consumer Component -> Amazon SQS: Polls asynchronous jobs [HTTPS / IAM]
* Order Processing Engine -> Amazon Aurora PostgreSQL: Executes transactional database writes [PostgreSQL Wire Protocol / TLS]
* Shipping Integrator Component -> Shipping Provider APIs: Manages external API calls [REST/JSON over HTTPS with mTLS]
* Outbox Dispatcher Component -> Amazon SNS: Publishes domain events [HTTPS / IAM]
* Outbox Dispatcher Component -> Amazon Aurora PostgreSQL: Polls and clears outbox tables [PostgreSQL Wire Protocol / TLS]

## Technology Stack
* Node.js & TypeScript: Provides robust runtime and type safety for background processing.
* AWS ECS Fargate: Runs containerized workers without server management.
* Amazon SQS / SNS: Enables decoupled, asynchronous messaging with DLQs.
* AWS KMS & Secrets Manager: Secures sensitive data and rotates API keys.

## Rationale
[Isolating third-party integrations and utilizing transactional outbox patterns ensures resilience and 99.95% availability under high loads. Strict IAM roles and cryptographic controls enforce GDPR/CCPA compliance and OWASP mitigations.]