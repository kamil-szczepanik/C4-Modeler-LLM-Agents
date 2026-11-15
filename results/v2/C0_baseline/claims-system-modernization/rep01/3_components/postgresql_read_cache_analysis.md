## Overview
The architecture implements a hybrid insurance claims platform using Azure Database for PostgreSQL to cache mainframe data for modern adjusters. It ensures sub-2-second response times while maintaining data synchronization during the three-year legacy migration.

## Key Elements
- Cache Storage Engine (Azure Database for PostgreSQL Flexible Server)
- Sync Consumer Component (.NET worker hosted in Azure Container Apps)
- Audit & Versioning Manager (.NET Library / Service Layer)
- Azure Service Bus
- Azure Key Vault
- Adjuster Web Application

## Relationships
- Adjuster Web Application -> Cache Storage Engine: Queries claim read-models [PostgreSQL Protocol / TLS 1.3]
- Anti-Corruption Layer / Azure Service Bus -> Sync Consumer Component: Ingests delta change events [AMQP]
- Sync Consumer Component -> Cache Storage Engine: Writes updates via connection pooling [TCP / TLS 1.3]
- Cache Storage Engine -> Azure Key Vault: Retrieves Customer-Managed Keys for TDE [HTTPS / REST]

## Technology Stack
- Azure Database for PostgreSQL Flexible Server: Managed database instance to reduce stateful cloud operations overhead
- .NET / Azure Container Apps: Scalable worker hosting for asynchronous event consumption
- Azure Service Bus: Asynchronous messaging broker for handling change data feeds
- Microsoft Entra ID & Azure RBAC: Enforces secretless authentication and least-privilege database roles

## Rationale
Managed Azure services minimize operational complexity for a cloud-inexperienced team while meeting strict security standards. Decomposing the read-cache into isolated read, write, and audit components guarantees sub-2-second UI performance and data freshness without risking the legacy mainframe.