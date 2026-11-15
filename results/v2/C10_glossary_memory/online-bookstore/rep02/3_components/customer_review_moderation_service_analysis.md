## Overview
The Customer Review & Moderation Service processes, analyzes, and moderates customer feedback for the Online Bookstore platform. It ensures high data security and brand trust while maintaining low-latency ingestion through asynchronous message queues.

## Key Elements
- Review Ingestion API
- Review Moderation Queue
- Automated Moderation & Spam Filter
- Moderation Workflow & Analytics Engine
- Review Persistence Repository
- Content Moderator / Administrator
- Catalog / Quality Analyst
- Amazon SQS
- Amazon RDS

## Relationships
- Review Ingestion API -> Review Moderation Queue [AWS SDK]
- Review Moderation Queue -> Automated Moderation & Spam Filter [AWS SDK]
- Automated Moderation & Spam Filter -> Moderation Workflow & Analytics Engine [Internal Function Call]
- Moderation Workflow & Analytics Engine -> Amazon RDS [AWS SDK]

## Technology Stack
- Python/FastAPI: Chosen for native NLP and ML framework integration.
- AWS ECS on Fargate: Provides serverless container orchestration with auto-scaling.
- Amazon SQS: Decouples ingestion from CPU-intensive ML filtering.
- Amazon RDS: Provides persistent relational storage for reviews and metrics.
- AWS Secrets Manager / KMS: Encrypts queues and secures configuration.

## Rationale
This architecture decouples heavy NLP moderation tasks via SQS to protect system availability and performance targets. Strict IAM roles, JWT RBAC, and automated PII masking ensure full GDPR and CCPA compliance.