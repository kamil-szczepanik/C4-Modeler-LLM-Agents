## Overview
The Library Management System is a solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. The architecture enforces strict EU-only data residency and maintains a 99th-percentile search response time under 800 ms.

## Key Elements
- **Users**: Patron, Staff
- **External Systems**: Identity Provider, External Payment Gateway, National Library Registry, Notification Service, Digital Content Delivery Provider, External SIEM/Monitoring
- **Containers**: Web Application (React, CDN), API Gateway (Kong/Envoy), Core Services Container (Java, Spring Boot), Search Container (Elasticsearch), Database (PostgreSQL), Caching Layer (Redis), Async Worker Container, Integration Worker Container, Search Worker Container (Debezium/CDC), Message Broker (RabbitMQ)
- **API Gateway Components**: SSL/TLS Termination & Geo-Routing Terminator, Auth & Rate Limiting Filter, Route Dispatcher, Request Transformation Engine, Circuit Breaker & Fallback Manager, Analytics & Logging Collector

## Relationships
- Web Application -> API Gateway: Sends API requests [HTTPS/REST/GraphQL/HTTP/2]
- Identity Provider -> API Gateway: Token validation via OAuth2/OIDC introspection [HTTPS]
- API Gateway -> Caching Layer (Redis): Implements token blacklisting, rate-limit tracking, and fallback content [RESP/TCP]
- API Gateway (Route Dispatcher) -> Core Services Container: Routes validated and transformed business traffic [gRPC/HTTP/2]
- API Gateway (Route Dispatcher) -> Search Container: Routes optimized catalogue search queries [gRPC/HTTP/2]
- API Gateway (Analytics & Logging Collector) -> External SIEM/Monitoring: Exports audit and observability data [OTLP/HTTPS] within EU boundaries

## Technology Stack
- **API Gateway**: Kong (built on Envoy) for native plugin ecosystems, rate-limiting, and JWT validation.
- **Protocols**: HTTPS, HTTP/2, and gRPC for low-overhead multiplexing and performance (<800ms search requirement).
- **Caching & State**: Redis for rate-limiting, token blacklisting, and fallback responses.
- **Telemetry**: OTLP/HTTPS for secure, EU-compliant monitoring and logging.

## Rationale
This architecture uses Kong/Envoy with optimized internal gRPC routing to achieve the strict <800ms search latency requirement. Edge termination and OTLP telemetry enforce strict EU-only data residency constraints.