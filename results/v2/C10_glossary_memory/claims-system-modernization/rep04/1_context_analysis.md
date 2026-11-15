## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern Azure platform while the legacy system remains the system of record. It enables online claim submission and adjuster workflows while maintaining strict data consistency and a 3-year hybrid migration timeline.]

## Key Elements
- End Customers and Brokers
- Claims Adjusters and Claims Managers
- New Claims Platform (Azure App Service, Azure SQL)
- Legacy Mainframe (COBOL/DB2, On-Premise)
- Corporate Active Directory / Azure AD (Identity Provider)
- Analytics & Reporting System (Azure Synapse / Power BI)
- Azure API Management (APM) Gateway

## Relationships
- Customers & Brokers -> New Claims Platform via HTTPS for online claim submission
- Claims Adjusters -> New Claims Platform via HTTPS for web application access
- New Claims Platform <-> Legacy Mainframe via Azure ExpressRoute, mTLS, and Azure API Management
- New Claims Platform -> Analytics & Reporting System via Azure Event Hubs using TLS 1.3
- Users -> Corporate Active Directory / Azure AD via OAuth 2.0 / OIDC for Single Sign-On

## Technology Stack
- Azure App Service and Azure SQL for hosting the modern platform due to managed cloud capabilities
- Azure API Management (APM) for rate-limiting, token validation, and protecting fragile mainframe interfaces
- Azure ExpressRoute and mTLS for secure, encrypted hybrid connectivity between Azure and on-premise infrastructure
- Azure Application Insights for distributed tracing across hybrid latency boundaries
- OAuth 2.0 / OpenID Connect (OIDC) via Azure AD / Entra ID for secure single sign-on

## Rationale
[This hybrid architecture isolates the legacy mainframe from excessive direct queries using an Azure API Management gateway and asynchronous event streams, ensuring business continuity and compliance with strict batch window constraints. Furthermore, leveraging managed Azure services mitigates the team's low cloud experience while supporting rapid, incremental claim type migrations with automated rollback capabilities.]