## Overview
[The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The Search Service container delivers sub-800ms item discovery with faceted filtering, typo tolerance, and real-time availability.]

## Key Elements
- Users: Library Patrons, Librarians, Library Administrators
- Containers: Web Frontend (React/TypeScript), API Gateway (Kong/Nginx), Search Service (Elasticsearch), Message Broker (RabbitMQ), Audit Logging Service (Go)
- Search Components: Query Parsing & NLP Component, Indexing & Synchronization Component, Search Execution Engine, Ranking & Aggregation Component, Analytics Publisher Component

## Relationships
- API Gateway -> Query Parsing & NLP Component: Routes search queries via internal REST/gRPC secured with mTLS
- Message Broker -> Indexing & Synchronization Component: Streams catalog updates via TLS-encrypted AMQP
- Indexing & Synchronization Component -> Ranking & Aggregation Component: Updates availability state via internal Java API
- Analytics Publisher Component -> Message Broker: Streams pseudonymized query analytics via AMQP

## Technology Stack
- Elasticsearch Core: Powers sub-800ms search execution and aggregations
- Lucene Query Parser / ES Analysis Modules: Implements fuzzy matching and autocomplete
- RabbitMQ / AMQP: Handles asynchronous catalog updates and analytics streaming
- AES-256: Secures data-at-rest for EU data residency compliance

## Rationale
[This architecture uses Elasticsearch and decoupled micro-components to meet stringent sub-800ms performance requirements while enforcing strict EU-only data residency, encryption, and RBAC controls. Asynchronous event processing ensures reliable real-time inventory updates and secure analytics generation.]