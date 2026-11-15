## Overview
[The system is a hybrid insurance claims modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with modern cloud services while maintaining legacy data sync. Its core purpose is to decouple online claim submissions and adjuster web applications from the mainframe using Azure services and asynchronous integration patterns.]

## Key Elements
- New Claims Platform
- Customers & Brokers
- Claims Adjusters
- Finance & Compliance Auditors
- Customer Portal App (React/TypeScript, Azure Static Web Apps)
- Adjuster Web App (React/Node.js BFF)
- Claims Core API (.NET Core modular monolith, Azure Container Apps)
- Integration Worker (.NET background service, Azure Container Apps)
- Audit & Compliance Service (Azure Function)
- Claim Read Database (Azure SQL Database)
- Azure Service Bus
- Enterprise Service Bus / Integration Gateway
- Legacy Mainframe COBOL/DB2 System of Record
- Insurer Active Directory

## Relationships
- Customers & Brokers -> Customer Portal App (HTTPS / JSON)
- Claims Adjusters -> Adjuster Web App (HTTPS / HTML)
- Customer Portal App -> Claims Core API (HTTPS / JSON)
- Adjuster Web App -> Claims Core API (HTTPS / JSON)
- Claims Core API -> Claim Read Database (TDS / TCP)
- Claims Core API -> Azure Service Bus (AMQP)
- Integration Worker -> Azure Service Bus (AMQP)
- Azure Service Bus -> Enterprise Service Bus / Integration Gateway (IPsec VPN / Azure ExpressRoute, TLS 1.3)
- Enterprise Service Bus / Integration Gateway -> Legacy Mainframe COBOL/DB2 System of Record (Managed File Transfer / MQ / APIs)
- Customer Portal App -> Insurer Active Directory (OIDC / OAuth2 via Azure Entra ID Connect)
- Adjuster Web App -> Insurer Active Directory (OIDC / OAuth2 via Azure Entra ID Connect)

## Technology Stack
- Azure Static Web Apps: Hosts React/TypeScript frontend with minimal cloud complexity
- Azure Container Apps: Runs containerized modular monoliths and background workers with KEDA scaling
- Azure SQL Database: Provides relational storage for claim read models and idempotency tracking
- Azure Service Bus: Asynchronous event queue using AMQP to buffer messages and protect legacy batch windows
- OpenTelemetry: Distributed tracing across cloud and on-premise hybrid boundaries
- Azure Entra ID: Manages SSO, MFA, and managed identities for secure service-to-service authentication

## Rationale
[This hybrid architecture isolates expensive mainframe dependencies behind an asynchronous Azure Service Bus queue, satisfying strict batch-window constraints and ensuring zero data loss. It allows gradual, risk-mitigated claim type migration with a one-day fallback capability while supporting a team with limited cloud experience.]