## Overview
The Online Bookstore is an Amazon-style e-commerce platform for purchasing physical and electronic books with recommendations and reviews. The Email Service is a microservice managing transactional and notification emails for the platform.

## Key Elements
- **Email API Controller**: NestJS controller for synchronous REST triggers.
- **Event Consumer**: Background worker consuming asynchronous domain events.
- **Template Engine**: Component utilizing Handlebars or EJS for rendering localized email bodies.
- **Notification Preference Manager**: Component checking user communication opt-outs.
- **Email Dispatcher**: Service integrating with external email providers.
- **Email Audit Logger**: Component recording delivery metadata.
- **External Dependencies**: AWS API Gateway, Amazon SQS, Amazon DynamoDB, Amazon RDS (PostgreSQL), AWS SES / SMTP.

## Relationships
- **API Gateway -> Email API Controller**: Routes email notification triggers [HTTP].
- **Amazon SQS -> Event Consumer**: Delivers asynchronous events [SQS].
- **Event Consumer & Email API Controller -> Notification Preference Manager**: Validates user consent [In-memory].
- **Event Consumer & Email API Controller -> Template Engine**: Renders messages [In-memory].
- **Template Engine -> Email Dispatcher**: Sends rendered payloads [In-memory].
- **Email Dispatcher -> AWS SES / SMTP**: Delivers final emails [HTTPS / SMTP].
- **Email Dispatcher -> Email Audit Logger**: Persists delivery logs [TypeORM].
- **Email Audit Logger -> Amazon RDS (PostgreSQL)**: Stores audit metadata [SQL].
- **Notification Preference Manager -> Amazon DynamoDB**: Queries opt-out preferences [NoSQL].

## Technology Stack
- **Node.js & NestJS**: Chosen for modular microservice architecture and dependency injection.
- **Amazon ECS/Fargate**: Serverless container orchestration for scalability.
- **Handlebars / EJS**: Lightweight templating for localized email generation.
- **Amazon SQS & EventBridge**: Asynchronous message queuing for decoupling.
- **Amazon DynamoDB & PostgreSQL**: Data stores for preference tracking and audit logging.
- **AWS SES**: Reliable transactional email delivery via HTTPS/SMTP.

## Rationale
This component architecture uses asynchronous event-driven patterns with Amazon SQS to ensure high availability and non-blocking notification delivery. Integrating privacy checks via DynamoDB ensures strict GDPR and CCPA compliance.