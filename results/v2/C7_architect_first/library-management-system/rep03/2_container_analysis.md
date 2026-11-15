## Overview
The Library Management System is a comprehensive solution designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service patron portals. It ensures EU-only data residency and maintains a 99th-percentile search response time under 800 milliseconds.

## Key Elements
* Library Patron and Librarian / Staff (Users)
* Payment Gateway, National Library Registry, Third-Party IdP / Academic SSO, Notification System (External Systems)
* Web Application SPA (React/TypeScript)
* API Gateway (NGINX / Spring Cloud Gateway)
* Core Domain Service (Java/Spring Boot)
* Search Service (Python/FastAPI with Elasticsearch)
* Database (PostgreSQL)
* Background Worker (Python/Celery) & Asynchronous Broker (Redis)

## Relationships
* Web Application SPA to API Gateway via HTTPS/WSS with JWT validation
* API Gateway to Core Domain Service and Search Service via gRPC over HTTP/2 with mTLS
* Core Domain and Search Services to PostgreSQL via JDBC/TLS
* Core Domain Service and Background Worker to Redis via TLS

## Technology Stack
* React/TypeScript: Client-side routing for patron/staff portals via CDN
* Java/Spring Boot: Manages cataloging, circulation, and business logic
* Python/FastAPI & Elasticsearch: Optimizes indices for sub-800ms search NFR
* PostgreSQL: Relational storage with EU-only data residency and column-level PII encryption
* Redis & Celery: Asynchronous background task processing and event pub/sub with AOF persistence
* NGINX / Spring Cloud Gateway: Handles routing, SSL termination, and JWT validation

## Rationale
This container-based architecture isolates resource-heavy components like the Search Service and Redis-backed background workers to easily meet strict performance and search latency requirements. Security and compliance controls, including EU-hosted infrastructure, mTLS, TLS 1.3, and column-level encryption, fully satisfy European data residency and GDPR mandates.