## Overview
[System: Insurance Claims Modernization Platform]
[Core Purpose: Gradually replaces a 30-year-old mainframe claims system using a hybrid cloud architecture.]

## Key Elements
- Customers / Brokers
- Claims Adjusters
- Legacy Mainframe (COBOL/DB2)
- Active Directory / Microsoft Entra ID
- Payment Gateway
- Azure API Management
- Customer Portal (React / Azure Static Web Apps)
- Adjuster Workspace (Angular / Azure App Service)
- Claims Core Engine (Java / Spring Boot / Azure Container Apps)
- Routing & Integration Service (Azure Container Apps):
  - Router Dispatcher (.NET isolated worker)
  - Configuration Cache (Azure App Configuration)
  - Legacy Adapter (HTTP Client)
  - Audit Logger Component (.NET Background Service)
- Business Analytics & Reporting (Azure SQL / Power BI)
- Azure SQL Database
- Azure Service Bus Topics

## Relationships
- Customers / Brokers -> Azure API Management: Online claim submissions [HTTPS / TLS 1.3]
- Claims Adjuster -> Azure API Management: Manage claims via web app [HTTPS / TLS 1.3 / SSO via Microsoft Entra ID]
- Azure API Management -> Claims Core Engine / Routing & Integration Service: Routes traffic [Internal API / HTTPS]
- Router Dispatcher -> Configuration Cache: Queries routing rules [Azure App Configuration SDK]
- Router Dispatcher -> Azure Service Bus Topics: Publishes claim events [AMQP / TLS 1.3]
- Azure Service Bus Topics -> Legacy Adapter & Claims Core Engine: Consumes events with retry/dead-letter [AMQP / TLS 1.3]
- Legacy Adapter -> Legacy Mainframe: Forwards unmigrated claims [Mutual TLS (mTLS) / Secure Hybrid Tunnel / VPN]
- Legacy Adapter -> Azure Key Vault: Retrieves rotating credentials and certificates [Managed Identity / REST]

## Technology Stack
- Azure Container Apps: Hosts microservices to eliminate cold starts and simplify hybrid networking for a team with low cloud experience.
- Azure App Configuration: Stores claim-type routing toggles for instant runtime switching and one-day mainframe fallback.
- Azure Service Bus Topics: Decouples routing from downstream processing and provides retry/dead-letter capabilities to prevent data loss.
- Azure Key Vault: Secures certificates and rotating credentials for mainframe integration.
- .NET / Java Spring Boot: Core runtime environments for cloud components and services.

## Rationale
The hybrid architecture respects legacy constraints by keeping the mainframe as the system of record while incrementally migrating claim types. Decoupled integration patterns and runtime configuration caches guarantee zero data loss and enable rapid fallback capabilities without complex deployments.