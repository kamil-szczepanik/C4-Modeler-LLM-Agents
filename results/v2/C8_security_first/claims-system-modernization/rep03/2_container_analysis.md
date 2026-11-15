## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud platform. It enables online claim submission and adjuster workflows while maintaining business continuity through a 3-year migration.

## Key Elements
* **Users:** Customers, Brokers, and Claims Adjusters
* **Frontends:** Customer Portal & Adjuster Web Apps built as Single Page Apps on Azure Static Web Apps
* **Backend Services:** Claim Management API, Claim Router / Anti-Corruption Layer (ACL), and Audit & Reconciliation Service running on Azure Container Apps (.NET 8)
* **Messaging & Configuration:** Azure Service Bus and Azure App Configuration
* **Data Stores:** Azure SQL Database (modern platform) and COBOL/DB2 Mainframe (system of record)
* **Security & Integration:** Azure Active Directory (Entra ID), Azure Key Vault, Azure API Gateway, and ExpressRoute / IPsec VPN with mTLS

## Relationships
* **Users to Frontends:** HTTPS/OIDC with Multi-Factor Authentication (MFA)
* **Frontends to Backend:** HTTPS REST APIs routed through Azure API Gateway
* **Claim Management API to Service Bus:** AMQP over TLS for asynchronous messaging
* **Claim Router to Mainframe:** mTLS over dedicated ExpressRoute / IPsec VPN tunnel enforcing rate limiting and circuit breakers
* **Audit Service to Azure SQL:** Entity Framework Core over secure internal connections

## Technology Stack
* **Cloud Provider:** Hybrid (Azure West Europe and on-premise mainframe) for gradual migration and data residency compliance
* **Compute:** Azure Container Apps (.NET 8) for containerized microservices reducing operational complexity for teams with low cloud experience
* **Messaging:** Azure Service Bus for decoupled, reliable eventing during mainframe batch windows
* **Security:** Azure Active Directory (Entra ID) for SSO/OIDC and Azure Key Vault for secret management via managed identities
* **Observability:** OpenTelemetry and Azure Application Insights for distributed tracing across hybrid boundaries

## Rationale
The hybrid architecture and Strangler Fig pattern using an Anti-Corruption Layer isolate modern UI components from mainframe latency and nightly batch constraints. Azure managed services mitigate the team's low cloud experience while guaranteeing zero data loss, strict security compliance, and rapid 1-day roll-back capabilities.