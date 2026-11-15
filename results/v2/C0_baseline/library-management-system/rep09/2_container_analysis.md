## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals exclusively within EU boundaries. It is designed to meet strict performance SLAs while ensuring robust security and high availability.

## Key Elements
- Library Patrons, Librarians/Circulation Staff, Library Administrators
- API Gateway (Nginx / Kong)
- Web App / Admin Portal (React, Node.js SSR)
- Core Services Container (Java / Spring Boot)
- Search Container (Elasticsearch)
- Database Container (PostgreSQL)
- Async Worker Container (Python / Celery or Java)
- EU Identity Provider (IdP), EU Payment Gateway, EU Notification Service, EU Cloud Infrastructure, Centralized Log & Metrics Aggregator

## Relationships
- Patrons and Staff access the *Web App / Admin Portal* via HTTPS.
- *API Gateway* routes traffic to *Web App* and *Core Services* using mTLS via gRPC/HTTPS.
- *Core Services* queries *PostgreSQL* and *Search Container* (Elasticsearch) synchronously.
- *Core Services* publishes checkout/notification events asynchronously to *Async Worker Container*.
- External integrations use TLS 1.3 with egress-controlled network policies.

## Technology Stack
- Kubernetes on EU Cloud Infrastructure: For immutable container deployments and zero-downtime rolling updates.
- Java / Spring Boot & Python / Celery: For core business logic and asynchronous task processing.
- React / Node.js SSR: For responsive web applications and admin portals.
- PostgreSQL & Elasticsearch: For relational data persistence and sub-second catalog discovery.
- Istio Service Mesh: To enforce mTLS and secure inter-container communication.

## Rationale
This architecture uses dedicated search and database containers hosted strictly within EU regions to achieve the sub-800ms search SLA. Asynchronous workers and stateless JWT validation isolate external dependencies and prevent bottlenecks, ensuring high availability and legal compliance.