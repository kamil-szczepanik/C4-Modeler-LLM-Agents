## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. The system leverages an optimized API Gateway and Core Domain Service architecture to guarantee high-performance search responses.

## Key Elements
- Web Application (SPA): React, Nginx
- API Gateway: Spring Cloud Gateway, Java, Netty
- Core Domain Service: Spring Boot, Java
- Search Service: OpenSearch
- Caching Layer: Redis, Caffeine
- Message Broker: Apache Kafka
- Database: PostgreSQL
- External Systems: EU-Tenant Identity Provider (IdP), EU-Hosted Payment Gateway, Notification Service, Digital Content Repository / DRM Provider

## Relationships
- Web Application (SPA) -> SSL/TLS Termination: Initiates secure connection [HTTPS/TLS 1.3]
- Authentication & Authorization Filter -> EU-Tenant Identity Provider (IdP): Validates tokens [REST/TLS]
- Routing & Load Balancing Filter -> Core Domain Service: Forwards validated requests [REST/TLS]
- Routing & Load Balancing Filter -> Search Service: Forwards search queries under 800ms SLA [REST/TLS]
- Rate Limiting Filter <-> Caching Layer (Redis): Reads/writes rate limit counters [TCP/Redis Protocol]
- Response Caching Component <-> Caching Layer (Redis): Retrieves cached catalogue payloads [TCP/Redis Protocol]
- API Analytics & Telemetry Filter -> EU-Hosted Monitoring Backend: Exports tracing and metrics [OTLP/gRPC]

## Technology Stack
- Spring Cloud Gateway & Java: Powers the API Gateway routing and filtering mechanisms
- Netty: Handles SSL/TLS termination for secure EU-compliant transport
- Spring Security: Enforces authentication and RBAC validation
- Bucket4j & Redis: Implements distributed rate limiting for traffic protection
- Resilience4j: Provides circuit breaking to prevent cascading failures
- Caffeine & Redis: Delivers edge response caching for sub-800ms search performance
- OpenTelemetry: Collects metrics and traces for EU-hosted monitoring

## Rationale
This component-level gateway architecture ensures strict adherence to EU data residency rules while utilizing edge caching and circuit breaking to satisfy the sub-800ms search SLA (R-05).