## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures EU-only data residency and meets high-performance search requirements.

## Key Elements
- **Library Patron & Librarian**: End users accessing the system.
- **Web Application**: React and TypeScript frontend.
- **API Gateway**: Kong or NGINX container comprising:
  - Routing & Proxy Engine (Kong/NGINX Core)
  - Authentication & Authorization Filter (Lua/OpenResty, JWT)
  - Rate Limiting & Throttling Module (Redis-backed)
  - SSL/TLS Termination & Security Headers Module (OpenSSL/NGINX)
  - Request Transformation & Analytics Filter (Lua/Go)
- **Core Domain**: Java, Spring Boot microservices.
- **Search Engine**: Elasticsearch for cataloging and search.
- **Integration Worker**: Node.js/Python background processor.
- **Message Broker**: RabbitMQ for asynchronous messaging.
- **PostgreSQL Database**: Relational datastore.
- **External Systems**: Identity Provider (IdS), Payment Gateway, Notification Service, DRM Provider.

## Relationships
- Web Application -> SSL/TLS Termination & Security Headers Module: Entry point for traffic [HTTPS]
- SSL/TLS Termination & Security Headers Module -> Authentication & Authorization Filter: Forwards decrypted traffic
- Authentication & Authorization Filter -> Routing & Proxy Engine: Forwards validated requests
- Routing & Proxy Engine -> Core Domain: Proxies internal traffic [gRPC and internal REST]
- Routing & Proxy Engine -> Search Engine: Direct internal queries for performance [gRPC/REST]

## Technology Stack
- React / TypeScript: Frontend UI for responsive user experience.
- Kong / NGINX: API Gateway for secure routing, SSL termination, and rate limiting.
- Java / Spring Boot: Core business logic with robust enterprise capabilities.
- Elasticsearch: High-speed search engine supporting <800ms response SLA.
- PostgreSQL: Relational storage enforcing EU data residency constraints.
- RabbitMQ: Asynchronous messaging between core and integration workers.

## Rationale
This architecture decouples the presentation layer from backend services using a high-performance API Gateway to meet strict latency and security goals. Microservices and dedicated search components ensure scalability while adhering to EU-only data residency constraints.