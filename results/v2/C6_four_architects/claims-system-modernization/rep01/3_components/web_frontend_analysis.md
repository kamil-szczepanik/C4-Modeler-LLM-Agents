## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims platform with a modern hybrid cloud architecture. It ensures zero data loss, high performance, and rapid fallback capabilities during the three-year migration.

## Key Elements
- **Users**: Customers, Brokers, and Claims Adjusters
- **External Systems**: Legacy Mainframe, Azure AD / Entra ID Connect
- **Web Frontend**: React / TypeScript Single Page Application (SPA)
- **API Gateway / BFF**: Node.js / Express backend-for-frontend
- **Claims Core Service**: .NET 8 / C# core domain service
- **Integration & Sync Worker**: Python / C# Azure Functions
- **Data & Messaging**: Azure SQL Database, Azure Service Bus, Azure Cache for Redis, Azure App Configuration

## Relationships
- *Customer Portal / Web Frontend* -> *Azure AD / Entra ID*: Authenticates users [OpenID Connect (OIDC) over HTTPS]
- *Web Frontend* -> *API Gateway / BFF*: Sends API requests and WebSocket messages [HTTPS/REST, WSS (JSON)]
- *API Gateway / BFF* -> *Claims Core Service*: Forwards internal commands and queries [gRPC / HTTPS]
- *Integration & Sync Worker* -> *Legacy Mainframe*: Synchronizes claims data [Batch / Secure File Transfer]
- *Claims Core Service* -> *Azure Service Bus*: Publishes and consumes domain events [AMQP]

## Technology Stack
- **Frontend**: React and TypeScript to minimize custom framework lock-in given limited team cloud experience
- **Backend / Services**: Node.js / Express for the BFF layer; .NET 8 / C# for robust core domain processing
- **Cloud Provider**: Azure (westeurope region) combined with on-premise mainframe integration for a secure hybrid setup
- **Data & State**: Azure SQL Database Managed Instance for relational persistence; Azure Cache for Redis for distributed caching; Azure Service Bus for asynchronous messaging

## Rationale
This hybrid architecture isolates expensive mainframe dependencies while introducing a modern cloud platform via strangulation. It directly satisfies stringent performance (R-05) and fallback (R-06) constraints without requiring extensive prior cloud experience from the engineering team.