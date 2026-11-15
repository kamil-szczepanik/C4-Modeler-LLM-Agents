## Overview
[Hybrid Insurance Claims Modernization Platform gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure cloud architecture. It enables online claim submissions and adjuster processing while maintaining legacy data consistency.]

## Key Elements
- End Customers & Brokers
- Claims Adjusters
- Web Application (React SPA with Node.js BFF on Azure App Service)
- API Gateway (.NET / YARP on Azure Container Apps)
- Claims Core Domain Service (.NET Core)
- Read-Model & Caching Store (Azure Cosmos DB / Redis)
- Corporate Active Directory

## Relationships
- End Customers & Brokers -> Web Application: Submits claims via public internet [HTTPS/JSON]
- Claims Adjusters -> Web Application: Manages claims via UI [HTTPS/JSON]
- Web Application -> Corporate Active Directory: Authenticates users [OpenID Connect / OAuth 2.0]
- Web Application -> API Gateway: Proxies domain requests with token propagation [HTTPS/JSON]

## Technology Stack
- React & TypeScript: Client-side UI for high performance and responsiveness
- Node.js BFF (Backend-for-Frontend): Manages secure session tokens and server-side validation
- Azure App Service: Hosts the Web Application securely
- Azure Cosmos DB / Redis: Manages read-models and encrypted draft claim persistence
- .NET Core & YARP: Powers backend domain services and the API Gateway

## Rationale
[This hybrid architecture isolates expensive mainframe dependencies while delivering a sub-2-second adjuster experience via modern cloud caching. The BFF pattern and rigorous token management ensure strict security compliance without compromising the 3-year migration timeline.]