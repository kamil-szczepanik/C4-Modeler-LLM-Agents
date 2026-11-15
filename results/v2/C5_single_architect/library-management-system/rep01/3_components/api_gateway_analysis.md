## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. The architecture enforces EU-only data residency while maintaining high-performance search responses under 800 ms.

## Key Elements
- Patrons / Library Members and Librarians / Staff (Users)
- Web Application (React, TypeScript)
- API Gateway (Kong / Nginx) containers: SSL/TLS Termination Component, Authentication & Authorization Component, Routing & Load Balancing Component, Rate Limiting & Throttling Component
- Core Business Service (Java, Spring Boot)
- Search Service (Elasticsearch)
- Database (PostgreSQL)
- Redis Cache (Redis)
- Notification Worker (Node.js)
- External Systems: External Payment Gateway, Digital Content Providers / e-Book Vendors, Notification Service, External Enterprise Search Service

## Relationships
- Patrons / Librarians -> SSL/TLS Termination Component: Inbound traffic [HTTPS]
- Web Application -> Authentication & Authorization Component: Validates credentials [HTTPS/JSON]
- SSL/TLS Termination Component -> Authentication & Authorization Component: Passes decrypted requests [Internal]
- Authentication & Authorization Component -> Routing & Load Balancing Component: Forwards validated requests [Internal]
- Routing & Load Balancing Component -> Core Business Service: Forwards authenticated traffic [gRPC]
- Routing & Load Balancing Component -> Search Service: Forwards search queries [gRPC]
- Routing & Load Balancing Component -> Redis Cache: Checks rate limits [RESP/TCP]

## Technology Stack
- Kong / Nginx & Lua: API Gateway core and routing plugins for edge traffic management
- OpenSSL / Nginx: SSL/TLS termination and perimeter security enforcing EU data residency
- Kong JWT Plugin & OAuth2: Edge-based authentication to offload backend services
- Redis: Backs rate limiting and throttling to protect search performance SLAs (R-05)
- Java / Spring Boot: Core Business Service implementation
- Elasticsearch: Dedicated Search Service ensuring low-latency catalog queries (< 800 ms)
- React & TypeScript: Web Application frontend
- PostgreSQL: Persistent data storage within EU boundary

## Rationale
Decomposing the API Gateway isolates edge security, SSL termination, and rate limiting to protect downstream services. This guarantees the 800ms search SLA while strictly enforcing EU data residency constraints.