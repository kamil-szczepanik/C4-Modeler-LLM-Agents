## Overview
The Library Management System is a public and academic library solution for cataloguing items, managing circulation, and providing self-service portals. It enforces EU-only data residency and maintains a 99th-percentile search response under 800 ms.

## Key Elements
- Library Patron (User)
- Library Staff (User)
- Web Application (React, TypeScript)
- API Gateway (Spring Cloud Gateway / Envoy)
- Catalogue Service, Circulation Service, Digital Content Proxy Service (Java, Spring Boot)
- Notification Worker (Node.js)
- PostgreSQL, Redis, Elasticsearch, RabbitMQ (Infrastructure)
- Router / State Management Component (React Router, Redux Toolkit)
- Authentication & Session Manager Component (React Context / OIDC client)
- Feature Modules Component (React)
- API Client Component (Axios)
- UI Component Library (Tailwind CSS, Radix UI)

## Relationships
- Library Patron -> Web Application [HTTPS]
- Library Staff -> Web Application [HTTPS]
- Web Application -> API Gateway [HTTPS/JSON]
- Feature Modules Component -> API Client Component [Internal Function Call]
- API Client Component -> API Gateway [HTTPS/JSON]

## Technology Stack
- React, TypeScript: Powers responsive UI and type-safe frontend components
- Spring Boot: Provides robust microservices for domain logic
- Spring Cloud Gateway / Envoy: Secures and routes API traffic
- PostgreSQL, Elasticsearch, Redis: Handles relational data, fast search, and caching within EU-only constraints

## Rationale
This architecture ensures secure API boundaries by routing all client requests through an API Gateway instead of exposing direct database connections. It delivers high-performance search and maintains strict EU data residency compliance.