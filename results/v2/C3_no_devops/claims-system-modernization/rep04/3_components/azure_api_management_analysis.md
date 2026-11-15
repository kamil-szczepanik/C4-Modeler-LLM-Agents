## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old mainframe with a modern Azure cloud platform while maintaining continuous claims processing. It utilizes a hybrid architecture to ensure seamless incremental migration, secure authentication, and rapid rollback capabilities.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Third-Party Partners & InsurTechs
- Azure API Management (Strangler Fig Router)
- Customer Portal (React SPA in Azure Static Web Apps)
- Adjuster Web Application (React SPA + ASP.NET Core BFF)
- Claims Processing Engine (ASP.NET Core Microservices on AKS)
- Anti-Corruption Layer (Azure Functions & Azure Service Bus)
- Legacy Mainframe (COBOL/DB2 on-premise)
- Azure App Configuration & Azure Cache for Redis
- Azure Active Directory & Key Vault

## Relationships
- Customers, Brokers, Adjusters, Partners -> Azure API Management: Accesses services and APIs [HTTPS/REST with TLS 1.3, OAuth 2.0 / OpenID Connect]
- Azure API Management -> Customer Portal & Adjuster Web Application: Routes traffic [HTTPS]
- Strangler Fig Router Policy -> Routing Configuration Store: Queries live routing rules [HTTPS/REST]
- Strangler Fig Router Policy -> Claims Processing Engine: Routes migrated claims [gRPC / HTTPS]
- Strangler Fig Router Policy -> Legacy Mainframe: Proxies unmigrated claims [site-to-site VPN/ExpressRoute with mTLS]
- Claims Processing Engine -> Anti-Corruption Layer: Translates domain events [Azure Service Bus]

## Technology Stack
- Azure API Management: Acts as Strangler Fig router and gateway, chosen for policy enforcement and routing capabilities.
- ASP.NET Core & Azure Kubernetes Service: Powers microservices for high scalability and modern developer velocity.
- React SPA & Azure Static Web Apps: Delivers performant, responsive UIs for customers and adjusters.
- Azure App Configuration: Enables zero-downtime, dynamic feature-flag routing for instant claim-type rollbacks.
- Azure Active Directory & Key Vault: Handles SSO integration, OAuth 2.0 validation, and secure mTLS certificate management.

## Rationale
This hybrid architecture isolates the expensive-to-change mainframe behind an anti-corruption layer while decoupling migration via API management. It guarantees business continuity, sub-second modern UI performance, strict security compliance, and one-day rollbacks.