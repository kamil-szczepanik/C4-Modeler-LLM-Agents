## Overview
[The Migration Control Service manages dynamic routing rules and audit reconciliation for the hybrid insurance claims platform. It ensures zero data loss and enables rapid claim-type rollbacks between the legacy mainframe and modern Azure services.]

## Key Elements
- **Migration API Controller**: Exposes REST endpoints for routing rules.
- **Reconciliation Engine**: Compares Cosmos DB state with DB2 audit logs.
- **Control Dashboard Backend**: Serves APIs for live monitoring and rollbacks.
- **State Store**: Azure Cosmos DB storing routing tables and migration state.
- **Audit & Compliance Logger**: Captures rule modifications with user context.
- **Alert Dispatcher**: Translates sync drifts into operational incidents.

## Relationships
- **Migration Router & Integration Service** -> **Migration API Controller**: HTTPS (REST) via Private Endpoints
- **Reconciliation Engine** -> **Azure Cosmos DB**: Cosmos DB Change Feed over TLS 1.3
- **Control Dashboard Backend** -> **Azure Entra ID**: HTTPS (OAuth 2.0 / OIDC) for RBAC
- **Migration Control Service** -> **Azure Key Vault**: HTTPS for secret/key retrieval

## Technology Stack
- **Azure App Service (.NET 8)**: Chosen for managed hosting and operational simplicity given low cloud experience.
- **Azure Cosmos DB**: Chosen for strong consistency and Change Feed capabilities.
- **Azure Entra ID**: Used for secure RBAC and single sign-on.
- **Azure Application Insights**: Used for structured logging and metric alerts.

## Rationale
[This architecture simplifies cloud operations for an inexperienced team while providing robust hybrid consistency controls. It meets strict non-functional requirements for zero data loss and one-day rollbacks via managed Azure services.]