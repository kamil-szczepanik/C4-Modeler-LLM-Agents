## Overview
[The Claims Core API is a modular monolith built on .NET Core and Azure Container Apps that orchestrates claim submissions and routing during a hybrid mainframe modernization. It securely bridges modern cloud interfaces with legacy on-premise systems while ensuring zero claim loss and sub-2-second response times.]

## Key Elements
- Claims Core API (.NET Core modular monolith, Azure Container Apps)
- Claim Submission Component (.NET Core)
- Claim Query & Routing Component (.NET Core)
- Fallback Orchestrator Component (.NET Core)
- Claim Admin & Metadata Component (.NET Core)
- Azure Service Bus (AMQP)
- Claim Read Database (Azure SQL Database)
- Insurer Active Directory (Azure Entra ID Connect)

## Relationships
- Customer Portal App -> Claims Core API: Sends claim submissions [HTTPS / JSON]
- Adjuster Web App -> Claims Core API: Fetches and updates claim data [HTTPS / JSON]
- Claim Submission Component -> Azure Service Bus: Publishes new claim events [AMQP]
- Claim Query & Routing Component -> Claim Read Database: Fetches optimized read models [TDS / TCP]
- Claims Core API -> Insurer Active Directory: Authenticates requests [OIDC / OAuth2 via Entra ID Connect]

## Technology Stack
- .NET Core: Selected for building the modular monolith and internal components due to robust enterprise features and strong typing.
- Azure Container Apps: Chosen to host the API containers, providing managed serverless scaling and built-in health probes for a team with limited cloud experience.
- Azure SQL Database: Utilized for the Claim Read Database to deliver sub-2-second query performance via optimized read models.
- Azure Service Bus: Deployed as an asynchronous message broker to decouple online submissions from mainframe latency using AMQP.
- OpenTelemetry & Polly: Implemented for distributed tracing and circuit breaking to ensure resilience across the hybrid cloud-mainframe boundary.

## Rationale
[This architecture successfully isolates legacy mainframe bottlenecks through asynchronous messaging and feature-flagged routing within a modular monolith. It meets all stringent performance, security, and maintainability requirements while accommodating the team's limited cloud experience.]