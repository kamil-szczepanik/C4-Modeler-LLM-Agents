## Overview
The Online Bookstore uses an asynchronous event-driven messaging architecture to decouple core microservices while ensuring scalability and GDPR compliance. It handles high-throughput catalog searches, orders, and recommendations across multiple global AWS regions.

## Key Elements
- Topic Router (AWS SNS): Fan-out for domain events like `OrderPlaced` and `InventoryUpdated`
- Queue Dispatcher (AWS SQS): Durable point-to-point buffering for consuming services
- Dead Letter Queue (AWS SQS DLQ): Captures failed or poisoned messages after max retries
- Event Schema Registry (AWS EventBridge): Validates and versions event JSON schemas
- Idempotency Store (Amazon ElastiCache Redis): Handles deduplication for at-least-once delivery
- KMS (AWS KMS): Provides encryption keys for data-at-rest protection

## Relationships
- Microservices -> Event Schema Registry: Validates event structures prior to publishing [AWS SDK/HTTPS]
- Topic Router -> Queue Dispatcher: Forwards messages to subscribed queues [AWS SNS Subscription/JSON over HTTPS]
- Topic Router -> KMS: Encrypts and decrypts payloads at rest [AWS KMS API]
- Queue Dispatcher -> Microservices: Delivers buffered asynchronous events [AWS SQS Long Polling/AWS SDK]

## Technology Stack
- AWS SNS: Chosen for reliable pub-sub topic routing and fan-out
- AWS SQS (Standard/FIFO & DLQ): Selected for resilient, decoupled message queuing and failure isolation
- AWS EventBridge Schema Registry: Implemented to prevent schema drift and validate payloads
- AWS KMS: Utilized for envelope encryption to satisfy GDPR/CCPA PII requirements
- Amazon CloudWatch: Deployed for alarm-based monitoring of message visibility and throttling

## Rationale
This architecture guarantees 99.95% availability and sub-2-second performance by decoupling services asynchronously and preventing cascading failures via robust DLQ and retry mechanisms. Security controls, encryption, and strict PII minimization ensure full compliance with GDPR and CCPA regulations.