## Overview
[The system is a hybrid cloud insurance claims modernization platform that gradually replaces a legacy mainframe with a modern Azure-based architecture. Its core purpose is to process claims securely while maintaining data consistency and a comprehensive audit trail.]

## Key Elements
- **Users & Personas**: End Customers, Brokers, Claims Adjusters, Compliance & Risk Officer, Operations/Migration Managers
- **External Systems**: Legacy Mainframe System, Azure Active Directory / Identity Provider, Notification Service, Azure Monitor / Sentinel
- **Containers**: Customer Portal, Adjuster Workspace, Azure API Management, Migration Control & Routing Engine, Claims Processing Core, Anti-Corruption Layer & Integration, Reconciliation Worker, Audit & Reconciliation Ledger, Azure Key Vault
- **Audit & Reconciliation Ledger Components**: Ledger Storage Engine (Azure SQL Ledger), Audit Query API (Azure Function), Discrepancy Notification Service (Azure Event Grid / Functions), Reconciliation Data Processor (Azure Function)

## Relationships
- Compliance & Risk Officer -> Audit Query API: Reads immutable audit reports and discrepancy dashboards [HTTPS/REST with OAuth2/OIDC]
- Reconciliation Worker -> Reconciliation Data Processor: Sends reconciliation output streams [HTTP/JSON or Azure Service Bus Queue with Managed Identities]
- Reconciliation Data Processor -> Ledger Storage Engine: Logs reconciliation records and audit data [Database Connection with mTLS / Managed Identities]
- Claims Processing Core -> Ledger Storage Engine: Writes audit logs [Database Connection]

## Technology Stack
- **Compute & Orchestration**: Azure Container Apps, Azure Functions (Consumption/Premium plan)
- **Database & Storage**: Azure SQL Ledger (tamper-evident tables with cryptographic hashing, append-only storage)
- **Integration & Messaging**: Azure Service Bus, Apache Camel, Azure Event Grid
- **Security & Identity**: Azure Active Directory (Entra ID) for OAuth2/OIDC RBAC, Azure Key Vault for Transparent Data Encryption (TDE) with customer-managed keys, Azure Private Endpoints
- **Frontend**: React SPA via Azure Static Web Apps, Node.js/Spring Boot BFF

## Rationale
- [Azure SQL Ledger guarantees unalterable, cryptographically verifiable audit records, satisfying strict regulatory and consistency constraints during the multi-year hybrid migration.]
- [Using lightweight serverless components like Azure Functions minimizes cloud complexity, directly aligning with the team's limited prior cloud experience while ensuring robust scalability.]