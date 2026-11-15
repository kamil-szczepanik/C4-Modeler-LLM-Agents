## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. Its Notification Worker container processes asynchronous notification events while strictly enforcing EU-only data residency constraints.

## Key Elements
*   **Notification Worker**: Node.js container for asynchronous message processing.
*   **Queue Consumer Component**: TypeScript and `amqplib` module for ingesting messages.
*   **Template Engine Component**: Nunjucks module for rendering localized message bodies.
*   **Data Sanitizer Component**: Custom TypeScript module for PII stripping.
*   **Dispatch Adapter Component**: Axios and Node.js HTTPS module for external integration.
*   **RabbitMQ**: Message broker container.
*   **Notification Service**: External system for final alert delivery.

## Relationships
*   Queue Consumer -> RabbitMQ: Consumes messages [AMQP]
*   Queue Consumer -> Template Engine: Passes raw payload [In-Memory Function Call]
*   Template Engine -> Data Sanitizer: Passes rendered payload [In-Memory Function Call]
*   Data Sanitizer -> Dispatch Adapter: Forwards sanitized payload [In-Memory Function Call]
*   Dispatch Adapter -> Notification Service: Delivers alerts [HTTPS/REST]
*   Notification Worker -> Notification Service: Dispatches alerts [AMQP/RabbitMQ]

## Technology Stack
*   **Node.js**: Chosen for lightweight, high-performance background worker tasks.
*   **TypeScript**: Ensures type safety across the notification processing pipeline.
*   **amqplib**: Protocol library for reliable RabbitMQ queue consumption via AMQP.
*   **Nunjucks**: Template engine for fast, localized message rendering.
*   **Axios / Node.js HTTPS**: Secure REST client for external API communication over TLS.

## Rationale
This architecture uses decoupled asynchronous messaging to meet performance requirements while isolating PII processing logic within EU boundaries. The modular component design ensures maintainability and strict compliance with EU-only data residency constraints.