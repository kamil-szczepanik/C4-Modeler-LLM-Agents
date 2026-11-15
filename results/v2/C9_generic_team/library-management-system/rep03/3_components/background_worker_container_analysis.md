## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It utilizes a resilient Background Worker Container to process asynchronous jobs while maintaining strict EU data residency and performance standards.

## Key Elements
* Background Worker Container: Processes asynchronous workloads independently.
* Message Broker Container: Queues and dispatches asynchronous messages.
* Configuration and Secrets Management Container: Provides dynamic runtime injection.
* EU-Hosted Observability Infrastructure: Collects metrics, traces, and structured logs.
* External Systems: High-Volume Publisher Feeds, Inter-Library Loan Networks, and Notification Gateways.

## Relationships
* Message Broker Container -> Background Worker Container: Triggers asynchronous job processing via Message Queue protocols using explicit ACK/NACK.
* Background Worker Container -> EU-Hosted Observability Infrastructure: Exports runtime metrics and W3C trace context headers.
* Background Worker Container -> External Systems: Communicates with rate-limiting and Circuit Breaker patterns.

## Technology Stack
* Idempotent Consumer Pattern & Dead Letter Queue (DLQ): Prevents data corruption and quarantines persistently failing jobs.
* W3C Trace Context & Structured JSON Logging: Enables distributed tracing and correlation across asynchronous boundaries.
* Circuit Breaker & Backpressure: Protects external dependencies and prevents cascading failures.
* Graceful Shutdown & Cancellation Tokens: Intercepts SIGTERM signals and enforces hard timeouts to preserve task state.

## Rationale
This architecture ensures high reliability and data integrity by decoupling heavy asynchronous processing from real-time workflows. Furthermore, strict isolation, payload validation, and boundary checks guarantee full compliance with EU data residency constraints.