## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid cloud platform while ensuring uninterrupted legacy processing and zero claim loss. It enables online submissions and modern adjuster workflows via Azure-hosted containers integrated securely with Active Directory.

## Key Elements
- Customer Portal (React / TypeScript SPA)
- API Gateway / BFF (Node.js / Express)
- Claims Core Service (.NET 8 / C#)
- Integration & Sync Worker (Python / C# Azure Function)
- Claims Database (Azure SQL Database Managed Instance)
- Integration Event Broker (Azure Service Bus)
- Distributed Cache (Azure Cache for Redis)
- Configuration Store (Azure App Configuration)
- Legacy Mainframe (COBOL/DB2)
- Azure AD / Entra ID

## Relationships
- Customer & Broker -> Customer Portal: Submits and tracks claims [HTTPS]
- Customer Portal -> API Gateway / BFF: Sends API requests and WebSocket messages [HTTPS/REST, WSS]
- API Gateway / BFF -> Claims Core Service: Dispatches commands and queries [gRPC / HTTPS]
- Claims Core Service -> Claims Database: Persists and retrieves claim data [ADO.NET / Entity Framework Core]
- Claims Core Service -> Integration Event Broker: Publishes domain events [AMQP over TLS]
- Integration & Sync Worker -> Legacy Mainframe: Synchronizes data [Batch / Secure File Transfer / Proprietary Protocols]
- Customer Portal & API Gateway -> Azure AD / Entra ID: Authenticates and validates users [OIDC / OAuth2 / JWKS over HTTPS]

## Technology Stack
- Frontend: React with TypeScript, Vite, TanStack Query, and Zustand for lightweight state management and caching
- Backend Gateway: Node.js with Express, TypeScript, and `ws` for WebSocket handling
- Core Services: .NET 8 / C# for robust, high-performance domain logic
- Database & Cache: Azure SQL Database Managed Instance and Azure Cache for Redis for transactional consistency and fast retrieval
- Messaging: Azure Service Bus for reliable asynchronous event distribution
- Cloud & Identity: Hybrid deployment on Azure West Europe and on-premises mainframe, secured via Azure AD / Entra ID

## Rationale
This hybrid architecture isolates expensive mainframe changes while safely migrating claim types incrementally over three years. It combines modern cloud scalability and performance with strict consistency guarantees to prevent duplicate or lost claims.