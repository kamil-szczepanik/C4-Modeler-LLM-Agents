## Overview
[Modernizes a regional insurer's 30-year-old mainframe claims system via a hybrid cloud platform while the legacy system processes ongoing claims.]

## Key Elements
- Routing & Auth Controller (TypeScript)
- Claim Aggregator Service
- UI Adaptation Layer
- Feature Flag & Routing Dispatcher
- Claims Core Service (Java/Spring Boot on Azure App Service)
- Mainframe Integration Adapter (Azure App Service Worker)
- Azure API Management
- Azure SQL Database
- Azure Service Bus
- Azure App Configuration & Azure Key Vault

## Relationships
- Adjuster Workspace -> Claims BFF: Sends requests [HTTPS/REST]
- Routing & Auth Controller -> Claim Aggregator Service: Invokes [In-memory]
- Claim Aggregator Service -> Feature Flag & Routing Dispatcher: Evaluates [In-memory]
- Feature Flag & Routing Dispatcher -> Claims Core Service: Forwards modern requests [HTTPS/REST]
- Feature Flag & Routing Dispatcher -> Mainframe Integration Adapter: Forwards legacy requests [HTTPS/REST]
- Claim Aggregator Service -> Azure SQL Database: Reads/writes UI state [TDS/Managed Identities]

## Technology Stack
- Node.js / Express: Powers the Claims BFF container for lightweight I/O handling
- Azure App Service: Hosts the BFF with deployment slots for zero-downtime blue/green deployments
- OpenTelemetry: Provides distributed tracing across hybrid infrastructure
- Azure App Configuration: Centralizes dynamic feature flags for incremental claim type migration
- Azure Key Vault & Managed Identities: Secures secrets without environment variable exposure

## Rationale
[This hybrid architecture enables incremental claim type migration while keeping the mainframe as the system of record. It guarantees sub-2-second adjuster response times via caching and circuit breakers despite slow mainframe dependencies.]