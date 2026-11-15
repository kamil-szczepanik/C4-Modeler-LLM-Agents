## Overview
The architecture modernizes a regional insurer's legacy mainframe by introducing a hybrid cloud platform on Azure while maintaining the 30-year-old COBOL/DB2 system of record. It enables incremental claim type migration, secure online submissions, and high-performance adjuster workflows without exceeding constraints.

## Key Elements
- **Users**: Customers, Brokers, Claims Adjusters
- **External Systems**: Legacy Mainframe (COBOL/DB2), Insurer’s Active Directory
- **Frontend Containers**: Customer Portal (React SPA on Azure Static Web Apps), Adjuster Workspace (React SPA on Azure Static Web Apps)
- **Backend Containers**: Claims API Management (Azure API Management), Claims BFF (Node.js/Express on Azure App Service), Claims Core Service (Java/Spring Boot on Azure App Service), Mainframe Integration Adapter (Azure App Service Worker)
- **Infrastructure Containers**: Message Broker (Azure Service Bus), Database (Azure SQL Database)
- **Database Components**: MigratedClaims Schema, SyncBuffer Schema, AuditLog Schema

## Relationships
- Customers / Brokers -> Customer Portal [HTTPS / TLS 1.3]
- Claims Adjusters -> Adjuster Workspace [HTTPS / TLS 1.3]
- Customer Portal / Adjuster Workspace -> Claims API Management [HTTPS / REST]
- Claims API Management -> Claims BFF [HTTPS / REST]
- Claims BFF -> Claims Core Service [gRPC / HTTPS]
- Claims Core Service -> Message Broker [AMQP over TLS]
- Message Broker -> Mainframe Integration Adapter [AMQP over TLS]
- Mainframe Integration Adapter -> Legacy Mainframe [SNA / MQ / Batch Files]
- Claims Core Service -> Database [TDS / Azure Managed Identity]
- Mainframe Integration Adapter -> Database [TDS / Azure Managed Identity]

## Technology Stack
- **Frontend**: React SPAs hosted on Azure Static Web Apps for modern, responsive UI.
- **API & Integration**: Azure API Management and Azure Service Bus for decoupled, asynchronous messaging.
- **Backend Runtime**: Node.js/Express (BFF) and Java/Spring Boot (Core Service) on Azure App Service.
- **Database Storage**: Azure SQL Database (Hyperscale/Business Critical) with schemas for migrated claims, sync buffering, and immutable audit logs.
- **Security & Identity**: Azure Active Directory (Entra ID) with SSO, Azure Key Vault (CMK), and Azure Managed Identities.

## Rationale
This hybrid architecture isolates expensive mainframe modifications by incrementally migrating claim types behind a modern API gateway and BFF layer. Azure SQL Database schemas, combined with Azure Service Bus and strict isolation, guarantee zero data loss and enable rapid 24-hour rollbacks.