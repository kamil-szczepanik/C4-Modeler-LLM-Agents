## Overview
[The system is an Insurance Claims Modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid cloud architecture. Its core purpose is to enable online claim submission and modernized adjuster workflows while maintaining seamless data consistency during a 3-year migration.]

## Key Elements
- **Claims Core Service**: Java/Spring Boot application hosted on Azure App Service.
- **Integration Router / Facade**: Component managing feature-flagged routing for claim types.
- **Claim Processing Engine**: Component executing domain logic via Spring Data JPA.
- **Asynchronous Event Handler**: Component processing domain events via Spring Messaging.
- **Claim State Cache**: Azure Cache for Redis for read-heavy operations.
- **Database**: Azure SQL Database.
- **Message Broker**: Azure Service Bus.

## Relationships
- Claims API Gateway -> Integration Router: REST / HTTPS / OIDC / OAuth2
- Integration Router -> Claim Processing Engine: In-process Java method calls
- Integration Router -> Claim State Cache: Redis / TCP
- Claim Processing Engine -> Claim State Cache: Redis / TCP
- Claim Processing Engine -> Database: JDBC / TDS / Managed Identities
- Asynchronous Event Handler -> Message Broker: AMQP / Managed Identities

## Technology Stack
- **Java / Spring Boot**: Foundation for the Claims Core Service microservice and internal components.
- **Azure App Service**: Hosting platform providing managed runtime and blue-green deployment capabilities.
- **Azure SQL Database**: Relational datastore utilizing Transparent Data Encryption (TDE) with Customer-Managed Keys.
- **Azure Cache for Redis**: In-memory caching tier enforcing TLS-only ports and VNet integration.
- **Azure Service Bus**: Asynchronous message broker utilizing Managed Identities.

## Rationale
[This architecture fits requirements by using an Integration Router to enable a rapid 1-day rollback of claim types (R-06) and a Redis Claim State Cache to mitigate slow mainframe response times under 2 seconds (R-05). Managed Azure services and automated controls compensate for the team's low cloud experience while enforcing zero-trust security and consistency (R-04, R-07).]