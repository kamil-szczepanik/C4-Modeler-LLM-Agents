## Overview
Gradually replaces a 30-year-old mainframe claims system with a modern hybrid platform while legacy processing continues. Utilizes Azure cloud services and asynchronous messaging to modernize user interfaces while protecting legacy constraints.

## Key Elements
- Customers & Brokers, Claims Adjusters, Finance & Compliance Auditors
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
- Customers & Brokers -> Customer Portal App [HTTPS / JSON]
- Claims Adjusters -> Adjuster Web App [HTTPS / HTML]
- Customer Portal App -> Claims Core API [HTTPS / JSON]
- Adjuster Web App -> Claims Core API [HTTPS / JSON]
- Claims Core API -> Claim Read Database [TDS / TCP]
- Claims Core API -> Azure Service Bus [AMQP]
- Integration Worker -> Azure Service Bus [AMQP]
- Azure Service Bus -> Enterprise Service Bus / Integration Gateway [IPsec VPN / Azure ExpressRoute, TLS 1.3]
- Enterprise Service Bus / Integration Gateway -> Legacy Mainframe COBOL/DB2 System of Record [Managed File Transfer / MQ / APIs]
- Customer Portal App -> Insurer Active Directory [OIDC / OAuth2 via Azure Entra ID Connect]
- Adjuster Web App -> Insurer Active Directory [OIDC / OAuth2 via Azure Entra ID Connect]

## Technology Stack
- Azure Static Web Apps: Hosts SPAs with global CDN distribution and minimal operational overhead.
- Azure Container Apps: Runs .NET Core microservices without complex infrastructure management.
- Azure SQL Database: Stores read models to isolate frontend traffic from mainframe latency.
- Azure Service Bus: Asynchronously buffers events to protect against the rigid nightly mainframe batch window.
- Azure Entra ID Connect: Delivers secure single sign-on integrating with on-premise Active Directory.

## Rationale
This hybrid architecture isolates expensive mainframe dependencies behind asynchronous queues and read models, ensuring high performance for users. It enables incremental, low-risk claim type migration while strictly preserving data consistency and supporting teams with limited cloud experience.