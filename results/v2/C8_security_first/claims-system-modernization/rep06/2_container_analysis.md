## Overview
[The system modernizes a regional insurer's 30-year-old mainframe by gradually migrating claims processing to a hybrid Azure cloud platform. It ensures business continuity by maintaining the legacy system of record while introducing modern web applications and event-driven microservices.]

## Key Elements
* Policyholders and Brokers (Users)
* Claims Adjusters (Users)
* API Gateway (Azure Front Door / Azure API Management)
* Claims Web Application (React / Azure App Service)
* Audit & Reporting Dashboard (React / Azure App Service)
* Claims Core Service (Node.js/TypeScript on Azure Container Apps)
* Integration/Sync Service & Read-Model Sync Worker (Azure Service Bus, Azure Functions / .NET)
* Legacy Mainframe System (COBOL / DB2)
* Identity Provider (Azure AD / Entra ID)

## Relationships
* Policyholders/Brokers to API Gateway via HTTPS/REST (Online claim submission)
* Claims Adjusters to Claims Web Application via HTTPS/REST (Claim handling)
* API Gateway to Claims Core Service via gRPC / HTTPS (Dynamic routing)
* Claims Core Service to Legacy Mainframe via MQ/AMQP and mTLS over IPsec VPN / Azure ExpressRoute (Hybrid data sync)
* Claims Core Service to Azure Service Bus via AMQP (Event streaming)
* Web Applications to Azure AD / Entra ID via OpenID Connect / OAuth 2.0 (SSO)

## Technology Stack
* Cloud Provider: Hybrid (On-premise mainframe and Azure West Europe)
* Frontend: React hosted on Azure App Service for fast adjuster UI rendering (<2s)
* Backend: Node.js/TypeScript on Azure Container Apps using CQRS and Event Sourcing
* Messaging: Azure Service Bus for standardized, managed event streaming and queuing
* Database & Caching: Azure SQL / Cosmos DB for local read models bypassing mainframe latency
* Security & Auth: Azure AD / Entra ID (OIDC), Azure Key Vault (CMK), and WAF

## Rationale
[This hybrid architecture decouples the responsive modern cloud UI from slow legacy mainframe responses using CQRS and local read models, meeting strict performance and consistency goals. Utilizing fully managed Azure services mitigates the team's low cloud experience while enabling claim-by-claim migration with rapid 1-day fallback capabilities.]