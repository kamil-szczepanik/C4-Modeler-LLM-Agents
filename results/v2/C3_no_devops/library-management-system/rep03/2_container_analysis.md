## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and sub-800ms search performance requirements.

## Key Elements
- Library Patrons (Members), Librarians / Circulation Staff, Library Administrators
- Patron Portal (React.js SPA) and Librarian Back-office (Next.js Web App)
- API Gateway (NGINX / Envoy)
- Catalogue Service (Java/Spring Boot) and Circulation Service (Node.js/Express)
- Asynchronous Event-Driven Messaging (Apache Kafka / RabbitMQ)
- Data Layer: PostgreSQL and Elasticsearch (EU-hosted)
- External Identity Provider (IdP), Third-Party Payment Gateway, Digital Content Repositories

## Relationships
- Patrons and Librarians to Web Frontends via HTTPS
- Web Frontends to API Gateway via HTTPS using OAuth2/OIDC with JWTs
- API Gateway to Backend Services via mTLS via Istio Service Mesh
- Catalogue and Circulation Services to Databases via encrypted connections with AES-256
- Backend Services to Event Broker via TLS-encrypted event streams

## Technology Stack
- React.js / Next.js: For responsive frontends and rapid initial load times
- Java/Spring Boot & Node.js/Express: For decoupled, high-performance backend microservices
- Elasticsearch: EU-hosted search engine ensuring <800ms 99th-percentile search responses
- PostgreSQL: EU-hosted relational database for transactional circulation data
- Apache Kafka / RabbitMQ: Asynchronous messaging to decouple search and check-out workflows
- Istio Service Mesh: For mTLS, zero-trust segmentation, and traffic policies

## Rationale
This architecture decouples heavy patron search traffic from front-desk circulation to protect performance and user experience. It enforces absolute EU data residency and zero-trust security via geo-isolated Kubernetes, regional KMS encryption, and service mesh policies.