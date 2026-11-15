## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within an EU-compliant environment. The system features a modular React-based web application backed by Java and Python microservices to handle high-performance searches and digital asset rendering.

## Key Elements
- **Web Application (SPA)**: React and Nginx container hosting the user interface.
- **API Gateway**: Spring Cloud Gateway (Java) routing external traffic.
- **Core Domain Service**: Spring Boot (Java) handling business logic.
- **Search Service**: OpenSearch providing low-latency catalog queries.
- **Message Broker & Cache**: Apache Kafka and Redis for event streaming and caching.
- **Workers**: Python/Celery containers for notifications, payments, and DRM.
- **External Systems**: EU-Tenant IdP, Payment Gateway, and Digital Content Repository.

## Relationships
- Patrons and Librarians -> Web Application (SPA): Accesses UI via [HTTPS]
- Web Application (SPA) -> API Gateway: Sends API requests via [HTTPS/REST]
- API Gateway -> Core Domain Service & Search Service: Routes internal calls via [gRPC/REST]
- Core Domain Service -> PostgreSQL, OpenSearch, and Redis: Persists and queries data
- Workers -> Notification & Payment Services: Dispatches emails, SMS, and processes transactions

## Technology Stack
- **Frontend**: React (with Zustand/Redux Toolkit, Axios, and React Router) served via Nginx for strict EU data residency.
- **Backend Services**: Java Spring Boot and Python (Celery) for robust microservice execution.
- **Data & Messaging**: PostgreSQL for relational storage, OpenSearch for search, and Apache Kafka for event distribution.
- **Infrastructure**: Redis for caching and OIDC/OAuth2 (`oidc-client-ts`) for authentication.

## Rationale
The microservices architecture with Redis caching ensures 99th-percentile search responses remain under 800 ms to meet performance requirements. Confining state management, telemetry boundaries, and static asset delivery within EU-hosted containers guarantees strict EU-only data residency compliance.