## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and sub-800ms search response times.

## Key Elements
*   **Users**: Library Patrons, Librarians / Circulation Staff, Library Administrators
*   **Containers**: Web Frontend (SPA), API Gateway, Core Business Service, Search Service, Database, Notification Dispatcher, Audit Logging Service, Message Broker
*   **External Systems**: Payment Gateway, Identity Provider (IdP), Notification Service

## Relationships
*   **Web Frontend** to **API Gateway**: HTTPS/REST
*   **API Gateway** to **Core Business Service & Search Service**: Internal REST/gRPC secured via mTLS
*   **Core Business Service** to **Database**: JDBC (PostgreSQL)
*   **Core Business Service & Notification Dispatcher** to **Message Broker**: AMQP (RabbitMQ/AWS SQS)
*   **Notification Dispatcher** to **Notification Service**: Outbound HTTPS
*   **External Integrations**: Payment Gateway and IdP via OAuth2/TLS 1.3 with webhook signature verification

## Technology Stack
*   **Web Frontend**: React/TypeScript hosted on an EU-region CDN
*   **API Gateway**: Kong or Nginx for reverse proxy and rate limiting
*   **Core Business Service**: Spring Boot (Java) for circulation and cataloging logic
*   **Search Service**: Elasticsearch cluster optimized for R-05 performance (<800ms)
*   **Database**: PostgreSQL managed in an EU AWS/Azure region enforcing AES-256 encryption-at-rest
*   **Notification Dispatcher**: Python/Celery worker container
*   **Audit Logging**: Go-based microservice with WORM storage

## Rationale
Separating user-facing portals from back-office management protects search performance (R-05) during peak hours. Strict regional hosting, mTLS, and append-only audit logging guarantee compliance with EU data residency and GDPR mandates.