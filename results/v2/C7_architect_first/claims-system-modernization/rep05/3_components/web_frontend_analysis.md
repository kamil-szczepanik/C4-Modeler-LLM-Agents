## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern hybrid cloud platform. The architecture ensures business continuity, zero claim loss, and sub-2-second UI response times during the 3-year migration.

## Key Elements
- **Users**: Customers, Brokers, Claims Adjusters
- **External Systems**: Legacy Mainframe System, Insurer's Active Directory, Payment Gateway & Notification System
- **Web Frontend**: React Single Page Application hosted on Azure App Service with Azure Front Door/CDN
- **Frontend Components**: Claim Submission UI, Adjuster Dashboard, Auth Client Module, Accessibility & Localization Module, User Analytics & Telemetry Tracking
- **BFF / API Gateway**: Node.js / Java Spring Boot deployed via Azure API Management
- **Backend Services**: Claims Processing Service (Java Spring Boot, JPA, Azure Container Apps)
- **Integration & Data**: Azure Service Bus, Azure SQL Database, Azure Redis Cache

## Relationships
- Customers, Brokers, Claims Adjusters -> Web Frontend: Accesses online claims and adjuster workflows via HTTPS / REST
- Web Frontend -> Insurer's Active Directory: Authenticates users and validates sessions via OAuth2 / OIDC with PKCE
- Web Frontend -> BFF / API Gateway: Proxies requests, routes traffic, and handles session cookies via HTTPS / REST
- BFF / API Gateway -> Claims Processing Service: Dispatches core business logic via internal HTTPS / REST
- Claims Processing Service -> Legacy Mainframe System: Syncs and routes unmigrated claim types via Custom Routing & Circuit-Breaker Worker / Integration Hub

## Technology Stack
- **Frontend**: React, TypeScript, Azure App Service (PaaS for reduced operational overhead), Azure Front Door/CDN (global load balancing and caching)
- **Backend & Integration**: Node.js, Java Spring Boot, Azure API Management, Azure Container Apps, Azure Service Bus
- **Data & Caching**: Azure SQL Database (secure server-side state and PII storage), Azure Redis Cache
- **Security & Observability**: Azure Application Insights (RUM, synthetic monitoring, distributed tracing), TLS 1.3, HTTP-only Secure SameSite=Strict cookies

## Rationale
- The hybrid cloud architecture successfully isolates expensive mainframe operations while migrating claim types individually over three years.
- Managed PaaS components (Azure App Service, Azure Container Apps) offset the team's low cloud experience while strict BFF-mediated security guarantees PII protection and zero-trust validation.