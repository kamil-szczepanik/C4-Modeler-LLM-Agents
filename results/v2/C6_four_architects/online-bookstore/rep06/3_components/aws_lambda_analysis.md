## Overview
The Online Bookstore system is a scalable e-commerce platform for purchasing physical and electronic books, featuring reviews and recommendations. It utilizes a serverless event-driven architecture on AWS to handle asynchronous processing, compliance, and asset management.

## Key Elements
- Order Confirmation Processor (Node.js/TypeScript)
- Shipping Webhook Handler (Node.js/TypeScript)
- Data Anonymizer (Python 3.11)
- Audit Log Exporter (Python 3.11)
- Image Thumbnail Generator (Python 3.11)
- AWS API Gateway
- Amazon SQS / SNS
- Amazon EventBridge
- Amazon S3
- Amazon CloudWatch
- AWS Secrets Manager

## Relationships
- Third-Party Shipping API invokes Shipping Webhook Handler via AWS API Gateway using HTTPS
- Order Confirmation Processor subscribes to Amazon SQS / SNS via AWS SDK (SigV4)
- Data Anonymizer is scheduled via Amazon EventBridge to interact with Amazon Aurora PostgreSQL via AWS SDK (SigV4)
- Image Thumbnail Generator is triggered by Amazon S3 object-creation events using AWS SDK (SigV4)
- All components fetch credentials from AWS Secrets Manager and emit structured JSON logs to Amazon CloudWatch

## Technology Stack
- Node.js (TypeScript): Chosen for high-throughput asynchronous event processing and webhook handling.
- Python 3.11: Chosen for scheduled data anonymization, audit exporting, and image processing tasks.
- AWS Lambda: Serverless compute to absorb traffic spikes without idling ECS Fargate resources.
- AWS Secrets Manager: Secure credential retrieval at cold start to satisfy OWASP Top-10 security.
- Amazon CloudWatch: Centralized logging via stdout for observability and compliance.

## Rationale
This serverless component architecture isolates lightweight asynchronous workflows, webhooks, and compliance routines from core e-commerce services on ECS Fargate. It ensures strict adherence to GDPR, CCPA, and OWASP Top-10 constraints while scaling seamlessly to support 1 million MAU.