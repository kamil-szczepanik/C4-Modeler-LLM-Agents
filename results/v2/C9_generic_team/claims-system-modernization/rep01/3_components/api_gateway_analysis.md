## Overview
[System: Hybrid Insurance Claims Modernization Platform]
[Core Purpose: Gradually replaces a 30-year-old mainframe claims system with a modern cloud platform while maintaining uninterrupted business operations.]

## Key Elements
- Customers and Brokers
- Claims Adjusters
- On-Premises COBOL/DB2 Mainframe
- Azure Hosted API Gateway
- Claim Ingestion & Validation Module (.NET Core / Modular Monolith)
- Anti-Corruption Layer (ACL) (.NET Core / Modular Monolith)
- Read-Model Cache (Azure Cache / In-Memory Database)
- Data Synchronization Worker (.NET Background Worker)
- Feature Flag Management Module (Azure App Configuration)
- Centralized Observability & Audit Logging Module (Azure Monitor / Application Insights)
- Database Migration & Schema Versioning Module (Flyway / Entity Framework)
- Azure Service Bus
- Azure Key Vault

## Relationships
- Customers and Brokers -> Azure Hosted API Gateway: Submit online claims [HTTPS / mTLS / API Keys]
- Claims Adjusters -> Azure Hosted API Gateway: Handle claims via modern web application [HTTPS / SSO via Azure Active Directory]
- Azure Hosted API Gateway -> Claim Ingestion & Validation Module: Route ingress traffic internally [Internal API]
- Azure Hosted API Gateway -> Read-Model Cache: Serve low-latency claim reads under 2 seconds [Internal Cache Query]
- Azure Hosted API Gateway -> Feature Flag Management Module: Dynamically toggle claim-type routing for rapid rollback [Azure App Configuration]

## Technology Stack
- Azure API Gateway: Edge routing, rate limiting, circuit breaking, response caching, request aggregation, JWT/OAuth2 validation, and error transformation.
- .NET Core: Core business logic, modular monoliths, and background worker implementation.
- Azure Cache / In-Memory Database: Low-latency read model caching to achieve <2s screen loads.
- Azure App Configuration: Dynamic feature flagging for 1-day claim-type rollback.
- Flyway / Entity Framework: Database migration and schema versioning.
- Azure Monitor / Application Insights: Centralized observability, auditing, and distributed tracing.

## Rationale
[This hybrid architecture decouples legacy mainframe constraints from modern cloud components using an API Gateway and anti-corruption layers.]
[It ensures strict consistency, zero-downtime incremental migration, and rapid rollbacks while accommodating limited cloud experience.]