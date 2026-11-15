## Overview
The Library Management System provides public and academic libraries with item cataloguing, circulation management, and self-service portals. It enforces strict EU-only data residency while maintaining high-performance search capabilities.

## Key Elements
- Library Patrons, Library Staff and Cataloguers, Library Administrators
- Envoy Proxy (API Gateway)
- React with NGINX (Web Application Container)
- Spring Boot (Catalogue Service)
- Node.js/Express (Circulation & Loan Service)
- Python FastAPI (Notification Service Worker)
- Elasticsearch (Search Indexer)
- PostgreSQL (Catalogue DB and Circulation DB)
- RabbitMQ (Message Broker)
- Enterprise Identity Provider, Payment Gateway, Notification Service

## Relationships
- Patrons/Staff to Web Application Container via HTTPS (REST/JSON)
- Web Application to API Gateway via HTTPS (TLS 1.3)
- API Gateway to Catalogue and Circulation Services via mTLS and gRPC/Protobuf
- Catalogue Service to Elasticsearch and Catalogue DB via gRPC/Protobuf
- Circulation Service to Circulation DB via gRPC/Protobuf and RabbitMQ via AMQP
- Circulation Service to Payment Gateway via HTTPS (REST/JSON)
- Notification Service Worker to Notification Service via HTTPS (REST/JSON)

## Technology Stack
- Envoy Proxy for external ingress, rate limiting, and TLS termination
- React / NGINX for frontend self-service portals
- Spring Boot (Java) for cataloguing to ensure robust enterprise processing
- Node.js/Express for circulation and loan management
- Python (FastAPI) for asynchronous notification processing
- Elasticsearch for sub-800ms catalogue search performance
- PostgreSQL with AES-256 encrypted EU persistent volumes for relational data
- RabbitMQ for asynchronous messaging and circuit-breaking payment processing
- gRPC/Protobuf for low-latency internal service-to-service communication
- OpenTelemetry for distributed tracing and observability

## Rationale
The container decomposition isolates high-performance search (Elasticsearch) and low-latency internal gRPC communication to satisfy the 99th-percentile search response time under 800 ms. Strict EU-located node assignments, encrypted persistent volumes, and application-layer message encryption ensure full compliance with EU-only data residency requirements.