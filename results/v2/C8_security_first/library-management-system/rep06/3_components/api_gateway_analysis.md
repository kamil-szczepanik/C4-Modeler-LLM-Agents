## Overview
The Library Management System is a comprehensive platform for public and academic libraries designed to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and high-performance search capabilities.

## Key Elements
- **Users:** Library Patrons, Librarians/Catalogers, Library Administrators
- **Frontends:** Patron Portal (Next.js), Librarian Dashboard (React)
- **API Gateway Layer:** Envoy Proxy (handling routing, rate-limiting, and ingress security)
- **Core Services:** Search & Catalogue Service (Elasticsearch/OpenSearch), Circulation Service (Node.js/Go), Notification Service (Node.js/Go), Integration Service (Python/Go)
- **Infrastructure & Security:** HashiCorp Vault, Message Broker (Kafka/RabbitMQ), PostgreSQL Database, Identity Provider (OAuth 2.0 / OIDC)
- **External Systems:** EU Payment Gateway, National Library Database

## Relationships
- Patron Portal -> API Gateway: Makes HTTPS (REST/GraphQL) API requests with OAuth 2.0 / OIDC tokens
- Librarian Dashboard -> API Gateway: Makes HTTPS (REST/GraphQL) API requests with OAuth 2.0 / OIDC tokens
- API Gateway -> Search & Catalogue Service: Queries catalogue via gRPC with mTLS
- API Gateway -> Identity Provider: Offloads token validation and claim verification
- Envoy Proxy -> HashiCorp Vault: Automates short-lived mTLS certificate rotation

## Technology Stack
- **API Gateway:** Envoy Proxy configured via xDS dynamic control planes and WebAssembly (Wasm) filters for robust performance, gRPC-web support, and low memory footprint
- **Frontend:** Next.js (Patron Portal) and React (Librarian Dashboard)
- **Search:** Elasticsearch/OpenSearch to satisfy the <800ms search NFR
- **Security & Auth:** OAuth 2.0 / OIDC, HashiCorp Vault, TLS 1.3 ingress, and mTLS internal transport
- **Observability:** Prometheus/OpenTelemetry with W3C Trace Context propagation restricted to EU backends

## Rationale
This architecture uses Envoy Proxy to establish a secure, observable trust boundary that successfully isolates public traffic while enforcing EU data residency constraints. The decoupled microservices and circuit-breaking modules guarantee high performance and sub-800ms search responses under peak loads.