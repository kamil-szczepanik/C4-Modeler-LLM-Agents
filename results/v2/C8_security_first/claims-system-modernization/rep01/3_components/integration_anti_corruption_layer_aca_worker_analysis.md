## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud platform. It ensures business continuity by maintaining zero data loss (R-04) and enabling rapid 1-day rollbacks (R-06) during the 3-year migration.

## Key Elements
- **Users**: Customers & Brokers, Claims Adjusters
- **Containers**: Customer Portal, Adjuster Web App, Claims API Gateway, Claims Core Services, Notification Service, Feature/Routing Service, Integration / Anti-Corruption Layer (ACA Worker)
- **External Systems**: Legacy Mainframe System (COBOL/DB2), Core Banking / Payment Gateway, Active Directory / Identity Provider
- **ACA Worker Components**: Message Consumer Component, Translation / Mapper Component, Legacy Adaptor Component, Outbox / Audit Dispatcher Component
- **Infrastructure**: Azure Service Bus, Azure SQL Database, Azure Key Vault, Azure Container Apps

## Relationships
- ACA Worker -> Legacy Mainframe System: Interfaces with legacy backend for hybrid operations via custom TCP sockets encapsulated in mTLS over IPsec VPN / ExpressRoute
- Message Consumer & Outbox / Audit Dispatcher -> Azure Service Bus: Consumes and dispatches messages via AMQP over TLS 1.3
- Outbox / Audit Dispatcher -> Azure SQL Database: Persists transaction states via TDS (Tabular Data Stream) using Managed Identity
- ACA Worker -> Azure Key Vault: Retrieves certificates and secrets using Azure Container Apps Managed Identities

## Technology Stack
- **ACA Worker Runtime**: Azure Container Apps (Worker profile) chosen for managed container scaling with minimal cloud experience.
- **Language & Framework**: .NET Worker Service (C#) for robust asynchronous message processing.
- **Data & Messaging**: Azure Service Bus with Dead-Letter Queues (DLQs) and Azure SQL Database for transactional outbox pattern (R-04).
- **Security**: Azure AD for SSO and Azure Key Vault for secret management.
- **Infrastructure-as-Code**: Bicep/Terraform for repeatable, safe deployments.

## Rationale
This hybrid architecture isolates complex legacy mainframe dependencies behind an Anti-Corruption Layer, protecting cloud users from 5-second mainframe latencies to guarantee sub-2-second UI responses. Utilizing managed Azure services mitigates the team's low cloud experience while strictly enforcing security, auditability, and zero-loss data consistency.