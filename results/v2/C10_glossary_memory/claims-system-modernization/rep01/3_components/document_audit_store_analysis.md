## Overview
The Insurance Claims Modernization platform is a hybrid cloud-native system gradually replacing a legacy on-premise mainframe while ensuring zero-loss claim processing during a 3-year transition. It provides secure online claim submission for external users and efficient case handling for internal claims adjusters.

## Key Elements
- Customers & Brokers [person]
- Claims Adjusters [person]
- Legacy Mainframe [externalSystem] (COBOL/DB2)
- Azure AD (Entra ID) [externalSystem]
- Payment Gateway [externalSystem]
- Core Notification Service [externalSystem]
- Enterprise Service Bus (ESB/MQ) [externalSystem]
- Web Application [container] (React / TypeScript & Next.js)
- Customer Portal [container] (React / TypeScript & Next.js)
- Claim Processing API [container] (Azure Container Apps)
- Integration Gateway / ACL [container] (Azure Container Apps)
- Feature Flag / Migration Router [container] (Azure Container Apps)
- Document & Audit Store [container] (Azure Blob Storage & Azure Cosmos DB)
- Document Repository [component] (Azure Blob Storage with WORM and Azure Key Vault CMK)
- Audit Ledger [component] (Azure Cosmos DB SQL API with change feed)
- Reconciliation & Sync Service [component] (Azure Container Apps with Azure Service Bus)

## Relationships
- Customers & Brokers -> Web Application: HTTPS (REST/GraphQL)
- Customers & Brokers -> Customer Portal: HTTPS (REST/GraphQL)
- Claims Adjusters -> Web Application: HTTPS
- Web Application -> Claim Processing API: HTTPS (REST/GraphQL)
- Customer Portal -> Claim Processing API: HTTPS (REST/GraphQL)
- Claim Processing API -> Feature Flag / Migration Router: Internal gRPC / HTTPS
- Claim Processing API -> Integration Gateway / ACL: Asynchronous messaging via Enterprise Service Bus (ESB/MQ) over AMQP/MQTT with mTLS
- Integration Gateway / ACL -> Legacy Mainframe: Hybrid ESB/MQ connection
- Claim Processing API -> Document Repository: Uploads and retrieves binary assets [HTTPS / TLS 1.3 (Azure SDK)]
- Claim Processing API -> Audit Ledger: Writes transaction and event logs [HTTPS / TLS 1.3 (Azure SDK)]
- Claim Processing API -> Reconciliation & Sync Service: Triggers asynchronous reconciliation tasks [Azure Service Bus / AMQP]
- Reconciliation & Sync Service -> Audit Ledger: Reads/writes state logs [HTTPS / TLS 1.3 (Azure SDK)]
- Reconciliation & Sync Service -> Document Repository: Archives/verifies document states [HTTPS / TLS 1.3 (Azure SDK)]
- Web Application -> Azure AD (Entra ID): OpenID Connect / OAuth 2.0 via HTTPS
- Customer Portal -> Azure AD (Entra ID): OpenID Connect / OAuth 2.0 via HTTPS
- Claim Processing API -> Payment Gateway: HTTPS (REST with OAuth 2.0)
- Claim Processing API -> Core Notification Service: Asynchronous Webhooks via Azure Event Grid (HTTPS)

## Technology Stack
- Azure Container Apps: Hosts microservices using consistent deployment patterns to accommodate the team's limited cloud experience.
- Azure Blob Storage: Secures unstructured binary attachments with WORM immutability policies and Customer-Managed Keys via Azure Key Vault.
- Azure Cosmos DB (SQL API): Maintains append-only transactional audit ledgers with change feed monitoring.
- React / TypeScript & Next.js: Powers responsive web interfaces for customers, brokers, and adjusters.
- Enterprise Service Bus (ESB/MQ): Decouples modern cloud components from the on-premise legacy mainframe.

## Rationale
This hybrid architecture isolates expensive mainframe dependencies behind an Integration Gateway while modernizing user interfaces and backend processing in Azure Container Apps. The modular Document & Audit Store guarantees consistency, tamper-evident compliance, and rapid 24-hour rollback capabilities.