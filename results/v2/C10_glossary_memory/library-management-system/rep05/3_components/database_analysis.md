## Overview
[The Library Management System is a comprehensive solution providing self-service portals, circulation management, and cataloguing for public and academic libraries. It ensures strict EU-only data residency and high-performance search capabilities.]

## Key Elements
* Library Patrons & Staff
* EU-edge Reverse Proxy
* Self-Service Web App
* Admin/Staff Portal
* API Gateway
* Circulation & Cataloguing Service
* Core Search Engine
* Database (PostgreSQL with Connection Pool Manager, Relational Storage Engine, Audit & Encryption Subsystem, Replication & Backup Subsystem, and Data Retention & Archival Subsystem)
* Third-Party Digital Content Providers
* Payment Gateway
* Notification Service

## Relationships
* Library Patrons & Staff -> EU-edge Reverse Proxy (HTTPS/TLS 1.3, OIDC/OAuth2)
* EU-edge Reverse Proxy -> Self-Service Web App (HTTPS)
* EU-edge Reverse Proxy -> Admin/Staff Portal (HTTPS)
* Self-Service Web App -> API Gateway (HTTPS/REST with JWT)
* Admin/Staff Portal -> API Gateway (HTTPS/REST with JWT)
* API Gateway -> Circulation & Cataloguing Service (gRPC/Internal, mTLS)
* Circulation & Cataloguing Service -> Core Search Engine (TCP)
* Circulation & Cataloguing Service -> Database Connection Pool Manager (PostgreSQL Wire Protocol, mTLS)
* Circulation & Cataloguing Service -> Third-Party Digital Content Providers (REST/JSON over HTTPS)
* Circulation & Cataloguing Service -> Payment Gateway (HTTPS/REST)
* Circulation & Cataloguing Service -> Notification Service (Webhooks/SMTP with HMAC)

## Technology Stack
* React/Next.js SPA: Frontend implementation for patron self-service
* React Admin SPA: Frontend implementation for staff operations
* Nginx/Kong: API Gateway for routing, rate limiting, and JWT validation
* Node.js/TypeScript: Core business logic implementation
* Elasticsearch: Core search engine ensuring search SLAs under 800ms
* PostgreSQL: Managed database with AES-256 encryption at rest, B-tree/GIN indexing, and EU region placement

## Rationale
[This architecture cleanly separates frontend interfaces, API routing, and core domain services to maintain high availability and performance. Utilizing managed PostgreSQL in the EU region with strict encryption and connection pooling directly satisfies data residency constraints and performance SLAs.]