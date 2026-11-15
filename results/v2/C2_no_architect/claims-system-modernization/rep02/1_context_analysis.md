## Overview
The system is a hybrid insurance claims modernization platform that gradually migrates claim types from a 30-year-old mainframe to Azure. It maintains business continuity and data consistency while delivering a responsive web interface for claims adjusters and online submission for customers.

## Key Elements
- Policyholders and Brokers (External users for online claim submission)
- Claims Adjusters (Internal users of the new web application)
- Compliance and Audit Officers (Internal users monitoring immutable audit trails)
- Azure App Service (Hosting the new adjuster web application and claim APIs)
- Azure Service Bus & Azure Cosmos DB (Event-driven integration layer and append-only event store)
- COBOL/DB2 Mainframe (On-premises legacy system of record)
- Azure Active Directory / Entra ID (Identity and Access Management)

## Relationships
- Policyholders and Brokers submit claims to Azure App Service via HTTPS (TLS 1.3, OpenID Connect/OAuth2).
- Claims Adjusters interact with Azure App Service via HTTPS for sub-second UI responses.
- Azure App Service communicates asynchronously with the COBOL/DB2 Mainframe via Azure Service Bus over Azure ExpressRoute or IPsec VPN (mTLS).
- Azure App Service logs state changes to Azure Cosmos DB using Managed Identities.
- Azure Active Directory federates with on-premise Active Directory for Single Sign-On.

## Technology Stack
- Azure App Service: Chosen as a fully managed PaaS to mitigate the team's low cloud experience and avoid AKS operational overhead.
- Azure Service Bus: Provides an asynchronous, event-driven integration layer to prevent mainframe batch window contention (23:00-05:00).
- Azure Cosmos DB: Serves as an append-only event store to guarantee immutable audit trails and data consistency (R-04).
- Azure Active Directory / Entra ID: Implements SSO and OAuth2/OpenID Connect for secure user authentication.
- Azure ExpressRoute / IPsec VPN with mTLS: Secures the hybrid network boundary between Azure and the on-premise mainframe.

## Rationale
This hybrid architecture isolates the expensive-to-change COBOL/DB2 mainframe while modernizing the user experience via Azure PaaS services. Asynchronous event-driven patterns and strict data consistency controls ensure seamless, risk-managed incremental migration of claim types over three years.