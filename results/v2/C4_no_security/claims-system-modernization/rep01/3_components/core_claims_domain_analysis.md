## Overview
[The system modernizes a 30-year-old mainframe claims system through a hybrid architecture, gradually migrating claim types while maintaining legacy processing. It uses .NET components deployed on Azure to deliver fast, secure online claim submissions and adjuster workflows.]

## Key Elements
* Claim Routing & Feature Flag Component (.NET / C#, MediatR)
* Claim Processing Engine (.NET / C#, Domain-Driven Design)
* Idempotency & Audit Manager (.NET / C#, EF Core)
* Reporting & Analytics Adapter (.NET / C#, MassTransit)
* Operational Data Store (Azure Database for PostgreSQL)
* Infrastructure & Messaging (Azure Container Apps, Azure Service Bus)

## Relationships
* Adjuster BFF -> Claim Routing Component [gRPC]
* Claim Routing -> Claim Processing Engine [In-Process, MediatR]
* Claim Processing Engine -> Idempotency Manager [In-Process]
* Idempotency Manager -> Operational Data Store [TLS, TCP]
* Claim Processing Engine -> Reporting & Analytics Adapter [In-Process, MediatR]
* Reporting & Analytics Adapter -> Azure Service Bus [AMQP]

## Technology Stack
* .NET / C#: Core component implementation providing strong typing and enterprise maturity
* Azure Container Apps: Simplifies cloud deployment for a team with limited cloud experience
* Azure Database for PostgreSQL: Relational storage supporting distributed leasing and consistency
* Azure Service Bus: Asynchronous messaging via AMQP to protect performance during peak loads

## Rationale
[This architecture decouples modern claim processing from the legacy mainframe while ensuring strict consistency and sub-2-second response times. Incremental migration and rapid rollback capabilities are safely managed through dynamic feature flagging and containerized cloud deployment.]