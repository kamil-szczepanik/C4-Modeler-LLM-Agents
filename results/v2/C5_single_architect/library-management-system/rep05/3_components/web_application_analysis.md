## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. The system ensures EU-only data residency and meets high-performance search requirements.

## Key Elements
- Library Patron and Librarian / Staff (Users)
- Web Application (React 18, TypeScript, Vite, Nginx)
- API Gateway (Spring Cloud Gateway / Kong)
- Core Domain Service (Java, Spring Boot)
- Search Service (Python, FastAPI, Elasticsearch)
- Background Worker Service (Python/Celery or Java/Spring Batch)
- PostgreSQL Database and Redis Cache

## Relationships
- Library Patron -> Web Application: Accesses self-service portals [HTTPS]
- Librarian / Staff -> Web Application: Manages cataloging and circulation via Admin UI [HTTPS]
- Web Application -> API Gateway: Calls backend APIs [HTTPS/JSON]

## Technology Stack
- React 18 with TypeScript: Ensures strict typing for complex domain models and component safety
- Vite and Nginx: Provides fast asset bundling and static asset serving
- TanStack Query (React Query): Manages server state and client-side caching to meet the <800ms search response requirement (R-05)
- Zustand / React Context: Manages global UI states, roles, and localization
- PostgreSQL and Elasticsearch: Handles relational persistence and rapid catalog search within EU constraints

## Rationale
This architecture cleanly separates the responsive client-side SPA from backend domain services while leveraging localized caching to satisfy strict performance metrics. The technology choices strictly adhere to EU data residency and rapid search constraints.