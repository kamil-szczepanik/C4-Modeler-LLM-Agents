## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It ensures EU-only data residency and meets strict performance constraints like 99th-percentile search responses under 800 ms.

## Key Elements
- Library Patrons and Library Staff (Users)
- Web Application (React/TypeScript SPA)
- API Gateway (Spring Cloud Gateway container)
- Core Domain Service (Java/Spring Boot)
- Search Service (Java with Elasticsearch)
- Identity Provider, Payment Gateway, Notification Service, National Library Registry (External Systems)
- API Gateway Components: Routing & Load Balancing Component, JWT Validation Filter, Rate Limiting & Throttling Component, Circuit Breaker Component

## Relationships
- Web Application -> API Gateway: Authenticates and routes calls [HTTPS/REST/WebSocket]
- API Gateway -> Identity Provider: Validates tokens [HTTPS/REST]
- Routing Filter -> Core Domain Service: Routes validated commands/queries [gRPC]
- Circuit Breaker -> Search Service: Protects search endpoints [gRPC]

## Technology Stack
- Spring Cloud Gateway: Selected for native reactive routing, dynamic service discovery, and Java ecosystem alignment
- Elasticsearch: Powers fast catalog searches to achieve the <800ms latency requirement
- Resilience4j: Integrated for circuit breaking to prevent cascading failures
- WebClient: Used for non-blocking reactive key caching during JWT validation

## Rationale
This architecture uses reactive, non-blocking routing and caching to minimize latency, satisfying the high-performance search constraint. Spring Cloud Gateway and integrated resilience patterns secure the edge while supporting EU-only data residency.