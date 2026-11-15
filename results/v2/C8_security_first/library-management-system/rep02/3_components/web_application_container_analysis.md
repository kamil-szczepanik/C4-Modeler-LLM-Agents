## Overview
The Library Management System provides item cataloguing, circulation management, and self-service portals for public and academic libraries. The architecture ensures strict EU-only data residency and high-performance search responses.

## Key Elements
- **Users**: Library Patrons, Library Staff and Cataloguers, Library Administrators
- **Containers**: Web Application Container (React with NGINX), Envoy Proxy, Catalogue Service (Spring Boot), Circulation & Loan Service (Node.js/Express), Notification Service Worker (Python FastAPI), Search Indexer (Elasticsearch)
- **Databases & Brokers**: Catalogue DB (PostgreSQL), Circulation DB (PostgreSQL), Message Broker (RabbitMQ)
- **External Systems**: Enterprise Identity Provider, Payment Gateway, Notification Service

## Relationships
- Library Patrons / Staff / Administrators -> Web Application Container: Accesses portals/interfaces [HTTPS (REST/JSON)]
- Web Application Container -> Envoy Proxy: Forwards web requests [HTTPS (TLS 1.3)]
- Envoy Proxy -> Catalogue Service & Circulation Service: Routes API requests [gRPC / HTTPS]

## Technology Stack
- React with NGINX: Frontend self-service and management portals, delivering high-performance UI rendering and strict security headers.
- Spring Boot (Java): Robust backend processing for catalogue management.
- Node.js/Express: Lightweight, high-throughput handling for circulation and loans.
- PostgreSQL: Relational storage ensuring EU-only data residency compliance.
- Elasticsearch: High-speed search engine supporting <800ms response requirements.

## Rationale
This microservices-based architecture decouples heavy cataloguing workflows from self-service portals while maintaining strict API boundaries. The technology stack guarantees high performance, secure session management, and full compliance with EU data residency constraints.