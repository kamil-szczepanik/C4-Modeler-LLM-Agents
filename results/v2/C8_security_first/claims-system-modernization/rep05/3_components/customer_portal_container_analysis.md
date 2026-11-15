## Overview
[The system is a modern hybrid cloud platform that gradually replaces a 30-year-old insurance mainframe while maintaining legacy processing. Its core purpose is to enable online claims submission and adjuster management while ensuring zero data loss and minimal legacy system disruption.]

## Key Elements
- End Customers & Brokers
- Claims Adjusters
- Customer Portal Container (Next.js / React)
- Adjuster Web App Container (Next.js / React)
- API Gateway (Azure Front Door / Azure API Management)
- Claims Orchestrator Container (Node.js / .NET Core)
- Legacy Mainframe Adapter Container (Azure Container Apps)
- Claims State Database (Azure SQL / Azure Cosmos DB)
- Microsoft Entra ID
- Azure Blob Storage
- Azure Container Apps

## Relationships
- End Customers & Brokers -> Customer Portal Container: Submit and manage online claims [HTTPS/REST over TLS 1.3]
- Customer Portal Container -> API Gateway: API requests with OIDC token validation [HTTPS/REST]
- Customer Portal Container -> Microsoft Entra ID: Validates OIDC tokens [OpenID Connect]
- Customer Portal Container -> Azure Blob Storage: Streams claim attachments via SAS tokens [HTTPS]
- API Gateway -> Claims Orchestrator Container: Routes API traffic [HTTPS/REST]
- Claims Orchestrator Container -> Legacy Mainframe Adapter Container: Forwards claim data [gRPC / HTTPS]
- Legacy Mainframe Adapter Container -> COBOL/DB2 Mainframe: Synchronizes legacy state [SNA / MQ / DB2 Connect]
- Claims Orchestrator Container -> Claims State Database: Persists modern claim state [SQL / Cosmos DB SDK]

## Technology Stack
- Next.js / React: Powers frontend SSR applications and BFF layer for optimized load performance and maintainability.
- Azure Container Apps: Hosts containerized microservices, abstracting Kubernetes complexity for a low-experience cloud team.
- Azure Front Door / APIM: Acts as an API gateway for edge caching, security termination, and routing.
- Microsoft Entra ID: Provides enterprise Single Sign-On via OpenID Connect (OIDC).
- Azure Blob Storage: Handles large file uploads using secure SAS tokens to prevent BFF memory exhaustion.
- Azure SQL / Cosmos DB: Manages modern claim persistence ensuring consistency.

## Rationale
[This hybrid architecture isolates the fragile COBOL mainframe behind an adapter while modernizing the frontend using Azure Container Apps to match team capabilities. It guarantees system continuity, low latency for adjusters, and strict security compliance without extending nightly batch windows.]