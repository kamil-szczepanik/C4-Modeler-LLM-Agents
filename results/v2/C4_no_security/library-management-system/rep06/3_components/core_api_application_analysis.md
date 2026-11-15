## Overview
The Library Management System provides catalogue management, circulation workflows, and self-service portals for public and academic libraries. The Core API Application manages domain logic, ensuring EU-only data residency and high-performance search capabilities.

## Key Elements
- **Core API Application:** Spring Boot / Java monolithic container deployed on Kubernetes
- **Catalog & Circulation Controller:** Spring MVC component for item management and workflows
- **Security & Audit Interceptor:** Spring Security / AOP component for GDPR compliance and audit logging
- **Payment & External Integration Service:** Manages third-party payment and digital content integrations with Resilience4j
- **Catalog Search Component:** Handles catalogue searches with Resilience4j circuit breaker and database fallback
- **Data Access Repository:** Spring Data JPA component managing connections to PostgreSQL read replicas

## Relationships
- API Gateway -> Core API Application: Routes external requests [HTTPS]
- Core API Application -> Primary Database: Queries and updates transactional data [gRPC/REST over TLS]
- Core API Application -> Search Engine: Performs catalogue searches [gRPC/REST over TLS]
- Core API Application -> APM Tool: Streams performance metrics [OpenTelemetry]

## Technology Stack
- **Spring Boot / Java:** Core framework for building scalable domain logic and controllers
- **Resilience4j:** Implements circuit breakers and retries for external services and search degradation
- **HikariCP:** Provides connection pooling to protect the database during fallback queries
- **OpenTelemetry:** Streams distributed tracing telemetry for performance monitoring

## Rationale
This architecture uses stateless containerization and Resilience4j circuit breakers to guarantee high availability during peak academic periods. Dedicated audit components and read-replica routing enforce strict EU data residency regulations while meeting sub-800ms search requirements.