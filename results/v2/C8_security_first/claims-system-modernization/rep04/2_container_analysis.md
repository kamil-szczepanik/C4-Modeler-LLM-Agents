## Overview
This system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud platform. It enables online claims submission and adjuster workflows while maintaining legacy coexistence.

## Key Elements
- **Users:** Customer / Policyholder, Broker, Claims Adjuster
- **External Systems:** Legacy Mainframe System (COBOL/DB2), Active Directory / Entra ID
- **Containers:** Azure API Management (API Gateway), Customer/Broker Portal, Adjuster Web App, Backend-for-Frontend (BFF), Claim Processing Core, Notification Service, Data Synchronization Worker, Audit & Event Store

## Relationships
- **Customer/Broker Portal -> API Management:** HTTPS via OAuth 2.0 / OpenID Connect (Azure AD)
- **Adjuster Web App -> BFF:** HTTPS / gRPC via Azure Managed Identities
- **BFF -> Azure Cache for Redis:** TLS for caching claim data
- **API Management -> Legacy Mainframe:** Mutual TLS (mTLS) bridging Azure and on-premise
- **Claim Processing Core -> Azure Service Bus:** AMQP / HTTPS for asynchronous messaging
- **Data Synchronization Worker -> Legacy Mainframe:** Batch/Sync integration protocols

## Technology Stack
- **Compute:** Azure Container Apps for low cloud learning curve and managed scaling
- **Integration & Routing:** Azure API Management and Azure Service Bus for hybrid decoupling
- **Caching & State:** Azure Cache for Redis for sub-2-second adjuster screen loads
- **Database & Audit:** Azure SQL (operational store) and Azure Cosmos DB (immutable audit trail)
- **Security & Observability:** Azure Active Directory (Entra ID), Azure Key Vault, Azure Application Insights, OpenTelemetry

## Rationale
This hybrid architecture isolates expensive mainframe changes using an API Gateway and strangler fig pattern, ensuring zero data loss and easy rollback. It meets strict performance SLAs via a caching BFF while accommodating the team's low cloud experience through managed Azure services.