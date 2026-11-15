## Overview
The Library Management System provides a digital platform for public and academic libraries to catalogue items, manage circulation, and operate self-service portals. It ensures strict EU data residency and high-performance search capabilities.

## Key Elements
*   **Web Application**: React/TypeScript SPA hosted on a CDN.
*   **API Gateway**: Spring Cloud Gateway / NGINX entry point.
*   **Core Domain Service**: Java / Spring Boot service with Catalog Management, Circulation Engine, User Management, and Data Access components.
*   **Search Service**: Python / FastAPI service.
*   **Integration Service**: Node.js / Express service.
*   **PostgreSQL**: Primary relational database (EU-hosted).
*   **Elasticsearch**: Search index (EU-hosted).
*   **Redis**: In-memory data store / cache (EU-hosted).
*   **RabbitMQ**: Message broker for asynchronous events (EU-hosted).

## Relationships
*   *Web Application* ➔ *API Gateway*: HTTPS / JSON
*   *API Gateway* ➔ *Core Domain Service* & *Search Service*: gRPC over mTLS
*   *Core Domain Service* ➔ *PostgreSQL*: JDBC over TLS 1.3
*   *Core Domain Service* ➔ *Redis*: RESP over TLS 1.3
*   *Core Domain Service* ➔ *RabbitMQ*: AMQP
*   *Integration Service* ➔ External Payment Gateways & Legacy ILS: HTTPS / AMQP

## Technology Stack
*   **Frontend**: React and TypeScript for client-side portals.
*   **Backend Services**: Java/Spring Boot for core logic, Python/FastAPI for search, Node.js/Express for integrations.
*   **Data & Caching**: PostgreSQL for relational storage, Elasticsearch for sub-800ms search, Redis for session and metadata caching.
*   **Messaging**: RabbitMQ for asynchronous event decoupling.
*   **Infrastructure**: EU-isolated VPC deployment to enforce data residency constraints.

## Rationale
Isolating the Python/FastAPI search service and Elasticsearch guarantees 99th-percentile search responses under 800ms without impacting core transactional workloads. Deploying all data stores within dedicated EU-region VPCs strictly fulfills the EU-only data residency constraint.