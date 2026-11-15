## Overview
[The system is a hybrid Insurance Claims Modernization platform that gradually replaces a legacy COBOL/DB2 mainframe with Azure-based microservices. Its core purpose is to enable online claim submission and adjuster processing while maintaining continuous legacy data synchronization over a three-year migration window.]

## Key Elements
- Policyholders and Brokers
- Claims Adjusters
- Compliance and Audit Officers
- COBOL/DB2 Mainframe
- Azure Active Directory / Entra ID
- Azure API Gateway / Azure APIM
- Claims Web App (Azure AKS, ASP.NET Core / React)
- Integration Service (Azure AKS, .NET)
- Claim Reconciliation Service (Azure AKS, .NET)
- Azure Cache for Redis
- Azure Service Bus
- Azure Key Vault
- Azure App Configuration
- Azure Monitor and Application Insights
- Azure Sentinel

## Relationships
- Policyholders and Brokers -> Claims Web App: Online claim submission [HTTPS / TLS 1.3]
- Claims Adjusters -> Claims Web App: Handles claims and views adjuster screens [<2s load time, HTTPS]
- Claims Web App -> Azure API Gateway: API requests [HTTPS / REST]
- Azure API Gateway -> Integration Service: Routes claims traffic and applies rate-limiting [HTTPS]
- Integration Service -> COBOL/DB2 Mainframe: Hybrid data exchange and legacy queries [mTLS 1.3 with certificate pinning]
- Integration Service -> Azure Service Bus: Publishes messages and dead-letter queues [AMQP / Azure SDK]
- Integration Service -> Azure Cache for Redis: Caches transit data with customer-managed keys [Redis Protocol over TLS]
- Integration Service -> Azure App Configuration: Dynamic feature flags for claim type rollbacks [HTTPS]
- Integration Service -> Azure Key Vault: Retrieves mainframe client certificates and credentials via CSI secret drivers [HTTPS]
- Integration Service -> Azure Sentinel: Forwards audit and authorization logs [Syslog / Azure Diagnostics]

## Technology Stack
- Azure Kubernetes Service (AKS): Hosts containerized microservices (.NET) for scalability and blue/green deployments.
- Azure API Management / API Gateway: Offloads hybrid routing, perimeter rate-limiting, and throttling.
- Azure Service Bus: Provides reliable messaging and dead-letter queues to prevent data loss.
- Azure Key Vault: Secures mainframe mTLS certificates and credentials with automated zero-downtime rotation.
- Azure App Configuration: Enables runtime feature flags for rapid 1-day claim type rollbacks without mainframe updates.
- Azure Monitor and Application Insights: Delivers managed observability and pre-built business-metric dashboards for teams with low cloud experience.
- Azure Sentinel: Centralizes security and audit logging for compliance.

## Rationale
[This hybrid architecture bridges the 5-second mainframe response lag to deliver sub-2-second adjuster screen loads while keeping the legacy system as the primary system of record. It guarantees compliance, zero data loss, and rapid one-day rollbacks through managed Azure services and robust integration patterns.]