## Overview
[The system is a modular monolith backend service built on .NET 8, designed to gradually modernize a 30-year-old mainframe insurance claims platform in a hybrid Azure and on-premises environment.]

## Key Elements
* Claim Management Module (.NET Class Library)
* Anti-Corruption Layer (ACL) Component
* Feature Flag & Routing Engine
* Caching / Read-Model Store
* Audit & Outbox Component

## Relationships
* API Gateway -> Backend Service: Routes authenticated requests [HTTPS / Internal VNet]
* Backend Service -> Azure SQL Database: Persists domain states and read models [T-SQL / Internal VNet]
* Backend Service -> Mainframe Integration Adapter: Triggers asynchronous synchronization [Internal VNet routing]
* Backend Service -> Azure Key Vault: Retrieves secrets and encryption keys [Azure SDK / Managed Identity]
* Backend Service -> Azure Application Insights: Sends distributed traces and business telemetry [Application Insights SDK]

## Technology Stack
* Backend Platform: .NET 8 Modular Monolith for strict internal boundaries without microservice overhead
* Runtime Hosting: Azure App Service PaaS with Blue/Green deployment slots for zero-downtime releases
* Data Persistence: Azure SQL Database using Entity Framework Core for transactional outbox pattern and eventual consistency
* Security & Auth: Azure Managed Identities, mTLS within the VNet, and Transparent Data Encryption (TDE)
* Infrastructure as Code: Bicep or Terraform to prevent configuration drift given team's low cloud experience

## Rationale
[This architecture enforces strict module boundaries and transactional outbox patterns to guarantee zero data loss and enable rapid one-day rollbacks for migrated claim types. It isolates legacy mainframe latency through caching and asynchronous processing, meeting strict performance and maintainability requirements.]