## Overview
The Case Management Service is a secure Node.js and TypeScript container that enables fraud analysts to review suspicious payment authorizations, execute bulk overrides, and submit rule feedback. It ensures strict PCI-DSS compliance and operational auditability without exposing raw card data.

## Key Elements
* Case API Controller (Node.js/Express)
* Case Business Logic & Orchestration Service (including Bulk Operation Processor)
* Card Masking / Tokenizer Integration Client
* Audit & Immutable Ledger Publisher
* Rule Feedback Publisher
* AWS Fargate, AWS Aurora PostgreSQL, Amazon SQS/Redis

## Relationships
* Fraud Analyst / Risk Manager -> Case API Controller: Interacts via HTTPS (Web UI) with OAuth2/OIDC authentication
* Case API Controller -> Case Business Logic: Invokes internal functions via TypeScript
* Case Business Logic -> AWS Aurora PostgreSQL: Persists case states via SQL/TLS
* Case Business Logic -> Amazon SQS/Redis: Queues asynchronous outbox messages
* Audit & Immutable Ledger Publisher -> Secure Audit Archive: Publishes signed audit logs via gRPC/HTTPS
* Rule Feedback Publisher -> Fraud Scoring Engine: Submits rule adjustment flags via gRPC/HTTPS
* Card Masking / Tokenizer Integration Client -> Payment Card Network / Tokenization Vault: Ingests tokenized references via HTTPS

## Technology Stack
* Node.js & TypeScript: Enables rapid UI-driven feature iteration for fraud analysts
* AWS Fargate: Hosts containers cost-effectively with auto-scaling to respect the 25,000 EUR monthly budget
* AWS Aurora PostgreSQL & Amazon Redis: Provides structured data persistence and asynchronous message queuing
* Zod / Joi: Enforces strict JSON schema validation on API inputs to prevent injection attacks
* AWS Secrets Manager: Manages automated rotation of database credentials and OIDC secrets

## Rationale
This architecture balances strict PCI-DSS Level 1 data minimization by excluding raw PANs from the Node.js memory space. It also ensures 7-year auditability and fault-tolerant asynchronous logging tailored for a three-engineer team.