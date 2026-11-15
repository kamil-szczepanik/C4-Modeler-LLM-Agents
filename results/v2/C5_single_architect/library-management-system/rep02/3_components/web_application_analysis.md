## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It ensures EU-only data residency and meets high-performance search requirements.

## Key Elements
* Library Patrons and Library Staff (Users)
* Web Application (React/TypeScript SPA)
* Auth Controller (TypeScript / OIDC Client Library)
* Catalog UI Module (React Components / TanStack Query)
* Circulation Module (React Components)
* API Client (Axios / Fetch API)
* State Management Store (Zustand / Redux Toolkit)
* Router Component (React Router)
* API Gateway (Nginx / Spring Cloud Gateway)
* Core Domain Service (Java/Spring Boot)
* Search Service (Java with Elasticsearch)
* Notification Worker (Node.js)
* Database (PostgreSQL)
* Message Broker (RabbitMQ / Apache Kafka)
* External Systems: Payment Gateway, Notification Service, National Library Registry, Identity Provider

## Relationships
* Library Patrons and Library Staff -> Web Application: Interacts via [HTTPS]
* Web Application -> API Gateway: Calls APIs via [HTTPS/REST]
* Router Component -> Catalog UI Module & Circulation Module: Lazy-loads views [In-process]
* Auth Controller & UI Modules -> State Management Store: Manages state [In-process]
* Auth Controller & Catalog UI Module -> API Client: Invokes requests [In-process]
* API Client -> API Gateway: Forwards authenticated requests [HTTPS/REST]

## Technology Stack
* React/TypeScript SPA: Powers the user-facing Single Page Application via CDN
* Zustand / Redux Toolkit: Manages local application state and caching
* React Router: Handles client-side navigation and lazy-loading
* Java / Spring Boot: Powers core domain services
* Elasticsearch: Ensures 99th-percentile search response under 800 ms
* PostgreSQL: Stores relational data within EU residency constraints

## Rationale
This architecture decouples domain UI modules within a high-performance React SPA while leveraging robust backend services. It strictly enforces EU data residency and optimizes search performance.