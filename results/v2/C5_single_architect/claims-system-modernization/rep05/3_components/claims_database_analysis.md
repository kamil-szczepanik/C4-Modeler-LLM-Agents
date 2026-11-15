## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid cloud platform on Azure West Europe. It enables online claim submission, adjuster processing, and incremental claim type migration while maintaining system stability and data consistency.

## Key Elements
- **Users**: Customer, Broker, Claims Adjuster
- **External Systems**: Legacy Mainframe System (COBOL/DB2, On-Premises), Active Directory, Integration Gateway
- **Containers**: Web App Portal (React, Azure App Service), Claims API Gateway / BFF (.NET Core, Azure API Management), Core Claims Service (.NET Core, Azure Container Apps), Integration & Sync Service (Azure Service Bus, Azure Functions), Feature Flag / Routing Service (.NET Core, Azure App Configuration), Claims Database (Azure SQL Database)
- **Claims Database Components**: Claim Repository Component (.NET Entity Framework Core), Audit & Reconciliation Component (Azure SQL Stored Procedures/Change Tracking), Migration Schema Versioning Component (FluentMigrator), Temporal History & Rollback Component (Azure SQL System-Versioned Temporal Tables)

## Relationships
- Customer / Broker -> Web App Portal: Submits claims [HTTPS / TLS]
- Claims Adjuster -> Web App Portal: Handles claims [HTTPS / TLS]
- Web App Portal -> Claims API Gateway / BFF: Routes API requests [HTTPS / REST]
- Claims API Gateway / BFF -> Core Claims Service: Forwards domain operations [gRPC / HTTPS]
- Core Claims Service -> Integration & Sync Service: Publishes migration sync events [AMQP / Azure Service Bus]
- Integration & Sync Service -> Legacy Mainframe System: Syncs records [MQ / Batch]
- Core Claims Service -> Claim Repository: Invokes data access [In-Process / C# Method Calls]
- Claim Repository -> Azure SQL Storage Engine: Executes queries [TDS / TCP 1433]
- Claim Repository -> Temporal History Component: Manages row versions [In-Process / T-SQL]
- Audit & Reconciliation Component -> Claim Repository: Reads state snapshots [In-Process / LINQ]
- Web App Portal / Core Claims Service -> Active Directory: Handles single sign-on [OIDC / OAuth2 / LDAPS]

## Technology Stack
- **Azure SQL Database**: Provides native ACID compliance and temporal tables to guarantee zero data loss (R-04) and support one-day rollbacks (R-06).
- **.NET Core & Entity Framework Core**: Powers robust backend services and relational data access with low maintenance overhead for a cloud-inexperienced team.
- **Azure Container Apps & App Service**: Host microservices and web apps natively on Azure.
- **Azure Service Bus**: Handles asynchronous messaging for hybrid integration.

## Rationale
This hybrid architecture isolates the expensive-to-change mainframe while modernizing claim types incrementally via Azure. Native cloud database features minimize custom application logic for data consistency and rollbacks, fitting a team with limited cloud experience.