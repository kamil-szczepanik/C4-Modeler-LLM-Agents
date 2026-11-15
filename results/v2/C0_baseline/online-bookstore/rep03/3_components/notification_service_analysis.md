## Overview
The Notification Service is a dedicated Node.js microservice running on AWS ECS Fargate that processes asynchronous domain events to deliver multi-channel alerts. It ensures GDPR/CCPA compliance, secure external API integrations, and robust delivery tracking for the Online Bookstore.

## Key Elements
- Event Consumer Component: Node.js with AWS SQS SDK
- Preference Engine Component: Node.js with Memory Cache and Amazon Aurora PostgreSQL
- Dispatcher Router Component: Node.js
- Template Engine Component: Node.js with Handlebars and MJML
- Provider Integration Adapters: Node.js with Axios
- Webhook Receiver Component: Node.js with Express and Amazon ElastiCache Redis
- External Services: SendGrid, Twilio, Segment, Snowflake, Amazon SQS, Amazon CloudWatch

## Relationships
- Amazon SQS -> Event Consumer: Consumes asynchronous notification events [AMQP / Event Stream]
- Event Consumer -> Preference Engine: Evaluates user consent and communication settings [In-memory call]
- Preference Engine -> Dispatcher Router: Routes allowed messages [In-memory call]
- Dispatcher Router -> Template Engine: Renders localized message templates [In-memory call]
- Template Engine -> Provider Integration Adapters: Sends formatted payloads [In-memory call]
- Provider Integration Adapters -> SendGrid/Twilio: Dispatches emails and SMS [REST / HTTPS]
- SendGrid/Twilio -> Webhook Receiver: Sends delivery status and engagement webhooks [REST / HTTPS via Amazon API Gateway]
- Webhook Receiver -> Segment/Snowflake: Streams engagement analytics [SDK / HTTPS]

## Technology Stack
- Node.js & Express: Core runtime and web framework for fast asynchronous processing
- AWS ECS (Fargate): Container orchestration for scalable and serverless service execution
- Amazon SQS & Amazon EventBridge: Asynchronous event ingestion with Dead Letter Queues (DLQ)
- Amazon Aurora PostgreSQL & Redis: Data persistence for user preferences and idempotency caching
- SendGrid & Twilio: Third-party providers for transactional email and SMS delivery
- AWS Secrets Manager & KMS: Secure credential storage and data encryption at rest

## Rationale
This architecture uses asynchronous event-driven queues and auto-scaling ECS Fargate tasks to handle high throughput without message loss. Security controls, HMAC webhook verification, and dedicated integration adapters ensure robust compliance, high availability (99.95%), and protection against third-party outages.