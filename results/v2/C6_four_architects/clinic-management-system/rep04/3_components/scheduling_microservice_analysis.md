## Overview
The Scheduling Microservice manages appointment creation, modification, and real-time resource clash checks within the Clinic Management System. It ensures high-throughput, low-latency concurrency, distributed locking, and strict HIPAA/GDPR compliance across a hybrid cloud environment.

## Key Elements
- API Handler (Go Router/gRPC): Manages incoming mTLS traffic from the API Gateway.
- Policy & Consent Evaluator (Go Middleware + Open Policy Agent): Enforces HIPAA/GDPR access controls.
- Scheduling Engine (Go Domain Logic): Implements core scheduling algorithms and conflict detection.
- Lock Manager Component (Redis Enterprise): Provides distributed locks via TCP/RESP to prevent double-booking.
- Calendar Synchronizer (Go Worker): Manages asynchronous event publishing using Go channels.
- Notification Dispatcher (Go Worker): Dispatches appointment confirmations and reminders.
- Data Access Layer (pgx): Manages connection pooling and executes transactional queries.

## Relationships
- API Handler -> Policy & Consent Evaluator: Intercepts requests for authorization [In-memory function/gRPC]
- Scheduling Engine -> Lock Manager: Acquires distributed locks [Redis RESP]
- Scheduling Engine -> Data Access Layer: Commits validated appointments [PostgreSQL wire protocol over TLS 1.3]
- Scheduling Engine -> Calendar Synchronizer: Emits domain events [Go Channels]
- Calendar Synchronizer -> Message Broker / Event Bus: Publishes CloudEvents [Apache Kafka]

## Technology Stack
- Go: Chosen for lightweight goroutines and high-throughput concurrency.
- Redis Enterprise: Selected for low-latency state caching and distributed locking.
- PostgreSQL / CockroachDB: Utilized for reliable ACID persistence.
- Open Policy Agent (OPA): Deployed as a sidecar for policy enforcement.
- Apache Kafka: Used for asynchronous event-driven messaging.

## Rationale
This architecture uses Go and Redis distributed locks to meet stringent low-latency resource clash checks and 99.99% availability targets in an active-active setup. Integrated policy evaluation and secure protocols ensure strict adherence to HIPAA and GDPR compliance mandates.