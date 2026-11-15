## Overview
The Online Bookstore uses an asynchronous event-driven messaging backbone on AWS to decouple microservices, ensure high availability, and support 1 million monthly active users. It processes domain events across three target cloud regions while maintaining compliance with GDPR and CCPA regulations.

## Key Elements
- Event Bus (Amazon EventBridge): Central JSON-based event router for domain events.
- Event Rules & Targets (Amazon EventBridge Rules): Filters and routes events based on patterns.
- Event Archive & Replay (Amazon EventBridge Archive): Stores events for retention, auditing, and lineage.
- Order Processing Queue (Amazon SQS Standard/FIFO): Decouples services and buffers spike traffic.
- Dead Letter Queue (Amazon SQS): Captures poisoned or failed messages.

## Relationships
- Order & Checkout Service --(Publishes domain events via AWS SDK/HTTPS)--> Event Bus
- Event Bus --(Routes filtered events via EventBridge Rules)--> Order Processing Queue
- Event Bus --(Retains events for GDPR/CCPA audit)--> Event Archive & Replay
- Async Worker Service --(Polls via Long Polling / AWS SDK)--> Order Processing Queue
- Order Processing Queue --(Redrives poisoned messages)--> Dead Letter Queue

## Technology Stack
- Amazon EventBridge: Chosen as the central event bus for native rule-based routing and low-latency pub/sub mechanics.
- Amazon SQS: Selected for reliable message queuing, buffering, and long-polling capabilities under high load.
- Amazon SQS Dead Letter Queue: Implemented to isolate failed messages and ensure audit compliance.
- Amazon EventBridge Archive: Utilized for automated event retention to meet GDPR and CCPA compliance.

## Rationale
This event-driven architecture guarantees 99.95% availability and sub-2-second page loads by decoupling heavy transactions and safely buffering traffic spikes. Furthermore, built-in archiving and dead-letter queues satisfy stringent data privacy regulations and multi-region scalability constraints.