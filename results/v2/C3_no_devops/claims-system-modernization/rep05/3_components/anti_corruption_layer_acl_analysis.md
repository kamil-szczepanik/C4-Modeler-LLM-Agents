## Overview
[System: Insurance Claims Modernization Platform]
[Core Purpose: Hybrid migration platform gradually replacing a 30-year-old COBOL/DB2 mainframe claims system while maintaining continuous business operations.]

## Key Elements
* **Users:** Customers, Brokers, Claims Adjusters, Migration Operations Managers
* **External Systems:** Legacy Mainframe (COBOL/DB2), Active Directory, Notification Service, Payment Gateway
* **Containers:** Web Application (React/Next.js), Claims API Gateway & Processing Service (.NET Core), Anti-Corruption Layer (ACL), Azure Service Bus, Azure SQL Database
* **ACL Components:** Translation Engine, Reconciliation Worker, ACL Admin & Audit API, Metrics Aggregator, ACL Data Store

## Relationships
* Customers / Brokers -> Web Application: Online claim submission [HTTPS / TLS 1.3]
* Claims Adjuster -> Claims API Gateway: Adjuster claim handling UI [HTTPS / REST]
* Claims Processing Service -> Anti-Corruption Layer (ACL): Domain model translation [gRPC / REST]
* Translation Engine -> COBOL/DB2 Mainframe: Legacy system integration [IBM MQ / TCP via ExpressRoute with mTLS]
* ACL Admin & Audit API -> ACL Data Store: Metrics and audit queries [EF Core / SQL]
* Claims Processing Service -> Metrics Aggregator: Event streaming [Azure Service Bus / Kafka Topic]

## Technology Stack
* **Frontend:** React, Next.js (Azure App Service) for modern web interfaces
* **Backend:** .NET Core Web API / Container Apps for scalable microservices
* **Integration:** Azure Service Bus / Apache Kafka for asynchronous messaging
* **Database:** Azure SQL Database and ACL Data Store for transactional and metrics persistence
* **Security:** Azure Key Vault & Managed Identities with Azure AD (OIDC/OAuth2) for SSO and RBAC

## Rationale
[This hybrid architecture isolates expensive mainframe constraints through a dedicated Anti-Corruption Layer, ensuring zero claim loss (R-04) and rapid one-day rollbacks (R-06).]
[It delivers modern web performance under 2 seconds (R-05) while safely bridging cloud infrastructure with the on-premise legacy system over a secure 3-year migration window.]