## Overview
The Library Management System provides self-service portals and circulation management for academic and public libraries. It ensures strict EU-only data residency while delivering high-performance catalog searches.

## Key Elements
* **Users:** Library Patrons, Librarians, Circulation Staff, Library Administrators
* **UI Containers:** Patron Web Portal (React, Nginx), Staff Management Portal (Angular, Nginx)
* **API & Core Containers:** Core API Gateway (Spring Cloud Gateway), Catalog & Search Service (Spring Boot, Elasticsearch), Circulation Service (Quarkus, PostgreSQL)
* **Messaging & Async Containers:** Notification Worker (Node.js), RabbitMQ
* **External Systems:** Payment Gateway, Notification Service, Identity Provider, External Academic Identity Federation, Digital Content Repositories, Centralized Observability Platform

## Relationships
* **Patron Web Portal & Staff Management Portal** interact with **Core API Gateway** via HTTPS REST/GraphQL.
* **Core API Gateway** routes search queries to **Catalog & Search Service** via gRPC.
* **Core API Gateway** routes transactions to **Circulation Service** via gRPC.
* **Circulation Service** and **Catalog & Search Service** synchronize via RabbitMQ (AMQP over TLS).
* **Notification Worker** consumes events from RabbitMQ and calls the external **Notification Service**.
* **Containers** ship telemetry to **Centralized Observability Platform** via gRPC.

## Technology Stack
* **React & Angular (Nginx):** Frontend container hosting for isolated UI performance.
* **Spring Cloud Gateway:** Centralized routing, rate-limiting, and JWT validation.
* **Elasticsearch (Spring Boot):** Dedicated search engine to meet the <800ms search SLA (R-05).
* **PostgreSQL (Quarkus):** Transactional datastore for loans, fines, and circulation data.
* **RabbitMQ:** Asynchronous event broker with dead-letter exchanges for resilient messaging.
* **Kubernetes:** EU-managed container orchestration ensuring data residency compliance.

## Rationale
Isolating patron and staff UI containers behind a unified API gateway prevents heavy librarian cataloging tasks from degrading patron search performance. Furthermore, dedicated Elasticsearch and PostgreSQL containers deployed within an EU-managed Kubernetes cluster satisfy the strict performance SLA and data residency constraints.