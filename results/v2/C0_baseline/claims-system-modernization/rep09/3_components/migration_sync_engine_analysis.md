## Overview
The Migration & Sync Engine is a core microservice container managing data synchronization and gradual migration between a legacy COBOL/DB2 mainframe and a modern Azure-based claims platform. It ensures seamless, zero-loss hybrid operations while enabling independent claim-type migrations and rapid rollbacks.

## Key Elements
- Migration & Sync Engine (.NET, Azure Container Apps)
- Sync Coordinator (MassTransit, Microsoft.FeatureManagement, Entity Framework Core)
- Transformation Adapter (AutoMapper, Polly)
- Reconciliation Worker (.NET background service)
- Routing & Policy Engine (Azure App Configuration)
- Migration Operator Dashboard (React, Azure Static Web Apps)

## Relationships
- Migration & Sync Engine -> Azure Service Bus: Publishes and consumes sync events [AMQP]
- Migration & Sync Engine -> Azure API Management (APIM): Connects to legacy mainframe [mTLS, IP whitelisting, TLS 1.3]
- Migration & Sync Engine -> Azure Key Vault / Azure App Configuration: Retrieves secrets and runtime feature flags [Managed Identities]
- Migration Operator Dashboard -> Migration & Sync Engine: Exposes sync metrics and rollback controls [HTTPS / Azure AD RBAC]

## Technology Stack
- .NET on Azure Container Apps: Chosen for enterprise readiness, container orchestration, and team skill alignment.
- MassTransit (.NET): Implements robust messaging patterns over Azure Service Bus.
- Entity Framework Core with Outbox Pattern: Ensures zero-loss transactions (R-04) across hybrid boundaries.
- Polly: Provides resilient circuit breakers for fragile mainframe calls during batch windows.
- Microsoft.FeatureManagement & Azure App Configuration: Enables dynamic runtime claim-type routing and 1-day rollbacks (R-06).

## Rationale
This architecture decouples the modern cloud platform from rigid mainframe constraints by isolating schema transformations and managing eventual consistency independently in Azure. It empowers operations teams with secure, runtime feature toggles and audit trails to meet strict compliance and hybrid migration deadlines.