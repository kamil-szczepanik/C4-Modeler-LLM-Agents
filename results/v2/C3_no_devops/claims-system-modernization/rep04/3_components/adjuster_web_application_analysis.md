## Overview
The Adjuster Web Application modernizes the regional insurer's claims handling workflow while operating within a hybrid cloud architecture. It provides adjusters with a secure, responsive interface that bridges modern microservices and the 30-year-old COBOL/DB2 mainframe.

## Key Elements
- React SPA (SPA UI Components, Auth Guard Component)
- ASP.NET Core BFF (Claim Management Controller, Read Model Projections Cache Service, Mainframe Anti-Corruption Client, Audit Trail Service)
- Azure Cache for Redis
- Azure Active Directory & Key Vault
- Anti-Corruption Layer (Azure Functions & Azure Service Bus)

## Relationships
- React SPA -> Claim Management Controller [HTTPS / JSON]
- Claim Management Controller -> Read Model Projections Cache Service [.NET In-Memory / TCP over TLS]
- Claim Management Controller -> Audit Trail Service [.NET In-Memory]
- Audit Trail Service -> Anti-Corruption Layer [gRPC / HTTPS]
- Adjuster Web Application -> Azure Cache for Redis [TCP/Redis Protocol with TLS]
- Adjuster Web Application -> Azure Active Directory & Key Vault [OAuth 2.0 / OpenID Connect / Managed Identities]

## Technology Stack
- React SPA: Chosen for responsive UI and local session storage draft auto-saving.
- ASP.NET Core BFF: Implements server-side token management, FluentValidation, and API orchestration.
- Azure Cache for Redis: Caches claims data to guarantee sub-2-second screen loads (R-05).
- Azure Active Directory: Enforces Single Sign-On (R-07) and Role-Based Access Control.
- Azure Managed Identities: Eliminates hardcoded secrets for Key Vault and Redis connections.

## Rationale
This architecture isolates legacy mainframe latency using cached read models to meet strict performance SLAs. It securely maintains data consistency and user authorization while supporting a gradual 3-year migration path.