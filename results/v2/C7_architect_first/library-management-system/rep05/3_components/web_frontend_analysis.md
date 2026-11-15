## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and maintains high performance with sub-800ms search responses.

## Key Elements
- **Users:** Library Patron, Academic Researcher, Librarian / Administrator, Library Manager
- **External Systems:** EU-Compliant Payment Gateway, Third-Party Notification Service, External Identity Provider (IdP)
- **Containers:** Web Frontend, API Gateway, Core Catalog Service, Circulation & Search Service, Worker Service
- **Frontend Components:** Authentication Manager, Catalogue & Search UI, Circulation & Self-Service Portal, Admin Dashboard, State & Session Store, API Client

## Relationships
- Library Patron, Academic Researcher, Librarian / Administrator, Library Manager -> Web Frontend: Accesses portals, catalogues, and admin UI via HTTPS
- Web Frontend -> API Gateway: Sends API requests via HTTPS/REST and WebSockets
- Web Frontend -> External IdP: Handles login and session tokens via OIDC Client

## Technology Stack
- **Web Frontend:** React, TypeScript, TanStack Query, Zustand, Chart.js
- **Reverse Proxy & Delivery:** Nginx, EU-Hosted Object Storage
- **Gateways & Backend:** Kong / Spring Cloud Gateway, Spring Boot, FastAPI, PostgreSQL, Elasticsearch
- **Asynchronous & Observability:** Celery, RabbitMQ, OpenTelemetry JS SDK, Prometheus

## Rationale
Decoupling static React build artifacts into EU-hosted object storage fronted by Nginx strictly enforces the EU-only data residency constraint. In-memory state management and optimized UI components ensure 99th-percentile search responses remain under 800ms.