## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for academic and public libraries. It ensures EU data residency while maintaining sub-second search performance.

## Key Elements
* **Users:** Library Patrons, Librarians, Library Administrators
* **Gateways/Brokers:** API Gateway (Nginx/Kong), RabbitMQ Message Broker
* **Containers:** Web Application (SPA), Catalogue & Search Container (Java/Spring Boot), Circulation & Core Container (Node.js/Express)
* **Components:** Search Controller, Search Service, Index Repository, Cataloguing Event Consumer
* **Databases/External:** PostgreSQL Database, Elasticsearch Cluster, Identity Provider (IdP)

## Relationships
* API Gateway -> Catalogue & Search Container: Routes internal traffic [gRPC]
* Circulation & Core Container -> RabbitMQ Message Broker: Publishes item mutation events [AMQP]
* RabbitMQ Message Broker -> Catalogue & Search Container: Delivers item mutation events [AMQP]
* Catalogue & Search Container -> Elasticsearch: Queries search index and executes upserts [HTTP/REST over TCP]
* Catalogue & Search Container -> RabbitMQ Message Broker: Publishes search telemetry events [AMQP]

## Technology Stack
* **Frontend:** React and TypeScript (hosted on EU-region CDN)
* **Search Engine:** Elasticsearch (deployed as managed stateful cluster with EU data residency)
* **Backend Runtime:** Java/Spring Boot (Catalogue & Search), Node.js/Express (Circulation)
* **Messaging:** RabbitMQ (with Dead Letter Queues for fault tolerance)
* **Observability:** OpenTelemetry for distributed tracing and latency tracking

## Rationale
Separating the stateless Java/Spring Boot search application from the stateful Elasticsearch cluster enables independent scaling and meets the <800ms search latency SLA (R-05). Asynchronous event processing via RabbitMQ protects search performance while ensuring near-real-time index updates for librarians.