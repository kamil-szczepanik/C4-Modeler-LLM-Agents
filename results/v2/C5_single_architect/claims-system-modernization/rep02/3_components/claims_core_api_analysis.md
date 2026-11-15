## Overview
The Claims Core API is a Java-based microservice component decomposing the modern platform's core business logic. It handles migrated claim types while orchestrating data synchronization with the legacy mainframe.

## Key Elements
- **Claim Management Controller**: Spring MVC REST endpoints receiving payloads from the Adjuster Workspace and Migration Router.
- **Claim Domain Service**: Spring Data Domain Service enforcing R-04 consistency constraints using CQRS (Write Model Handler and Read Model Projections).
- **Legacy Anti-Corruption Layer (ACL)**: Spring Integration component translating domain models for unmigrated claim types.
- **Claim Repository**: Spring Data JPA managing transactional persistence in Azure SQL.
- **Event Publisher Component**: Spring Cloud Stream emitting domain events to Azure Service Bus.

## Relationships
- Adjuster Workspace / Migration Router -> Claim Management Controller: External REST/JSON calls over HTTPS.
- Claim Domain Service -> Claim Repository: JDBC persistence calls to Azure SQL.
- Claim Domain Service -> Legacy Anti-Corruption Layer: Internal method delegation for unmigrated types.
- Event Publisher Component -> Azure Service Bus: Asynchronous event publishing using AMQP.

## Technology Stack
- Java & Spring Boot: Selected for enterprise maturity to mitigate the team's limited cloud experience.
- Spring MVC: Used for exposing robust REST APIs.
- Spring Data JPA & Azure SQL: Provides transactional persistence guaranteeing zero data loss.
- Spring Cloud Stream & Azure Service Bus: Handles asynchronous, decoupled event-driven messaging.

## Rationale
This architecture uses proven enterprise Java frameworks to lower delivery risk for a team with minimal cloud experience. The CQRS pattern and decoupled event publishing ensure high performance and reliable hybrid integration with the legacy mainframe.