## Overview
- Gradually modernizes a regional insurer's legacy mainframe by decoupling online submission and adjuster interfaces using managed Azure services and asynchronous integration patterns.
- Replaces the 30-year-old COBOL/DB2 system over a three-year period while maintaining operational continuity, data consistency, and strict security compliance.

## Key Elements
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
- Azure Static Web Apps: Hosts React/TypeScript frontend for customers and brokers.
- Azure Container Apps: Runs containerized .NET Core APIs and background integration workers.
- Azure SQL Database: Provides relational read storage with encryption, private endpoints, and Dynamic Data Masking.
- Azure Service Bus: Buffers asynchronous event messaging to protect the mainframe batch window.
- Azure Active Directory (Entra ID Connect): Delivers single sign-on and MFA.

## Rationale
- Hybrid cloud architecture allows the legacy mainframe to remain the system of record while incrementally migrating claim types.
- Managed Azure services minimize operational overhead for a team with limited cloud experience while meeting strict sub-2-second performance and security constraints.