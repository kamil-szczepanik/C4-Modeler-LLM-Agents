## Overview
A Library Management System providing public and academic libraries with item cataloging, circulation management, and self-service portals. The architecture ensures strict EU-only data residency and high performance.

## Key Elements
* Patrons, Librarians, Library Administrators (Users)
* Academic Identity Providers, Payment Gateway, Digital Content Providers, EU Notification Gateway (External Systems)
* Patron Self-Service Portal & Librarian Management Portal (React/TypeScript SPAs)
* API Gateway (Kong / Envoy)
* Search Microservice & Circulation & Catalogue Microservice (Java / Spring Boot)
* Notification Dispatcher (Node.js / TypeScript)
* Message Broker (RabbitMQ / Kafka)
* Database Layer (PostgreSQL with EU-pinned TLS 1.3/JDBC) & Elasticsearch (EU-hosted)

## Relationships
* Patron Self-Service Portal -> API Gateway [HTTPS]
* Librarian Management Portal -> API Gateway [HTTPS]
* API Gateway -> Search Microservice [gRPC/HTTP2 over mTLS with OAuth 2.0 / OIDC]
* API Gateway -> Circulation & Catalogue Microservice [gRPC/HTTP2 over mTLS with OAuth 2.0 / OIDC]
* API Gateway -> Academic Identity Providers [OIDC and SAML over HTTPS]
* API Gateway -> Payment Gateway [REST/JSON over HTTPS with mTLS and OAuth2]
* API Gateway -> Digital Content Providers [REST/JSON over HTTPS with mTLS and OAuth2]

## Technology Stack
* Kong / Envoy (API Gateway): Chosen for edge routing, WAF inspection, JWT validation, and circuit breaking.
* React / TypeScript (SPAs): Enables responsive self-service and management portals.
* Java / Spring Boot (Microservices): Provides robust, scalable backend processing for search and cataloging.
* PostgreSQL & Elasticsearch (Data Layer): Ensures secure, performant storage and 99th-percentile search responses under 800ms within EU constraints.

## Rationale
This architecture uses an API Gateway to enforce security, data residency, and resilience at the edge while protecting backend microservice resources. Decoupled microservices and geo-redundant EU deployment guarantee scalability, sub-800ms search performance, and compliance.