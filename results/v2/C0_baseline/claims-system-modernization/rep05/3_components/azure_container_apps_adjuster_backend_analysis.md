## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure-based platform while maintaining uninterrupted core operations. It ensures zero data loss, sub-2-second adjuster screen loads, and single sign-on authentication.

## Key Elements
- React Claims Web App
- Azure API Management / Migration Router
- Azure Container Apps (Adjuster Backend)
- Claim Management Component
- Read-Side Query Component
- Integration Adapter Component
- Security & Context Middleware
- Azure Cosmos DB
- Azure Service Bus
- Azure Key Vault
- Legacy Mainframe
- Azure Entra ID

## Relationships
- React Claims Web App -> Azure API Management / Migration Router: Forwards web traffic [HTTPS/TLS 1.3]
- Azure API Management / Migration Router -> Security & Context Middleware: Routes validated requests [HTTPS]
- Security & Context Middleware -> Claim Management Component: Passes authenticated context [In-Process]
- Claim Management Component -> Integration Adapter Component: Dispatches domain events [In-Process]
- Integration Adapter Component -> Azure Service Bus: Publishes asynchronous events [AMQP]
- Read-Side Query Component -> Azure Cosmos DB: Queries local projections [TCP/SQL]
- Integration Adapter Component -> Legacy Mainframe: Syncs claim data [Custom Protocol]

## Technology Stack
- Azure Container Apps: Scalable runtime for backend microservices, chosen for low cloud experience overhead.
- ASP.NET Core Minimal APIs: Core framework for implementing adjuster business logic.
- CQRS Pattern & Entity Framework Core: Isolates read models to guarantee sub-2s responses (R-05).
- MassTransit & Azure Service Bus: Handles asynchronous messaging and domain events.
- Azure Entra ID & JWT: Enforces single sign-on and role-based access control (R-07).
- Azure Cosmos DB: Provides low-latency storage for local claim projections.
- Azure Key Vault: Secures runtime secrets using Managed Identities.

## Rationale
The hybrid CQRS architecture isolates sub-2s performance requirements from slow legacy mainframe responses while ensuring seamless business continuity and a rapid one-day fallback. Furthermore, managed Azure services minimize operational complexity for a team with limited cloud experience.