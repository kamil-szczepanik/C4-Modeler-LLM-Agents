## Overview
The Core Domain Service provides business logic, circulation management, and EU-compliant audit logging for the Library Management System. It handles item cataloguing, loan policies, and secure self-service portal operations.

## Key Elements
- **Core Domain Service** (Container, Java/Spring Boot)
- **Circulation Manager Component** (Spring Bean/Service)
- **Catalogue Manager Component** (Spring Bean/Service)
- **Audit Logger Component** (Spring Bean/Data JPA)
- **Event Publisher Component** (Spring Cloud Stream / RabbitMQ Template)
- **Security Interceptor Component** (Spring Security / gRPC Interceptor)
- **PostgreSQL Database** (Container, PostgreSQL with dedicated audit schema)
- **RabbitMQ Message Broker** (Container, RabbitMQ with DLQ)

## Relationships
- `API Gateway` -> `Security Interceptor Component`: Forwards requests [gRPC with mTLS]
- `Security Interceptor` -> `Circulation Manager` & `Catalogue Manager`: Authorizes validated gRPC calls
- `Core Domain Service components` -> `PostgreSQL Database`: Persists transactional state [JDBC over TLS 1.3]
- `Audit Logger` -> `PostgreSQL Database`: Writes to a restricted, append-only schema [JDBC over TLS 1.3]
- `Core Domain Service` -> `RabbitMQ Message Broker`: Publishes domain events like `ItemCheckedOut` [AMQP 0-9-1 over TLS 1.3]

## Technology Stack
- **Java / Spring Boot**: Enforces strict domain boundaries and transaction management.
- **Spring Security / gRPC Interceptor**: Validates method-level OAuth2/JWT scopes for roles.
- **Spring Data JPA**: Manages database persistence and object-relational mapping.
- **PostgreSQL**: Stores operational data and isolated, immutable audit logs.
- **RabbitMQ**: Handles asynchronous domain event dispatching with circuit breakers and dead-letter queues.

## Rationale
This architecture isolates the immutable audit logger into a dedicated database schema with least-privilege permissions, ensuring strict EU data residency and GDPR compliance. Furthermore, bounded thread pools and mTLS protect core circulation performance and transaction reliability.