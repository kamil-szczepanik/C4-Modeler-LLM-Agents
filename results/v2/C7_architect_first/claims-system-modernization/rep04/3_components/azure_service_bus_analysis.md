## Overview
Modernizes a regional insurer's legacy COBOL/DB2 claims platform via a hybrid cloud architecture. Azure components process migrated claim types while maintaining integration with the on-premises system of record.

## Key Elements
- Users: Customer/Broker, Claims Adjuster
- External Systems: Legacy Mainframe, Corporate Active Directory
- Containers: Customer Portal (React, Azure Static Web Apps), Adjuster Workspace (.NET Core, Azure App Service), Claims Integration Service (.NET Core Worker Service, Azure Container Apps), Mainframe Adapter (.NET Core API, On-Premises)
- Message Broker: Azure Service Bus (Premium Tier, AMQP)
- Security & Secrets: Azure Key Vault, Azure Entra ID (RBAC)

## Relationships
- Customer Portal -> Claims Integration Service: Submits online claims [HTTPS/REST]
- Adjuster Workspace -> Claims Integration Service: Manages claims [HTTPS/REST]
- Claims Integration Service -> Azure Service Bus (`claims-lifecycle` Topic): Publishes claim state changes [AMQP]
- Azure Service Bus (`mainframe-sync-queue`) -> Mainframe Adapter: Dispatches queued legacy transactions [AMQP]
- Mainframe Adapter -> Legacy Mainframe: Updates system of record [DB2/COBOL interface]
- All Azure Containers -> Corporate Active Directory: Single Sign-On authentication [OpenID Connect/OAuth 2.0]

## Technology Stack
- Azure Service Bus Premium Tier: Provides native VNet integration, dedicated capacity, sessions, and duplicate detection for zero data loss.
- .NET Core: Core application framework for modern cloud containers and integration workers.
- React: Frontend library for Customer Portal and Adjuster Workspace.
- Azure Key Vault with Managed Identities: Manages application-level PII encryption keys and secrets without hardcoded credentials.
- Azure Entra ID: Enforces role-based access control (RBAC) across all microservices and Azure Service Bus.

## Rationale
The hybrid architecture isolates expensive mainframe dependencies while allowing gradual, risk-free migration of claim types one by one. Azure Service Bus guarantees zero data loss, supports strict batch-window constraints, and enables rapid switch-back to the legacy system within one day if needed.