## Overview
[System: Library Management System]
[Core Purpose: Catalogue items, manage circulation, and provide self-service portals with EU-only data residency and sub-800ms search performance.]

## Key Elements
- Asynchronous Broker (Redis)
- Event Publisher / Pub-Sub Engine (Redis Pub/Sub)
- Task Queue Manager (Redis Streams / Lists)
- Dead-Letter Queue (DLQ)
- Core Domain Service (Java/Spring Boot)
- Background Worker (Python/Celery)
- Web Application SPA (React/TypeScript)

## Relationships
- Core Domain Service -> Event Publisher: Publishes domain events [TCP/RESP3, mTLS]
- Core Domain Service -> Task Queue Manager: Enqueues background tasks with encrypted PII payloads [TCP/RESP3, mTLS]
- Task Queue Manager -> Background Worker: Dispatches tasks for consumption [TCP/RESP3, mTLS]
- Background Worker -> Task Queue Manager: Sends task acknowledgments (`XACK`) [TCP/RESP3, mTLS]
- Background Worker -> Dead-Letter Queue: Routes unprocessable poison-pill messages [TCP/RESP3, mTLS]

## Technology Stack
- Redis (Sentinel/Cluster): Chosen for high-availability event pub/sub and task queue management across EU zones
- Redis Streams (`XADD`/`XREADGROUP`/`XACK`): Ensures at-least-once task processing and zero data loss for self-service actions
- AOF Persistence & AES-256 / Field-Level Encryption: Balances data durability with strict GDPR compliance and EU data residency
- Mutual TLS (mTLS) & Redis ACLs: Secures data-in-transit and enforces strict least-privilege access control

## Rationale
[This architecture uses a resilient, secure Redis-based asynchronous broker with strict EU data residency and encryption controls to guarantee zero data loss and fault-tolerant self-service workflows.]
[Decoupling event publishing from durable task queues ensures high performance, compliance with GDPR regulations, and strict alignment with sub-800ms response requirements.]