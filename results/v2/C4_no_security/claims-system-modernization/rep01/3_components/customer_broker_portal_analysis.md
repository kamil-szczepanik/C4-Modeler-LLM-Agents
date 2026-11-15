## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern hybrid cloud platform on Azure West Europe. It ensures seamless online claim submission and adjuster workflows while maintaining zero downtime and strict hybrid data consistency.

## Key Elements
* Policyholders and Brokers (Users)
* Claims Adjusters (Users)
* Customer/Broker Portal (Node.js, TypeScript, Next.js, Azure App Service)
* Adjuster Workstation and BFF (.NET, Azure App Service)
* Core Claims Domain & Claim Migration Manager (.NET)
* Anti-Corruption Layer (ACL) Gateway & Integration Worker (.NET, Azure Service Bus)
* Operational Data Store (Azure Database for PostgreSQL)
* Legacy Mainframe (COBOL/DB2, On-Premises)
* Microsoft Entra ID (Identity Provider)

## Relationships
* Policyholders/Brokers -> Customer/Broker Portal: Online claim submission and status tracking [HTTPS, OpenID Connect]
* Customer/Broker Portal -> Azure API Management: Routes ingress API traffic [HTTPS]
* Azure APIM -> Core Claims Domain: Internal service communication [gRPC over TLS]
* Core Claims Domain -> Anti-Corruption Layer Gateway: Hybrid database and legacy bridging [gRPC, TCP]
* ACL Gateway -> Legacy Mainframe: Batch and synchronous claim processing [SNA, DB2 protocols]
* Customer/Broker Portal -> Azure Cache for Redis: Distributed session and broker view caching [TCP]
* All Services -> Microsoft Entra ID: Single Sign-On authentication [OAuth2, OIDC]

## Technology Stack
* Frontend/BPortal: Node.js, TypeScript, Next.js, React Server Components (chosen for rapid UI delivery)
* Backend Services: .NET / C# (chosen for robust enterprise domain modeling)
* Compute: Azure App Service for Linux with Docker containers (standardizes deployments for low cloud-experience team)
* Integration & Caching: Azure Service Bus, Azure Cache for Redis (handles asynchronous decoupling and distributed scalability)
* Database: Azure Database for PostgreSQL (modern relational operational data store)
* Security & Observability: Microsoft Entra ID, MSAL, Azure Application Insights (ensures secure SSO and distributed tracing)

## Rationale
This hybrid architecture isolates the expensive-to-change legacy mainframe behind an Anti-Corruption Layer and Azure Service Bus, allowing risk-free, incremental claim-type migrations. Cloud-native caching and containerized Azure App Services ensure high performance and maintainability despite the team's limited cloud experience.