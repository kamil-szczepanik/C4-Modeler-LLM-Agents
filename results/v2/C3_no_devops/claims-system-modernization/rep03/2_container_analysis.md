## Overview
The system incrementally modernizes a legacy regional insurance claims platform by migrating claim types to a hybrid cloud architecture. It maintains operational continuity and zero data loss while interacting with an on-premise mainframe.

## Key Elements
- **Users:** Customer, Broker, Claims Adjuster, Finance/Compliance Auditor
- **External Systems:** Legacy Mainframe Claims System, Azure Active Directory (Identity Provider)
- **Containers:** 
  - API Gateway (Azure API Management)
  - Customer Portal & Adjuster Web App (Azure Container Apps / React)
  - Claims Domain Services (Azure Container Apps / .NET Core)
  - Integration & Anti-Corruption Layer (Azure Service Bus)
  - Claims Audit Store (Azure Cosmos DB)
  - Mainframe Adapter (Azure Container Apps / .NET Core)

## Relationships
- Customer/Broker/Adjuster/Auditor to API Gateway via HTTPS (TLS 1.3) with OpenID Connect (OIDC) JWT tokens
- API Gateway to Customer Portal, Adjuster Web App, and Claims Domain Services via HTTPS
- Claims Domain Services to Claims Audit Store via HTTPS (Document API)
- Claims Domain Services to Integration Layer via AMQP (Azure Service Bus)
- Integration Layer to Mainframe Adapter via AMQP
- Mainframe Adapter to Legacy Mainframe via custom TCP/LU6.2 bridging over Azure ExpressRoute/IPsec VPN with mTLS

## Technology Stack
- **Compute:** Azure Container Apps for abstracting Kubernetes complexity for the cloud-inexperienced team
- **Frontend:** React for responsive UI meeting the sub-2s performance constraint
- **Backend & Integration:** .NET Core for domain microservices and legacy adapters
- **Messaging:** Azure Service Bus with transactional outbox pattern to respect batch windows and ensure zero data loss
- **Database:** Azure Cosmos DB for append-only, immutable business event auditing and PII encryption
- **Security:** Azure API Management and Azure AD for SSO and RBAC enforcement

## Rationale
This hybrid architecture isolates domains to enable independent claim type migration and rapid one-day rollbacks. It protects legacy mainframe constraints while leveraging managed Azure services to minimize cloud operational overhead.