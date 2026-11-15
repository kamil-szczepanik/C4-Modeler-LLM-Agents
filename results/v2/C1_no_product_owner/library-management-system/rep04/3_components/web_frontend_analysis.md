## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The architecture utilizes a React SPA frontend hosted on Nginx communicating with Spring Boot microservices via an API Gateway.

## Key Elements
- Library Patron, Librarian (Users)
- Web Frontend (React SPA, Nginx Container)
- Routing & Shell Component, Catalog Component, Circulation Component, API Client Component, Auth & Session Component (Frontend Components)
- API Gateway (Spring Cloud Gateway)
- Catalogue Service, Circulation Service, Notification Service (Spring Boot, Java 21)
- PostgreSQL, Elasticsearch (Databases), RabbitMQ (Message Broker)

## Relationships
- Library Patron / Librarian -> Web Frontend: Accesses portals via `HTTPS/REST` and `WSS://` (WebSockets)
- Web Frontend -> API Gateway: Sends API requests via `HTTPS/REST` with W3C Trace Context headers (`traceparent`) and HttpOnly cookies
- API Gateway -> Catalogue Service / Circulation Service: Routes internal requests

## Technology Stack
- React / React Router: UI framework and routing for client-side rendering
- Nginx: Web server configured with strict CSP headers, TLS 1.3, and EU-only data residency hosting
- TanStack Query: Client-side state management and pagination to meet <800ms search latency
- Axios: HTTP and WebSocket transport client

## Rationale
Client-side caching and pagination ensure 99th-percentile search responses remain under 800 ms. Strict Nginx security headers and secure cookie management protect patron data while complying with EU data residency constraints.