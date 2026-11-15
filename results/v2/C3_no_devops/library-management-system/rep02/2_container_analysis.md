## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures strict EU data residency and high-performance search capabilities.

## Key Elements
- **Users**: Library Member (Patron), Librarian / Library Staff, Library Administrator
- **Containers**: Web Application (React/TypeScript SPA with IndexedDB/Service Workers), API Gateway (NGINX / Spring Cloud Gateway), Core Business Services (Java/Spring Boot), Search Engine (Elasticsearch / OpenSearch), Database (PostgreSQL), Analytics Worker (Python/Spring + Apache Kafka/RabbitMQ)
- **External Systems**: Payment Gateway, Digital Content Providers, Notification System

## Relationships
- Patron / Staff to API Gateway via HTTPS/REST and WebSockets
- API Gateway to Core Business Services and Search Engine via gRPC / internal REST with mTLS
- Core Business Services to Database via secure PostgreSQL protocol
- Core Services to Analytics Worker via Apache Kafka / RabbitMQ event streaming with mTLS

## Technology Stack
- **Frontend**: React and TypeScript served via CDN, with browser IndexedDB for local caching
- **Routing/Security**: NGINX or Spring Cloud Gateway, OAuth 2.0 / OpenID Connect with JWT
- **Backend**: Java with Spring Boot for core services
- **Search**: Elasticsearch / OpenSearch cluster for R-05 (<800ms response)
- **Data & Analytics**: PostgreSQL managed service (EU-hosted), Apache Kafka/RabbitMQ for event streaming

## Rationale
This architecture decouples the user-facing SPA and API Gateway to deliver fast, secure self-service experiences while isolating core business services. Dedicated search and analytics containers satisfy performance targets and business metrics without violating strict EU-only data residency constraints.