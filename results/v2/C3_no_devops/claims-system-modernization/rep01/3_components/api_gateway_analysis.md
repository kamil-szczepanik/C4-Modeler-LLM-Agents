## Overview
[A hybrid cloud platform gradually replacing a 30-year-old mainframe claims system for a regional insurer. It enables modern online claim submission while maintaining legacy system of record compatibility.]

## Key Elements
- End Customers & Brokers, Claims Adjusters
- Legacy Mainframe, Corporate Active Directory
- API Gateway (.NET / YARP on Azure Container Apps)
- Claims Core Domain Service (.NET Core), Read-Model & Caching Store (Azure Cosmos DB / Redis)
- Azure SQL Database, Azure Key Vault, Azure Functions

## Relationships
- Web Application -> API Gateway: Forwards requests [HTTPS/JSON]
- API Gateway -> Claims Core Domain Service: Routes internal requests [gRPC/mTLS]
- API Gateway -> Corporate Active Directory: Validates JWTs [HTTPS]

## Technology Stack
- Azure Container Apps / YARP: Chosen for lightweight, scalable API routing within team skill limits.
- .NET Core: Provides robust performance for domain services meeting <2s SLA.
- Azure Cosmos DB / Redis: Ensures low-latency read models for adjuster screens.
- Azure Key Vault: Secures credentials and routing certificates via managed identities.

## Rationale
[The hybrid architecture isolates expensive mainframe changes while modernizing user-facing components via Azure. It satisfies strict latency, security, and incremental migration requirements.]