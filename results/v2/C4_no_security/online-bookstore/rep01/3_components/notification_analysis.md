## Overview
The Online Bookstore is a scaled-down, multi-region e-commerce platform designed to support 1 million monthly active users with high availability and GDPR/CCPA compliance. The Notification component manages asynchronous transactional messaging, such as order confirmations and shipping updates, across global AWS regions.

## Key Elements
- **Registered Customer & Store Administrator**: Primary users receiving transactional alerts and operational notifications.
- **Event Consumer Component**: Built with Java and Spring Boot to poll AWS SQS.
- **Priority Router Component**: Routes critical transactional payloads past bulk queues.
- **Template Engine Component**: Uses Handlebars.js for dynamic, localized message rendering.
- **Dispatch Adapter Component**: Integrates with Amazon SES and Amazon SNS.
- **Preference & Audit Repository Component**: Manages GDPR/CCPA compliance logging via Amazon RDS PostgreSQL.

## Relationships
- AWS SQS -> Event Consumer (AMQP/HTTPS polling)
- Event Consumer -> Priority Router (In-Memory Java method call)
- Priority Router -> Template Engine (In-Memory Java method call)
- Template Engine -> Dispatch Adapter (HTTPS REST API)
- Dispatch Adapter -> Amazon SES / Amazon SNS (HTTPS REST API)
- Event Consumer & Dispatch Adapter -> Preference & Audit Repository (JDBC over TLS)

## Technology Stack
- **Java / Spring Boot**: Chosen for the Event Consumer and database layers for robust enterprise reliability.
- **AWS SQS & DLQ**: Ensures decoupled, resilient asynchronous messaging with exponential backoff retries.
- **Amazon SES & Amazon SNS**: Scalable, managed services for email and SMS delivery.
- **Handlebars.js**: Enables lightweight, dynamic email and SMS templating.
- **Amazon RDS (PostgreSQL)**: Stores GDPR/CCPA user preferences and immutable audit logs securely.
- **Resilience4j & HikariCP**: Provides connection pooling and circuit breakers to prevent database exhaustion.

## Rationale
This architecture ensures 99.95% availability and high performance by decoupling notification delivery from core checkout flows using SQS. Multi-region redundancy, circuit breakers, and async audit logging protect system stability while strictly maintaining GDPR and CCPA compliance.