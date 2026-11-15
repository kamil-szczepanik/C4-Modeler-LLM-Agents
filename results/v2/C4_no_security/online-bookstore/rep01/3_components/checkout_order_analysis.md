## Overview
The Online Bookstore Checkout & Order component handles secure transactions, regulatory compliance, and order fulfillment. It ensures high availability and low latency for 1M MAU across multi-region AWS infrastructure.

## Key Elements
* Checkout Controller (Express.js router for API Gateway requests)
* Order Orchestrator (Core domain logic and state machine)
* Cart Manager (DynamoDB session and cart state handler)
* Fulfillment Publisher (AWS EventBridge/SQS event emitter)
* Order Repository (TypeORM-based PostgreSQL mapper)
* Consent Auditor (GDPR/CCPA compliance middleware)
* Payment Gateway Client (mTLS REST adapter with circuit breakers)

## Relationships
* Checkout Controller -> API Management: Receives HTTPS / JSON requests with JWT validation
* Cart Manager -> Amazon DynamoDB: Manages active shopping sessions over TCP
* Order Orchestrator -> Payment Gateway: Processes secure payments via HTTPS / REST with mTLS
* Fulfillment Publisher -> AWS SQS / AWS EventBridge: Publishes asynchronous events for shipping and tax
* Order Repository -> Amazon RDS (PostgreSQL): Persists transactional data via TLS-encrypted JDBC/TCP

## Technology Stack
* Node.js & TypeScript: Powers the core container for high-throughput I/O performance
* Express.js: Provides routing and middleware execution
* Amazon RDS (PostgreSQL): Stores transactional data with Multi-AZ and read replicas
* Amazon DynamoDB: Persists shopping carts and idempotency keys
* AWS SQS & EventBridge: Enables asynchronous messaging for shipping and compliance
* TypeORM: Maps domain entities to PostgreSQL

## Rationale
This architecture decouples transactional workflows from external API dependencies using asynchronous messaging and circuit breakers to guarantee 99.95% uptime. Dedicated components for consent auditing and payment integration ensure robust GDPR/CCPA compliance and financial transaction integrity.