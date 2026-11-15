## Overview
The Online Bookstore system is a scalable e-commerce platform for purchasing physical and electronic books, featuring reviews and recommendations. It utilizes an asynchronous, event-driven messaging architecture on AWS to handle high traffic and third-party integrations securely.

## Key Elements
* **EventBridge Ingress Gateway**: AWS EventBridge Target Configuration receiving domain events.
* **SNS Topic Router**: Amazon SNS (Standard/FIFO) for pub/sub event fan-out.
* **SQS Order Queue**: Amazon SQS (FIFO) for strict order and payment buffering.
* **SQS Integration Queue**: Amazon SQS (Standard) for outbound shipping tasks.
* **SQS Dead-Letter Queue (DLQ)**: Amazon SQS Standard/FIFO capturing failed messages.
* **SQS/SNS Access Policy Manager**: AWS IAM & KMS managing encryption and security.

## Relationships
* `Amazon EventBridge` -> `EventBridge Ingress Gateway` (Forwards events, HTTPS)
* `EventBridge Ingress Gateway` -> `SNS Topic Router` (Publishes payload, AWS Internal)
* `SNS Topic Router` -> `SQS Order Queue` (Publish/Subscribe, HTTPS)
* `SNS Topic Router` -> `SQS Integration Queue` (Publish/Subscribe, HTTPS)
* `SQS Order Queue` -> `Core E-Commerce Service` (Polls messages, SQS Protocol)
* `SQS Integration Queue` -> `Integration Service` (Polls messages, SQS Protocol)
* `SQS Order Queue` & `SQS Integration Queue` -> `SQS Dead-Letter Queue` (Fails over, AWS Internal)
* `SQS Dead-Letter Queue` -> `Audit & Compliance Service` (Consumes error logs, SQS Protocol)
* `SQS/SNS Access Policy Manager` -> `SNS Topic Router` & `SQS Integration Queue` (Secures & Encrypts, AWS IAM/KMS)

## Technology Stack
* **Amazon SNS**: Fan-out routing for decoupled domain events.
* **Amazon SQS (FIFO & Standard)**: Message buffering ensuring strict order processing and reliable integration handoffs.
* **AWS IAM & KMS**: Security governance for encryption-at-rest and in-transit to satisfy compliance mandates.
* **Amazon EventBridge**: Ingress event routing across microservices.

## Rationale
This event-driven architecture ensures high scalability and 99.95% availability by decoupling core services from third-party shipping APIs. Furthermore, dedicated DLQs and IAM/KMS encryption fulfill strict GDPR, CCPA, and OWASP Top-10 security requirements.