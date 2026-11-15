## Overview
[System: Insurance Claims Modernization Platform]
[Core Purpose: Gradually replaces the 30-year-old mainframe claims system with a modern hybrid cloud platform while ensuring zero data loss and uninterrupted batch windows.]

## Key Elements
• **Frontend SPA**: React / TypeScript hosted on Azure Static Web Apps
• **API Gateway**: .NET Core / Envoy implementing CQRS pattern
• **Backend Service**: Modular Monolith in .NET Core hosted on Azure App Service
• **Mainframe Integration Adapter**: Azure Functions with Polly
• **Secrets Management**: Azure Key Vault
• **Configuration Refresh Service**: Azure App Configuration SDK
• **Secret Rotator Function**: Azure Functions (.NET / C#)
• **Database**: Azure SQL Database
• **Monitoring Service**: Azure Application Insights and Azure Monitor Diagnostic Settings
• **Security & Networking**: Azure RBAC, Managed Identities, Azure Private Endpoint / Private Link

## Relationships
• **Frontend SPA -> API Gateway**: Submits claims and handles adjuster workflows [HTTPS/REST]
• **API Gateway -> Backend Service**: Routes domain commands and queries [gRPC / HTTPS]
• **Backend Service / Integration Adapter -> Secrets Management**: Retrieves active secret versions via Private Endpoint [Azure SDK / Managed Identity]
• **Backend Service / Integration Adapter -> Configuration Refresh Service**: Polls or receives webhooks for secret version changes [HTTPS/TLS]
• **Secret Rotator Function -> Azure SQL Database / External APIs**: Updates credentials [HTTPS/TLS]
• **Secrets Management -> SIEM / Governance Reporting**: Streams diagnostic access and administrative logs [Azure Monitor Diagnostic Settings with WORM storage]

## Technology Stack
• **Azure Static Web Apps & React/TypeScript**: Provides responsive UI for claims adjusters under 2s response time.
• **.NET Core & Azure App Service**: Powers backend domain logic with modular monolith architecture.
• **Azure Key Vault & Azure App Configuration**: Centralizes secure credential management and webhook-driven cache invalidation to prevent stale connection pooling.
• **Azure Functions**: Executes automated, zero-downtime credential rotation and event-driven integration tasks.
• **Azure Private Link**: Secures internal network traffic to Key Vault without public IP exposure.

## Rationale
[The hybrid architecture leverages Azure managed services to bridge the legacy COBOL/DB2 mainframe with a modern cloud platform, minimizing operational overhead for a cloud-inexperienced team.]
[Robust secrets management, automated rotation, and strict private networking ensure strict compliance and zero-downtime claim processing.]