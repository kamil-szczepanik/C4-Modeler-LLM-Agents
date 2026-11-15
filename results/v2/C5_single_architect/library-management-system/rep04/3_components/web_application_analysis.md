## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The Web Application container is decomposed into modular frontend components to ensure high-performance discovery and circulation.

## Key Elements
* Library Patron and Librarian / Library Staff (Users)
* Web Application (React, TypeScript Container)
* Routing & Shell Component
* Catalog & Search Component
* Circulation & Self-Service Component
* API Client Service
* API Gateway (Kong or NGINX), Core Domain (Java, Spring Boot), and Search Engine (Elasticsearch)

## Relationships
* Library Patron & Librarian -> Web Application: Accesses portals [HTTPS]
* Web Application -> API Gateway: Routes requests [HTTPS/REST and WebSockets]
* Routing & Shell -> Catalog & Search & Circulation & Self-Service: Delegates views
* Catalog & Search -> TanStack Query -> API Client Service: Fetches data [HTTPS/REST]
* Domain components -> API Client Service: Communicates with backend [HTTPS/REST and WebSockets]

## Technology Stack
* React with TypeScript: Enforces type safety and structured SPA navigation
* TanStack Query: Provides client-side caching and input debouncing to meet performance constraints
* Axios/Fetch: Handles HTTP transport
* WebSockets: Streams real-time notifications

## Rationale
This architecture decouples UI domain logic from network transport while implementing client-side caching to guarantee 99th-percentile search response times under 800ms. It maintains strict EU data residency constraints through localized integration patterns.