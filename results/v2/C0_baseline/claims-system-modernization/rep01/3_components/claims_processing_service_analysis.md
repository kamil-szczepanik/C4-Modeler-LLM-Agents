## Overview
Gradually replaces a 30-year-old mainframe claims system with a modern Azure-hosted platform while maintaining legacy processing. The system ensures zero data loss and enables continuous operations during a three-year hybrid migration.

## Key Elements
- **Users**: Policyholders, Brokers, and Claims Adjusters
- **External Systems**: API Gateway, Legacy Mainframe, Microsoft Entra ID
- **Containers**: Customer Portal (React SPA in Azure Static Web Apps), Adjuster Web Application (Node.js/ASP.NET Core BFF), PostgreSQL Read-Cache, Claims Processing Service (.NET Core microservices), Anti-Corruption Layer (ACL), Migration Operations Dashboard, Azure Service Bus, Azure Container Apps, Azure Key Vault
- **Components (Claims Processing Service)**: Claim Orchestrator Component, Claim Domain Model Component, Exception Handler Component, Integration Client Component

## Relationships
- Customer Portal & Adjuster Web Application -> API Gateway: Secure HTTPS requests
- API Gateway -> Claims Processing Service: mTLS and JWT validation via Microsoft Entra ID [HTTPS]
- Claims Processing Service -> Azure Service Bus: Asynchronous messaging [AMQP / TLS 1.3]
- Claims Processing Service -> Anti-Corruption Layer (ACL): Resilient communication with circuit breakers [HTTPS / Polly]
- Anti-Corruption Layer -> Legacy Mainframe: Synchronized legacy database updates [DB2 / SNA]

## Technology Stack
- **Compute**: Azure Container Apps (hosting .NET Core microservices and Node.js BFF)
- **Database**: PostgreSQL (handling read-cache and persistent state)
- **Messaging**: Azure Service Bus (managing asynchronous domain events and dead-letter queues)
- **Security & Secrets**: Microsoft Entra ID (SSO/JWT) and Azure Key Vault with Managed Identities (CMK encryption)
- **Resilience & Tracing**: Polly (.NET circuit breakers) and OpenTelemetry (distributed tracing)

## Rationale
The hybrid container architecture isolates the fragile legacy mainframe using an Anti-Corruption Layer and circuit breakers, ensuring sub-2-second adjuster response times. Lean .NET Core microservices deployed in Azure match the team's cloud skillset while meeting strict consistency and rollback requirements.