## Overview
The Library Management System is a comprehensive platform designed for public and academic libraries to catalogue items, manage circulation, and provide self-service patron portals. It adheres strictly to EU-only data residency requirements while ensuring high-performance search capabilities.

## Key Elements
*   **Users:** Library Patrons, Librarians, Library Administrators
*   **External Systems:** Payment Gateway, Notification Service, Digital Content Providers, Identity Provider (IdP)
*   **Frontend Container:** Web Application (SPA)
*   **Edge Container:** API Gateway
*   **Backend Containers:** Catalogue & Search Container, Circulation & Core Container, Notification & Payment Workers
*   **Infrastructure Containers:** PostgreSQL Database, Elasticsearch, RabbitMQ Message Broker

## Relationships
*   Library Patrons and Librarians interact with the Web Application SPA via HTTPS.
*   Web Application SPA communicates with the API Gateway via REST/GraphQL over HTTPS.
*   API Gateway routes internal traffic to backend containers using gRPC.
*   Circulation & Core Container communicates with RabbitMQ using AMQP.
*   Notification & Payment Workers integrate with external Payment Gateway and Notification Service.

## Technology Stack
*   **Web Application:** React and TypeScript, hosted on an EU-region CDN.
*   **API Gateway:** Nginx/Kong for TLS termination, JWT validation, and rate limiting.
*   **Search Engine:** Elasticsearch backed by Java/Spring Boot to meet sub-800ms search latency (R-05).
*   **Core Logic:** Node.js/Express for circulation business rules.
*   **Database:** PostgreSQL for transactional persistence with strict EU region-pinned volumes.
*   **Message Broker:** RabbitMQ in a high-availability cluster for asynchronous messaging.
*   **Background Workers:** Python/Celery utilizing dead-letter queues and circuit breakers.
*   **Observability:** OpenTelemetry for distributed tracing.

## Rationale
This architecture uses dedicated search and core containers with internal gRPC communication to easily satisfy the strict 99th-percentile search response time under 800 ms. Furthermore, region-pinned volumes and EU-hosted databases ensure complete compliance with the mandatory EU-only data residency constraints.