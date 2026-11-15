## Overview
[The system is a hybrid insurance claims modernization platform that gradually replaces a 30-year-old mainframe with a modern cloud solution. Its core purpose is to enable seamless online claim submission, adjuster workflows, and incremental claim type migration while ensuring continuous business operations.]

## Key Elements
- [Claims Adjuster Web App Container (Next.js / React)]
- [Customer Portal Container (Next.js / React)]
- [API Gateway (Azure Front Door / APIM)]
- [Claims Orchestrator Container (Node.js / .NET Core)]
- [Legacy Mainframe Adapter Container (Azure Container Apps)]
- [Claims State & Idempotency Database (Azure Cosmos DB)]
- [Legacy Mainframe (COBOL/DB2 with CICS/MQ)]
- [Microsoft Entra ID]

## Relationships
- [End Customers & Brokers -> API Gateway: Online claim submission via HTTPS/REST]
- [Claims Adjusters -> API Gateway: Claim processing via HTTPS]
- [Claims Orchestrator Container -> Legacy Mainframe Adapter Container: Asynchronous messaging and synchronous requests via Azure Service Bus and gRPC]
- [Legacy Mainframe Adapter Container -> Legacy Mainframe: Legacy transactions via CICS/MQ over mTLS on Site-to-Site VPN / Azure ExpressRoute]
- [Legacy Mainframe Adapter Container -> Azure Cosmos DB: State persistence and idempotency tracking via TCP/TLS]

## Technology Stack
- [Azure Container Apps: Hosting the adapter container due to managed scalability]
- [Azure Cosmos DB: Unified storage for claims state and idempotency keys to simplify the operational footprint]
- [Azure App Configuration: Dynamic feature toggling for the one-day claim type rollback switch]
- [Azure Key Vault: Secure injection of RACF/SAF mainframe credentials and mTLS certificates]
- [OpenTelemetry: Distributed hybrid tracing and business metrics collection]

## Rationale
[This hybrid architecture abstracts legacy complexity behind a dedicated adapter container while using robust cloud-native services to guarantee data consistency and fast UI performance. It enables safe, incremental migration of claim types with rapid rollback capabilities, perfectly fitting the team's cloud experience level.]