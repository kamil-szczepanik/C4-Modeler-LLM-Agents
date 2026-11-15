## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform for purchasing physical and electronic books with recommendations and reviews. It utilizes a resilient background processing architecture to handle asynchronous workloads, shipping integrations, and notifications.

## Key Elements
- **Event Consumer (AWS Lambda / Python)**: Polls message queues to process decoupled asynchronous tasks.
- **Shipping Integrator (Python / AWS SDK)**: Communicates with external shipping APIs for order fulfillment.
- **Notification Dispatcher (Python / AWS SDK)**: Dispatches transactional emails and alerts.
- **Outbox Processor (Python / AWS ECS task)**: Scans transaction tables to reliably publish domain events and prevent dual-write issues.
- **AWS SQS**: Asynchronous message queuing backbone.

## Relationships
- **Order & Checkout Database (RDS PostgreSQL)** -> **Outbox Processor**: Queries unpublished outbox events via `SQL/TCP`.
- **Outbox Processor** -> **Event Consumer**: Relays reliable message payloads via `AWS SQS`.
- **Shipping Integrator** -> **Shipping Provider API**: Submits fulfillment requests via `HTTPS (REST)`.
- **Notification Dispatcher** -> **Notification Service**: Dispatches alerts via `HTTPS`.

## Technology Stack
- **Python**: Core runtime for all background worker components to ensure rapid implementation and rich AWS SDK support.
- **AWS Lambda & AWS ECS**: Execution environments providing serverless and containerized scalability for tasks.
- **AWS SQS**: Message broker providing decoupled, fault-tolerant asynchronous communication.
- **PostgreSQL (RDS)**: Relational database utilizing the transactional outbox pattern for data consistency.

## Rationale
This event-driven component architecture decouples core checkout flows from third-party shipping APIs to guarantee at-least-once delivery. It directly supports the 99.95% availability target while mitigating data consistency risks in a distributed environment.