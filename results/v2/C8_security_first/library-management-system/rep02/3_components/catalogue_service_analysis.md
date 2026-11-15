## Overview
The Library Management System is a comprehensive digital solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and sub-800ms search performance SLAs.

## Key Elements
*   **Users:** Library Patrons, Library Staff and Cataloguers, Library Administrators
*   **External Systems:** Enterprise Identity Provider, Payment Gateway, Notification Service
*   **Containers & Infrastructure:** Envoy Proxy, Web Application Container (React with NGINX), Catalogue Service (Spring Boot/Java), Circulation & Loan Service (Node.js/Express), Notification Service Worker (Python FastAPI), Search Indexer (Elasticsearch), Catalogue DB & Circulation DB (PostgreSQL), Message Broker (RabbitMQ)
*   **Catalogue Service Components:** API Controller (Spring MVC/gRPC), Catalogue Management Domain, Search & Query Component, Event Publisher, Catalogue Analytics Component

## Relationships
*   **Envoy Proxy -> Catalogue Service:** Routes cataloguing requests using mTLS and gRPC/Protobuf
*   **Catalogue Service -> Search Indexer:** Indexes and searches catalogue data via gRPC/Protobuf
*   **Catalogue Service -> Catalogue DB & Circulation DB:** Reads and writes catalogue data using TLS 1.3 and gRPC/Protobuf
*   **Catalogue Service -> Message Broker:** Publishes signed domain events via RabbitMQ
*   **Catalogue Service -> Notification Service:** Exposes metadata hooks for patron alerts

## Technology Stack
*   **Spring Boot (Java):** Powers the Catalogue Service, providing robust enterprise processing.
*   **Elasticsearch:** Serves as the Search Indexer for high-performance faceted searches (<800ms SLA).
*   **PostgreSQL:** Acts as the primary persistent storage for catalogue and circulation data under TLS 1.3.
*   **RabbitMQ:** Handles asynchronous event messaging with HMAC event signature verification.
*   **Kubernetes:** Manages containerized deployments, HPAs, and EU-localized resource quotas.
*   **OpenTelemetry & Prometheus/Grafana:** Provides distributed tracing and observability.

## Rationale
This architecture decouples write-heavy cataloguing operations from read-heavy search models to consistently achieve the sub-800ms performance SLA under heavy loads. Strict component isolation, TLS 1.3 encryption, and Kubernetes-based deployments ensure compliance with EU data residency mandates and security best practices.