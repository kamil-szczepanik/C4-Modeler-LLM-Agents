## Overview
The system is a hybrid modernization platform for a regional insurer that gradually replaces a 30-year-old mainframe claims system. Its core purpose is to provide modern online claim submission and adjuster portals while keeping the legacy mainframe as the system of record.

## Key Elements
- **Users**: Customer & Broker, Claims Adjusters
- **Edge Routing**: Azure API Management (APIM)
- **Frontends**: Customer Portal (React / TypeScript SPA), Web Frontend (React / TypeScript SPA)
- **BFF / Gateway Components**: Customer BFF (Node.js / Express), Adjuster BFF (Node.js / Express with WebSocket Gateway Module)
- **Backend Services**: Claims Core Service (.NET 8 / C#), Integration & Sync Worker (Python / C# Azure Function)
- **Data & Caching**: Azure SQL Database Managed Instance, Azure Cache for Redis
- **Messaging**: Azure Service Bus (Integration Event Broker)
- **External Systems**: Legacy COBOL/DB2 Mainframe, Azure Active Directory / Entra ID

## Relationships
- Customer Portal & Web Frontend -> Azure API Management [HTTPS, WSS]
- Azure API Management -> Customer BFF & Adjuster BFF [HTTP/2, internal vNet]
- Adjuster BFF -> Azure Cache for Redis [TCP/RESP]
- Azure Service Bus -> Adjuster BFF (WebSocket Gateway) [AMQP / Azure SDK]
- Customer BFF & Adjuster BFF -> Claims Core Service [gRPC]
- Azure API Management -> Azure Active Directory [OpenID Connect (OIDC) over HTTPS]

## Technology Stack
- **Edge Security**: Azure APIM for managed rate-limiting, SSL termination, and OIDC token validation to reduce operational overhead.
- **Frontend Runtimes**: Node.js with Express for lightweight, decoupled BFFs tailored to customer and adjuster workflows.
- **Caching & Real-Time**: Azure Cache for Redis to mitigate 5-second mainframe latencies, and Socket.io/ws for real-time WebSocket push updates.
- **Backend & Integration**: .NET 8 for core claims services, Python/C# Azure Functions for sync workers, and Azure Service Bus for event-driven messaging.

## Rationale
This hybrid architecture isolates the expensive-to-change mainframe while modernizing the user experience via Azure-hosted cloud services. It successfully meets strict performance and consistency constraints despite the team's low initial cloud experience.