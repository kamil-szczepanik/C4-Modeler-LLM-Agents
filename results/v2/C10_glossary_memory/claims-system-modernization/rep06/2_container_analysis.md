## Overview
[The system is a hybrid insurance claims modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with modern cloud services. Its core purpose is to enable online claim submissions and fast adjuster workflows while maintaining synchronization with the legacy system.]

## Key Elements
- [Customer Portal App (React/TypeScript, Azure Static Web Apps)]
- [Adjuster Web App (React/Node.js BFF)]
- [Claims Core API (.NET Core modular monolith, Azure Container Apps)]
- [Integration Worker (.NET background service, Azure Container Apps)]
- [Audit & Compliance Service (Azure Function)]
- [Claim Read Database (Azure SQL Database)]
- [Azure Service Bus]
- [Enterprise Service Bus / Integration Gateway]
- [Legacy Mainframe COBOL/DB2 System of Record]
- [Insurer Active Directory / Azure Entra ID]

## Relationships
- [Customers & Brokers -> Customer Portal App (HTTPS / JSON)]
- [Claims Adjusters -> Adjuster Web App (HTTPS / HTML)]
- [Customer Portal App & Adjuster Web App -> Claims Core API (HTTPS / JSON)]
- [Claims Core API -> Claim Read Database (TDS / TCP)]
- [Claims Core API -> Azure Service Bus (AMQP)]
- [Integration Worker -> Azure Service Bus (AMQP)]
- [Azure Service Bus -> Enterprise Service Bus / Integration Gateway (IPsec VPN / Azure ExpressRoute, TLS 1.3)]
- [Enterprise Service Bus / Integration Gateway -> Legacy Mainframe COBOL/DB2 System of Record (Managed File Transfer / MQ / APIs)]
- [Customer Portal App & Adjuster Web App -> Insurer Active Directory (OIDC / OAuth2 via Azure Entra ID Connect)]

## Technology Stack
- [Azure Container Apps: Unified hosting for backend services balancing microservice separation with low operational complexity for teams with limited cloud experience.]
- [Azure SQL Database: Provides relational storage with Transparent Data Encryption (TDE) and Private Endpoints for data protection and fast read performance.]
- [Azure Service Bus: Asynchronous messaging to buffer events and handle the nightly mainframe batch window (23:00-05:00).]
- [.NET Core: Backend runtime for core business logic, APIs, and background worker processes.]
- [Azure Key Vault: Secure runtime credential and secret injection using managed identities.]

## Rationale
[This hybrid architecture decouples modern web interfaces from the legacy mainframe, satisfying performance requirements via read-side caching despite slow mainframe responses. The container design isolates components to ensure reliable data consistency and modular claim-type rollbacks within the required timeframe.]