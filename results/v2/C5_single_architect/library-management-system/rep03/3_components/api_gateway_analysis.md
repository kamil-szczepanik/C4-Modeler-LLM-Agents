## Overview
The Library Management System provides cataloging, circulation, and self-service portal capabilities for public and academic libraries. It relies on an EU-hosted microservices architecture to meet strict data residency and sub-800ms search performance requirements.

## Key Elements
- Library Patron and Library Staff (Users)
- Web Application (React, TypeScript)
- API Gateway (Spring Cloud Gateway, Project Reactor)
- Catalogue Service, Circulation Service, Digital Content Proxy Service (Java, Spring Boot)
- PostgreSQL (Database), Redis (Cache/Rate Limiting), Elasticsearch (Search), RabbitMQ (Message Broker)
- External Systems: Payment Gateway, Digital Content Provider, Notification Service

## Relationships
- Web Application -> API Gateway: Sends API requests [HTTPS/JSON]
- API Gateway -> Catalogue Service / Circulation Service / Digital Content Proxy Service: Routes requests [gRPC over TLS]
- Authentication & Authorization Component -> Redis: Validates rate limits and tokens [TCP]

## Technology Stack
- Spring Cloud Gateway: Chosen for native Spring Security integration and Project Reactor performance.
- Resilience4j: Implements circuit breaking and retries natively within Spring Cloud Gateway.
- Redis: Backs rate limiting and token checks.
- Java / Spring Boot: Powers core business microservices.

## Rationale
This architecture meets EU data residency constraints and sub-800ms search SLAs through reactive routing and centralized resilience patterns. Spring Cloud Gateway and Resilience4j effectively isolate downstream services from traffic surges.