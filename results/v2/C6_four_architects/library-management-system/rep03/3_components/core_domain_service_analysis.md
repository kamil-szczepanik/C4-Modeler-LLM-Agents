## Overview
- Library Management System for public and academic libraries to catalogue items and manage circulation.
- Designed as a modular Java Spring Boot core domain service with strict EU data residency enforcement.

## Key Elements
- Integration Facade Component (Spring `@Controller`/`@GrpcService`)
- Catalog Management Component (Spring `@Service`)
- Circulation & Lending Engine (Spring `@Service`)
- Patron Account Manager (Spring `@Service`)
- Search Integration Component (Spring `@Service`)
- Data Access Layer Component (Spring Data JPA)
- Event Publisher/Consumer Component (Spring `@Component`)
- External Systems: PostgreSQL Database, Elasticsearch Search Service, Distributed Cache (Redis), Notification & Event Bus (Apache Kafka)

## Relationships
- API Gateway -> Integration Facade Component [gRPC over TLS]
- Integration Facade Component -> Domain Services [In-memory Method Calls]
- Domain Services -> Data Access Layer Component [In-memory Method Calls]
- Data Access Layer Component -> PostgreSQL Database [JDBC]
- Search Integration Component -> Elasticsearch Search Service [HTTP/REST over TLS]
- Circulation & Lending Engine -> Distributed Cache [TCP / Spring Data Redis]
- Event Publisher/Consumer Component -> Apache Kafka [Kafka Wire Protocol]

## Technology Stack
- Java / Spring Boot: Core container runtime for robust business logic
- Spring Data JPA / JDBC: Centralized database access for strict EU data residency enforcement
- Elasticsearch: High-performance search to meet <800ms response requirements
- Apache Kafka: Asynchronous event publishing and consumption
- gRPC over TLS: High-performance inbound transport from API Gateway

## Rationale
- Centralized Data Access Layer strictly enforces EU-only data residency constraints.
- Modular Spring `@Service` decomposition ensures high cohesion, maintainability, and sub-millisecond circulation validation via Redis.