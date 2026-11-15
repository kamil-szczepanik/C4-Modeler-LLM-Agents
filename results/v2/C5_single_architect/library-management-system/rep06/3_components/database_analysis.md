## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures EU-only data residency and meets high-performance search requirements.

## Key Elements
- Patron, Librarian / Staff (Users)
- Payment Gateway, Notification Provider, Identity Provider, Digital Content Provider (External Systems)
- Web Application (SPA) (React, TypeScript, Nginx)
- API Gateway (Spring Cloud Gateway, Envoy)
- Core Domain Service (Java, Spring Boot)
- Search Service (Python, FastAPI, Elasticsearch)
- Async Event Broker (Apache Kafka)
- Background Worker (Python, Celery)
- Database (PostgreSQL)
  - Relational Data Store (PostgreSQL 15)
  - Connection Pooler (PgBouncer)

## Relationships
- Core Domain Service -> Connection Pooler: Executes transactions and queries [JDBC / TCP]
- Connection Pooler -> Relational Data Store: Forwards pooled queries [PostgreSQL Wire Protocol]
- Core Domain Service -> Database: Persists and queries data [JDBC]
- Search Service -> Async Event Broker: Consumes catalogue events [Apache Kafka protocol]

## Technology Stack
- PostgreSQL 15: Chosen for robust ACID compliance and secure relational persistence.
- PgBouncer: Selected to prevent thread exhaustion and manage connection spikes.
- Elasticsearch / Python FastAPI: Deployed for the Search Service to meet the <800 ms search latency requirement (R-05).
- Apache Kafka: Used for decoupled asynchronous event streaming.

## Rationale
This architecture isolates connection overhead and core transactional logic from search workloads, ensuring strict EU data residency compliance. The separation of PostgreSQL and Elasticsearch optimizes both relational integrity and fast catalog discovery.