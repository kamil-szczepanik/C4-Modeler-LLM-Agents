## Overview
[The Library Management System is a comprehensive solution providing cataloging, circulation, and self-service portals for academic and public libraries. It ensures EU-only data residency and meets strict performance SLAs.]

## Key Elements
- Library Patrons, Library Staff, Library Administrators
- Envoy Proxy, Web Application Container (React with NGINX)
- Catalogue Service (Spring Boot), Circulation & Loan Service (Node.js/Express)
- Notification Service Worker (Python FastAPI), Search Indexer (Elasticsearch)
- Databases: Catalogue DB, Circulation DB (PostgreSQL)
- Message Broker (RabbitMQ): Exchange Router, Persistence Store (Mnesia), Dead Letter & Retry Manager, Event Fanout Router
- External Systems: Enterprise Identity Provider, Payment Gateway, Notification Service

## Relationships
- Circulation & Loan Service -> Message Broker (Exchange Router): Publishes async loan/payment events [AMQP over TLS 1.3 with mTLS]
- Event Fanout Router -> Search Indexer: Forwards item check-in/out inventory updates [AMQP over TLS 1.3]

## Technology Stack
- RabbitMQ: Asynchronous messaging with quorum queues and TLS 1.3 node-to-node encryption
- PostgreSQL: Relational storage for catalogues and loans (EU-hosted)
- Elasticsearch: High-performance indexing ensuring 99th-percentile search < 800 ms
- Prometheus: Telemetry and monitoring for queue depth, consumer lag, and SLAs

## Rationale
[This architecture uses containerized microservices and an asynchronous message broker to guarantee high availability, strict EU data residency compliance, and rapid self-service portal response times. Decoupling services via RabbitMQ ensures fault tolerance during peak loads and payment gateway outages.]