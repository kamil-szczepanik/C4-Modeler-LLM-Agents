## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. The architecture ensures EU-only data residency and meets high-performance search requirements.

## Key Elements
- Patrons / Library Members and Librarians / Staff
- Web Application (React, TypeScript) with internal components: Router / Layout (React Router), Authentication (Auth Context / OAuth2 SDK), Catalogue & Search, Circulation & Self-Service
- API Gateway (Kong / Nginx)
- Core Business Service (Java, Spring Boot)
- Search Service (Elasticsearch)
- Database (PostgreSQL) and Redis Cache (Redis)
- Notification Worker (Node.js)
- External Payment Gateway, Digital Content Providers, Notification Service, External Enterprise Search Service

## Relationships
- Patrons / Librarians -> Router / Layout: Uses [HTTPS]
- Catalogue & Search Component -> API Gateway: Queries search and catalogue data via [HTTPS/JSON]
- Circulation & Self-Service Component -> API Gateway: Executes transactions via [HTTPS/JSON]
- Web Application -> API Gateway: Sends requests to backend services [HTTPS/JSON]

## Technology Stack
- React and TypeScript: Powers the responsive frontend web application
- React Router: Manages navigation and layouts
- OAuth2 SDK: Handles authentication and role-based access
- React Query / SWR: Implements client-side result caching for performance
- Kong / Nginx: Acts as API Gateway
- Java with Spring Boot: Powers Core Business Service
- Elasticsearch: Provides search capabilities
- PostgreSQL: Stores system data within EU boundaries
- Redis Cache: Accelerates frequently accessed data
- Node.js: Powers Notification Worker
- Localized EU CDN: Serves UI assets for data residency compliance

## Rationale
This architecture uses localized EU infrastructure and client-side caching to satisfy strict EU-only data residency constraints. It decouples services to achieve 99th-percentile search responses under 800 ms.