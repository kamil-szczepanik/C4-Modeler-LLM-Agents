## Overview
This hybrid cloud architecture incrementally modernizes a legacy insurance claims platform by migrating claim types one by one to Azure. It maintains the 30-year-old on-premise mainframe as the system of record while using an asynchronous, event-driven integration layer to ensure zero data loss and enable rapid rollbacks.

## Key Elements
- **Users**: Policyholders, Brokers, and Claims Adjusters
- **External Systems**: Microsoft Entra ID (SSO), API Gateway / On-Premise Mainframe (COBOL/DB2)
- **Customer Portal**: React SPA hosted in Azure Static Web Apps
- **Adjuster Web Application**: Node.js/ASP.NET Core BFF paired with a PostgreSQL read-cache
- **Claims Processing Service**: .NET Core microservices handling core domain logic
- **Anti-Corruption Layer (ACL)**: Integration service translating modern events to legacy formats
- **Migration Operations Dashboard**: React SPA and .NET Core API for business reconciliation
- **Messaging & Infrastructure**: Azure Service Bus, Azure Container Apps (ACA), and Azure Key Vault

## Relationships
- **Customers/Brokers -> Customer Portal**: HTTPS (TLS 1.3)
- **Adjusters -> Adjuster Web App**: HTTPS (TLS 1.3) with OpenID Connect / OAuth 2.0 via Microsoft Entra ID
- **Adjuster Web App -> PostgreSQL**: TCP / TLS for low-latency read caching
- **Claims Processing Service <-> Azure Service Bus**: AMQP / HTTPS for asynchronous messaging
- **ACL <-> API Gateway / Mainframe**: gRPC over mTLS and secure IP whitelisting
- **Containers -> Azure Key Vault**: Managed Identities with HTTPS for dynamic secret injection

## Technology Stack
- **Azure Container Apps (ACA)**: Abstracts Kubernetes complexity for a team with low cloud experience
- **.NET Core & Node.js**: Powers microservices and Backend-for-Frontend (BFF) applications
- **PostgreSQL**: Delivers sub-2s read-model caching to decouple from mainframe latency
- **Azure Service Bus**: Ensures reliable messaging, circuit breaking, and dead-letter queueing during mainframe batch windows
- **Microsoft Entra ID**: Enforces Single Sign-On (SSO) and RBAC/ABAC security controls
- **Bicep / Terraform**: Automates infrastructure-as-code deployment with pre-configured Azure Monitor / Application Insights

## Rationale
The hybrid architecture protects the business by keeping the stable legacy mainframe as the system of record while isolating changes via an Anti-Corruption Layer. Using managed Azure services minimizes operational overhead for an inexperienced cloud team while meeting strict sub-2s performance and one-day rollback requirements.