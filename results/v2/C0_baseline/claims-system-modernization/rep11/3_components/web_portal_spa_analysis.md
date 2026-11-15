## Overview
- Modernizes a 30-year-old regional insurer's claims system by gradually migrating claim types to a new platform while keeping the mainframe as the system of record.
- Delivers a secure hybrid cloud architecture utilizing Azure and on-premises infrastructure to ensure business continuity and seamless customer experiences.

## Key Elements
- Customers and Brokers (External Actors)
- Web Portal (SPA) (React hosted on Azure Static Web Apps)
- Claims API (BFF) (Node.js / TypeScript in Azure Kubernetes Service)
- Mainframe Adapter (Node.js / TypeScript in Azure Kubernetes Service)
- Legacy Mainframe System (COBOL/DB2, On-Premises)
- Azure Cosmos DB & Azure Service Bus
- Active Directory / Azure AD (Identity Provider)

## Relationships
- Customers & Brokers -> Web Portal (SPA): HTTPS (TLS 1.3)
- Web Portal (SPA) -> Claims API (BFF): REST over HTTPS with OAuth 2.0 / OIDC
- Claims API (BFF) -> Mainframe Adapter: Internal gRPC / REST
- Mainframe Adapter -> Legacy Mainframe System: 3270 / SNA / DB2 direct batch protocols

## Technology Stack
- Frontend: React / TypeScript for dynamic form rendering and user interfaces
- Hosting & CDN: Azure Static Web Apps for global delivery and simplified deployment
- Backend Compute: Azure Kubernetes Service (AKS) running Node.js / TypeScript services
- Integration & Messaging: Azure Service Bus for asynchronous decoupling
- Database: Azure Cosmos DB for operational flexibility during migration
- Security: Azure AD with OIDC and HttpOnly/Secure/SameSite=Strict cookies

## Rationale
- The hybrid approach balances strict cost and operational constraints by keeping the expensive mainframe as the system of record while incrementally modernizing user touchpoints.
- Managed Azure services like Static Web Apps and AKS accommodate the team's limited cloud experience while meeting strict security and performance requirements.