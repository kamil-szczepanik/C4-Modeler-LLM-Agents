## Overview
The Library Management System provides cataloguing, circulation, and self-service portal capabilities for public and academic libraries. It ensures EU-only data residency and meets strict sub-800ms search performance requirements.

## Key Elements
- Patrons and Librarians (Users)
- Web Application (React, TypeScript)
- API Gateway (Kong / Nginx)
- Core Business Service (Java / Spring Boot)
- Search Service (Elasticsearch)
- Database (PostgreSQL)
- Redis Cache
- Notification Worker (Node.js)
- External Systems: Payment Gateway, e-Book Vendors, Notification Service, Enterprise Search Service

## Relationships
- Web App -> API Gateway via HTTPS/JSON
- API Gateway -> Core Business Service & Search Service via gRPC/REST
- Core Business Service -> Database via TCP
- Core Business Service -> Redis Cache via TCP/RESP
- Core Business Service -> External Payment Gateway via HTTPS
- Notification Worker -> External Notification Service via HTTPS/AMQP

## Technology Stack
- React, TypeScript: Frontend web application for responsive user interfaces.
- Java, Spring Boot: Robust backend for core cataloguing and circulation business logic.
- Elasticsearch: Dedicated search engine ensuring 99th-percentile search response < 800 ms (R-05).
- PostgreSQL: Primary relational database restricted to EU infrastructure for data residency constraints.
- Redis: In-memory cache to reduce database load during high-traffic browsing.
- Node.js: Asynchronous background worker for decoupled notification processing.

## Rationale
This architecture decouples heavy search operations into Elasticsearch to achieve the sub-800ms performance mandate. Additionally, localizing PostgreSQL and Elasticsearch within EU infrastructure strictly satisfies regional data residency constraints.