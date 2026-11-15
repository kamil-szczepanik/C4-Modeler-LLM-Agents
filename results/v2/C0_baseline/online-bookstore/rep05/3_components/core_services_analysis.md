## Overview
The Online Bookstore system is a scaled-down e-commerce platform that enables global users to browse catalogs, purchase physical and electronic books, and access reviews and recommendations. It delivers high scalability, strict compliance, and global availability across multiple AWS regions.

## Key Elements
- **Core Services Container**: Node.js/NestJS application running on Amazon ECS (Fargate).
- **Catalog & Search Component**: Handles product discovery and catalog queries via NestJS modules.
- **Cart & Checkout Component**: Manages shopping carts, multi-currency conversion, and payment orchestration.
- **User & Compliance Component**: Enforces GDPR/CCPA data access, audit logging, and profile management.
- **Inventory Reservation Component**: Manages decoupled, eventual consistency inventory locks via Amazon SQS.
- **Outbox Dispatcher Component**: Publishes reliable transactional events from the database outbox table.
- **Databases & Storage**: Aurora PostgreSQL (Multi-AZ with global read replicas) and Amazon KMS.

## Relationships
- **Core Services -> Aurora PostgreSQL**: Reads and writes transactional data [TCP/TLS with IAM DB Auth]
- **Cart & Checkout Component -> Tax & Compliance Service**: Calculates taxes and validates payments [REST/TLS with circuit breakers]
- **Outbox Dispatcher Component -> Amazon EventBridge**: Publishes asynchronous domain events [Async Event Publishing (JSON)]
- **Inventory Reservation Component -> Amazon SQS**: Processes asynchronous inventory locks [AMQP/HTTPS]

## Technology Stack
- **Node.js / NestJS**: Framework for building modular, maintainable microservices within Core Services.
- **Amazon ECS (Fargate):** Serverless container orchestration ensuring secure, elastic scaling.
- **Aurora PostgreSQL:** Relational database providing transactional integrity and global replication.
- **Amazon SQS & EventBridge:** Messaging and event streaming to decouple asynchronous workflows.
- **AWS KMS & Secrets Manager:** Application-level envelope encryption for PII and automated credential rotation.

## Rationale
This architecture uses modular NestJS components and serverless ECS Fargate containers to easily scale up to handle 1 million MAU without performance degradation. Decoupled asynchronous messaging with Amazon SQS and outbox patterns ensures 99.95% availability while robust encryption and IAM DB Auth satisfy strict GDPR/CCPA compliance.