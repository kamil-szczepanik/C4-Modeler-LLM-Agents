## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a modern hybrid cloud platform. It enables online claim submission and adjuster workflows while maintaining synchronization with the legacy system of record.

## Key Elements
- **Customers and Brokers:** External users submitting claims online.
- **Claims Adjusters:** Internal users handling claims via the web application.
- **Active Directory:** On-premises identity provider for Single Sign-On.
- **Legacy Mainframe:** On-premises COBOL/DB2 system of record.
- **API Gateway:** Azure Front Door / App Gateway managing HTTPS routing.
- **Customer Portal:** React SPA hosted on Azure Static Web Apps.
- **Adjuster Workspace:** Node.js Backend-for-Frontend on Azure App Service.
- **Claims Core Engine:** Java Spring Boot service on Azure Container Apps.
- **Integration Layer:** Azure Event Hubs with Apache Camel.
- **Migrated Claims Database:** Azure Database for PostgreSQL.

## Relationships
- Customers/Brokers to Customer Portal via HTTPS.
- Customer Portal and Adjuster Workspace to API Gateway via HTTPS using OpenID Connect.
- API Gateway to Adjuster Workspace via HTTPS.
- Adjuster Workspace to Claims Core Engine via gRPC.
- Claims Core Engine to Migrated Claims Database via JDBC over TLS.
- Claims Core Engine and Legacy Mainframe to Integration Layer via Apache Camel and Azure Event Hubs.

## Technology Stack
- **Frontend:** React on Azure Static Web Apps for modern UI delivery.
- **Backend Services:** Node.js (BFF) and Java Spring Boot on Azure App Service and Azure Container Apps for robust domain logic.
- **Messaging/Integration:** Azure Event Hubs with Apache Camel for low operational overhead and protocol translation.
- **Database:** Azure Database for PostgreSQL for transactional consistency.
- **Security:** Azure Active Directory via OpenID Connect for SSO.

## Rationale
This hybrid architecture isolates expensive mainframe dependencies through an integration layer while leveraging managed Azure services to accommodate the team's low cloud experience. It ensures high performance, strict data consistency, and rapid fallback capabilities.