## Overview
The Notification Worker is an asynchronous containerized system responsible for reliably dispatching transactional alerts and marketing notifications for the Online Bookstore. It ensures multi-currency localization and strict GDPR/CCPA compliance while meeting a <60-second delivery SLA.

## Key Elements
- Notification Worker Container (Node.js with TypeScript, Amazon ECS Fargate)
- Event Consumer Component
- Routing & Prioritization Component
- Preference & Consent Validator Component
- Localization & Template Engine Component
- Dispatcher Component
- Amazon SQS (Dual Queues: Transactional & Marketing, with Dead Letter Queue)
- Amazon DynamoDB (User preferences and consent storage)
- AWS Secrets Manager
- Email/Notification Service (External REST API)

## Relationships
- Amazon EventBridge -> Amazon SQS: Publishes domain events [HTTPS/SQS]
- Event Consumer -> Dual SQS Queues: Polls events asynchronously [HTTPS/SQS]
- Routing & Prioritization -> Preference & Consent Validator: Inspects and routes event payloads [In-memory typed interface]
- Preference & Consent Validator -> Amazon DynamoDB: Queries user opt-in and GDPR flags [HTTPS/TLS]
- Localization & Template Engine -> Email/Notification Service: Renders localized multi-currency content [In-memory]
- Dispatcher -> Email/Notification Service: Sends notifications via exponential backoff with circuit breaking [REST/TLS]

## Technology Stack
- Node.js with TypeScript: Chosen for rapid I/O handling, clean payload mapping, and low overhead.
- Amazon ECS (Fargate): Provides serverless container orchestration with dynamic autoscaling based on queue depth.
- Amazon SQS: Ensures resilient asynchronous message decoupling with queue-level isolation and DLQ support.
- Amazon DynamoDB: Offers low-latency access for real-time consent and preference validation.
- AWS Secrets Manager: Injects API keys securely at container startup without environment variables.

## Rationale
Dual SQS queues and ECS Fargate autoscaling physically guarantee the <60-second transactional SLA by preventing marketing traffic from blocking critical alerts. Zero-PII logging, strict IAM role boundaries, and consent validation ensure complete GDPR and CCPA compliance.