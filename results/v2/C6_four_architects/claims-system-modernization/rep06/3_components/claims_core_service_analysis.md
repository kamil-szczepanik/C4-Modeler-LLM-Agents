## Overview
The Claims Core Service is a .NET 8 microservice running in Azure Container Apps that processes modern claims while coordinating with a legacy mainframe. It enables gradual claim type migration and rapid rollbacks to meet strict hybrid modernization constraints.

## Key Elements
* Claim Submission Controller (ASP.NET Core Web API)
* Claim Routing Engine (C# Component)
* Claim Domain Model & Engine (C# Class Library)
* Mainframe Anti-Corruption Layer - ACL (C# Component)
* Persistence Repository (EF Core Context)
* Integration Event Publisher/Subscriber (MassTransit .NET)
* Workflow Orchestration Service (C# Component)
* Document Management Client (Typed HttpClient)
* Claim Caching & Read Model Component (Redis / Memory)

## Relationships
* Claim Submission Controller -> Claim Routing Engine: Forwards raw submissions [In-process]
* Claim Routing Engine -> Claim Domain Model & Engine: Routes modernized claim types [In-process]
* Claim Routing Engine -> Mainframe Anti-Corruption Layer: Routes legacy claim types [In-process]
* Claim Domain Model & Engine -> Persistence Repository: Performs transactional reads/writes [TDS via EF Core]
* Claim Domain Model & Engine -> Integration Event Publisher/Subscriber: Publishes domain events [AMQP via Azure Service Bus]
* Workflow Orchestration Service -> Claim Caching & Read Model Component: Updates read models [In-process / Redis]
* Document Management Client -> Document Management System: Uploads and retrieves attachments [HTTPS]
* Mainframe Anti-Corruption Layer -> Mainframe Integration Adapter: Syncs legacy data [gRPC/HTTP]

## Technology Stack
* .NET 8 / C#: Chosen to leverage existing team expertise and minimize the cloud learning curve
* Azure Container Apps: Hosts the microservice with scalable, managed infrastructure
* Entity Framework Core & Azure SQL Database: Provides reliable relational persistence
* MassTransit & Azure Service Bus: Ensures asynchronous, reliable event-driven messaging
* Azure Cache for Redis: Implements CQRS-lite read models to guarantee sub-2-second UI responses

## Rationale
This architecture isolates legacy dependencies through dedicated routing and translation components, allowing seamless claim-by-claim migration and one-day rollbacks. Furthermore, internal caching and decoupled messaging satisfy strict performance and consistency constraints without overwhelming expensive mainframe interfaces.