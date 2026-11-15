## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries within EU data residency constraints. The API Gateway container manages secure, non-blocking routing and edge security for all ingress traffic.

## Key Elements
- **Library Patron & Librarian / Staff**: Primary human users interacting with the system.
- **Web Application**: Frontend UI built with React, TypeScript, and Nginx.
- **API Gateway**: Edge router built with Spring Cloud Gateway (Java, Spring WebFlux).
- **Core Domain Service & Search Service**: Backend business logic and search containers.
- **Redis Cache**: In-memory data store for rate limiting.
- **External Systems**: Payment Gateway, Notification Service, Digital Rights Management (DRM) Provider.

## Relationships
- **Web Application -> SSL Termination & CORS Handler**: Ingress traffic [HTTPS/JSON]
- **API Gateway -> Search Service**: Routes search queries [gRPC]
- **API Gateway -> Core Domain Service**: Routes circulation requests [gRPC]
- **API Gateway -> Redis Cache**: Evaluates rate limits [Redis Protocol]
- **Authentication & Authorization Filter -> Notification Service**: Dispatches audit events [HTTPS/JSON]

## Technology Stack
- **Spring Cloud Gateway (Java / Spring WebFlux)**: Chosen for non-blocking performance to meet the <800ms search SLA.
- **Spring Security / OAuth2**: Validates JWT tokens for secure authentication.
- **Redis**: Backs the rate limiter to protect downstream services.
- **gRPC**: Protocol for high-performance internal container communication.

## Rationale
This architecture leverages a reactive Java edge gateway and gRPC protocols to achieve high-performance routing, ensuring search responses remain under 800ms. Distributed components and EU-hosted infrastructure satisfy strict data residency and security constraints.