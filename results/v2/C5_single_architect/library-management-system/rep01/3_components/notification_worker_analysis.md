## Overview
The Notification Worker is an asynchronous background component of the Library Management System responsible for decoupled notification processing. It ensures reliable, GDPR-compliant delivery of alerts to patrons and staff.

## Key Elements
* **Queue Consumer Component**: Node.js worker consuming background jobs.
* **Template Engine Component**: Handlebars-based rendering engine.
* **Compliance Sanitizer Component**: TypeScript-based PII masking engine.
* **Dispatcher Client Component**: Axios-based HTTP client.
* **Retry & Dead-Letter Handler Component**: Exception and backoff manager.

## Relationships
* Queue Consumer -> Template Engine: Passes raw event payloads [In-memory function call]
* Template Engine -> Compliance Sanitizer: Passes rendered payload [In-memory function call]
* Compliance Sanitizer -> Dispatcher Client: Sends sanitized payload [In-memory function call]
* Dispatcher Client -> Notification Service: Sends alerts [HTTPS]
* Queue Consumer -> Retry & DLQ: Handles processing exceptions [AMQP]

## Technology Stack
* **Node.js**: Lightweight runtime optimized for I/O-bound background processing.
* **amqplib**: AMQP protocol library for asynchronous queue consumption.
* **Handlebars**: Template engine for rendering localized messages.
* **Axios**: HTTP client for secure external dispatch.
* **TypeScript**: Provides type safety for compliance and PII sanitization.

## Rationale
This decoupled, event-driven architecture isolates the core domain from external delivery failures while ensuring strict adherence to EU data residency and privacy constraints.