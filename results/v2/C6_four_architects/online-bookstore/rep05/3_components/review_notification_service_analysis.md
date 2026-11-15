## Overview
[The Review & Notification Service container handles customer reviews, ratings, and asynchronous notifications for the Online Bookstore.]
[It uses a modular NestJS architecture to process synchronous HTTP requests and asynchronous event queues efficiently.]

## Key Elements
• Review Controller: Exposes REST endpoints for review submission and retrieval.
• Review Service: Manages review business logic and domain event publishing.
• Moderation Service: Sanitizes review text using compliance checks.
• Review Repository: Encapsulates database access using TypeORM.
• Review Cache Component: Interfaces with Redis for caching top reviews.
• Notification Consumer: Processes background messages from message queues.
• Template Engine: Compiles localized notification templates using Handlebars.
• Notification Dispatcher: Sends emails via external notification APIs.

## Relationships
• API Gateway -> Review Controller [HTTPS / REST]
• Review Service -> Review Cache Component [Redis TCP/RESP protocol]
• Review Repository -> Aurora PostgreSQL Database [Native TCP/TLS]
• Notification Consumer -> Amazon SQS [Long Polling]
• Notification Dispatcher -> SendGrid/AWS SES [HTTPS / REST APIs]

## Technology Stack
• Node.js & NestJS: Chosen for modular architecture and dependency injection.
• TypeORM: Facilitates database mapping and persistence.
• Handlebars: Used for dynamic email and notification rendering.
• AWS SDK (v3): Integrates with cloud services like SES and SQS.
• Amazon Redis: Provides caching to meet low-latency goals.

## Rationale
[The component-level separation isolates synchronous HTTP review traffic from asynchronous event-driven notifications to ensure high scalability.]
[Utilizing caching and modular NestJS design directly supports performance and maintainability requirements under high loads.]