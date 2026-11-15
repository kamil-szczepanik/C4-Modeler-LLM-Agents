## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It is architected as a secure, high-performance distributed system with strict EU-only data residency enforcement.

## Key Elements
*   **Web Application**: React, TypeScript SPA served via CDN
*   **Self-Service Kiosk App**: Electron / C# WPF desktop app
*   **API Gateway**: Nginx / Kong reverse proxy
*   **Core Domain Service**: Java, Spring Boot microservice
*   **Search Service**: Elasticsearch index
*   **Reporting & Analytics Service**: Python, FastAPI microservice
*   **Database**: PostgreSQL (EU-hosted)
*   **Distributed Cache**: Redis in-memory data store
*   **Notification & Event Bus**: Apache Kafka (EU-hosted)
*   **Async Worker**: Python, Celery background worker

## Relationships
*   **Web Application / Kiosk App** -> **API Gateway** via HTTPS (REST/JSON)
*   **API Gateway** -> **Core Domain Service** & **Reporting Service** via gRPC over TLS
*   **Core Domain Service** -> **PostgreSQL** via JDBC
*   **Core Domain Service** -> **Search Service** via HTTP/REST over TLS
*   **Core Domain Service** -> **Redis Cache** via TCP
*   **Core Domain Service** -> **Kafka Broker** via Kafka Wire Protocol
*   **Async Worker** -> **External Systems** (Payment Gateway, Notification Service) via HTTPS

## Technology Stack
*   **React / TypeScript**: Frontend rendering for responsive web UI
*   **Java / Spring Boot**: Robust backend platform for core business logic
*   **Elasticsearch**: Dedicated search engine ensuring 99th-percentile search response < 800 ms
*   **PostgreSQL**: Relational storage ensuring ACID compliance within EU boundaries
*   **Redis**: In-memory caching for session management and fast catalog lookups
*   **Apache Kafka**: Event broker for decoupled, reliable asynchronous processing

## Rationale
This architecture uses dedicated caching and search containers to guarantee sub-800ms search performance under load. Strict private subnet isolation and centralized EU-hosted persistence ensure full compliance with mandatory EU data residency constraints.