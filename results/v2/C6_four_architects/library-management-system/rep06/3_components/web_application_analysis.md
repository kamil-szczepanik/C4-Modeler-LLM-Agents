## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It uses a component-based frontend and a hexagonal backend architecture.

## Key Elements
- **Web Application Container**: React, TypeScript SPA hosted on a CDN.
- **Router Component**: `react-router-dom` for client-side routing.
- **Auth & State Store Component**: `Zustand` and OAuth2/OIDC Client.
- **UI Component Library**: `Tailwind CSS` and `Radix UI`.
- **API Client Component**: `Axios` for HTTP communication.
- **Search & Catalog View Component**: Optimized for performance.
- **Localization Component**: `react-i18next` for multi-language support.
- **Error Boundary Component**: `React Error Boundary` for fault handling.
- **Core Domain Service Container**: Java and Spring Boot backend.
- **Inbound REST Adapters**: Spring MVC controllers.
- **Domain Services**: Pure business logic core for item cataloging (R-01).
- **Outbound Persistence Adapters**: `Spring Data JPA` for PostgreSQL.
- **Outbound Messaging Adapters**: `Spring AMQP` for RabbitMQ.

## Relationships
- **Web Application** -> **API Gateway**: Sends requests [HTTPS / JSON, TLS 1.3].
- **UI/Router Components** -> **API Client Component**: Fetches and renders data [Internal TS Function Call].
- **Search & Catalog View Component** -> **API Client Component**: Executes paginated queries [Internal TS Function Call].
- **Inbound REST Adapters** -> **Domain Services**: Invokes use case interfaces [Java Method Call].
- **Domain Services** -> **Outbound Adapters**: Triggers data operations [Java Method Call / AMQP].

## Technology Stack
- **React & TypeScript**: Powers the high-performance SPA client interface.
- **Zustand & OAuth2/OIDC**: Secures sessions and enforces EU data residency.
- **Tailwind CSS & Radix UI**: Delivers accessible, responsive design elements.
- **Java & Spring Boot**: Powers scalable, robust backend microservices.
- **Spring Data JPA & PostgreSQL**: Manages relational persistence with EU data constraints.
- **Spring AMQP & RabbitMQ**: Handles asynchronous domain event messaging.

## Rationale
This architecture combines a component-optimized frontend with a hexagonal backend to meet rigorous performance goals like sub-800ms search responses. Furthermore, it strictly enforces EU-only data residency and modular separation of concerns.