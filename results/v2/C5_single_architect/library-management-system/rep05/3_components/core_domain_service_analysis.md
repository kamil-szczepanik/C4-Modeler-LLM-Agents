## Overview
The Library Management System provides cataloguing, circulation management, and self-service portals for public and academic libraries. It ensures strict EU-only data residency and high-performance search responses under 800ms.

## Key Elements
- **Users**: Library Patron, Librarian / Staff
- **External Systems**: Payment Gateway, Notification Service, Digital Rights Management (DRM) Provider
- **Containers**: Web Application, API Gateway, Core Domain Service, Search Service, Background Worker Service, PostgreSQL Database, Redis Cache
- **Core Domain Components**: Book/Item Management Component, Circulation Engine Component, Domain Event Publisher, Security/Auth Component

## Relationships
- **Core Domain Service -> PostgreSQL Database**: JDBC [TCP] for EU-resident relational persistence
- **Core Domain Service -> Redis Cache**: Accesses cache for session management [TCP]
- **Core Domain Service -> Search Service**: Apache Kafka / Spring Cloud Stream [AMQP/TCP] for asynchronous catalogue synchronization
- **Circulation Engine -> Book/Item Management**: In-process method calls [Java]

## Technology Stack
- **Web Application**: React, TypeScript, Nginx for client-side portals
- **API Gateway**: Spring Cloud Gateway / Kong for request routing
- **Core Domain & Search**: Java, Spring Boot, Spring Data JPA, Spring Security, Python, FastAPI, Elasticsearch
- **Messaging & Caching**: Apache Kafka, Spring Cloud Stream, Redis
- **Persistence**: PostgreSQL Database configured for EU data residency

## Rationale
Decomposing the Core Domain Service into specialized Java components maintains clean transactional boundaries within the Spring Boot container. Utilizing Apache Kafka for asynchronous indexing protects search performance to meet the 800ms NFR while enforcing strict EU data residency constraints.