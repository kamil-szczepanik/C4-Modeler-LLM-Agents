## Overview
[Hybrid modernization platform replacing a 30-year-old COBOL/DB2 mainframe claims system incrementally with a cloud-native Azure architecture. Enables online claim submissions and adjuster web workflows while maintaining legacy data consistency for three years.]

## Key Elements
* Customer/Broker Portal (Azure Container Apps)
* Adjuster Web App (Azure Container Apps)
* Azure API Management (API Gateway)
* Claim Processing Core (Azure Container Apps / Azure Service Bus)
* Data Synchronization Worker (Azure Container Apps)
* Audit & Event Store (Azure Cosmos DB / Azure SQL)
* Legacy Mainframe System (COBOL/DB2 on-prem)
* Active Directory / Entra ID

## Relationships
* Customer/Broker Portal -> Azure API Management [HTTPS/TLS 1.3]
* Adjuster Web App -> Azure API Management [HTTPS/TLS 1.3]
* Azure API Management -> Claim Processing Core [HTTPS/REST]
* Data Synchronization Worker -> Legacy Mainframe System [gRPC/mTLS over ExpressRoute]
* Data Synchronization Worker -> Claim Processing Core [AMQP / Azure Service Bus SDK]
* Claim Processing Core -> Audit & Event Store [Cosmos DB SDK]

## Technology Stack
* Azure Container Apps: Container hosting chosen for simplicity given low team cloud experience.
* Azure Service Bus: Asynchronous messaging for reliable event-driven claim processing.
* Spring Boot / Apache Camel: Core framework and protocol translation for the integration worker.
* Azure Cosmos DB: Scalable audit and event store for tracking claim states.
* Azure Cache for Redis: High-performance idempotency tracking and deduplication.
* Azure Key Vault & Managed Identities: Secure credential management and RBAC.

## Rationale
[The hybrid architecture isolates fragile mainframe dependencies behind secure integration gateways while modernizing user-facing applications on Azure. This design fulfills strict consistency, security, and rollback requirements without exceeding the team's cloud expertise.]