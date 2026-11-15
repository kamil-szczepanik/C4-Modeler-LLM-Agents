## Overview
[The Insurance Claims Modernization platform gradually replaces an on-premise mainframe system with a hybrid cloud-native platform while ensuring continuous, zero-loss claim processing during a 3-year transition.]

## Key Elements
- Claim Orchestrator Component (.NET 8 / MediatR)
- Payment & Notification Coordinator Component (.NET 8 / HTTP Client)
- Migration & Routing Client Component (.NET 8 / gRPC Client)
- Data Persistence Component (.NET 8 / Azure Cosmos DB SDK)
- Feature Flag / Migration Router (Azure Container Apps)
- Payment Gateway (External system)
- Core Notification Service (External system)
- Document & Audit Store (Azure Blob Storage & Azure Cosmos DB)

## Relationships
- Claim Orchestrator Component -> Migration & Routing Client Component (In-memory MediatR dispatch)
- Migration & Routing Client Component -> Feature Flag / Migration Router (Internal gRPC)
- Payment & Notification Coordinator Component -> Payment Gateway (HTTPS with OAuth 2.0 and idempotency tokens)
- Payment & Notification Coordinator Component -> Core Notification Service (Asynchronous Webhooks via Azure Event Grid (HTTPS))
- Data Persistence Component -> Document & Audit Store (HTTPS / TLS 1.3 via Azure Cosmos DB SDK)

## Technology Stack
- .NET 8 / C#: Core component implementation language offering strong maintainability for the team.
- MediatR: In-memory dispatching for low latency and clean separation of concerns.
- Polly: Resilience and circuit-breaking for external payment integrations.
- FluentValidation: Strict input schema validation for security hardening.
- OpenTelemetry & Azure Application Insights: Standardized telemetry and structured logging with PII sanitization.
- Azure Key Vault: Secure secret and credential management.

## Rationale
[This component-level architecture enforces strict separation of concerns and robust security controls within Azure Container Apps. It provides the necessary telemetry, resilience, and idempotency guarantees required to safely migrate complex insurance workflows while mitigating the team's limited cloud experience.]