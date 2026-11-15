## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid cloud platform. It enables online claim submissions and adjuster workflows while maintaining synchronization with the legacy system of record.

## Key Elements
* Customer / Broker: External actors submitting claims online.
* Claims Adjuster: Internal users handling claims.
* Web App Portal: React frontend hosted on Azure App Service.
* Claims API Gateway / BFF: Azure API Management and .NET Core.
* Core Claims Service: .NET Core on Azure Container Apps.
* Integration & Sync Service: Azure Service Bus and Azure Functions.
* Feature Flag / Routing Service: Azure App Configuration and .NET Core middleware.
* Claims Database: Azure SQL Database.
* Legacy Mainframe System: On-premises COBOL/DB2 system.
* Active Directory & Integration Gateway: On-premises enterprise services.

## Relationships
* Customer / Broker and Claims Adjuster access Web App Portal via HTTPS.
* Web App Portal communicates with Claims API Gateway / BFF using HTTPS.
* Claims API Gateway / BFF authenticates users via Active Directory using OIDC/OAuth2, and routes requests via gRPC/HTTPS.
* Core Claims Service persists and retrieves data from Azure SQL Database using TDS/ADO.NET.
* Integration & Sync Service communicates with the on-premises Integration Gateway via AMQP and HTTPS.
* Feature Flag / Routing Service dynamically directs claim traffic between Core Claims Service and Integration Gateway.

## Technology Stack
* React & Azure App Service: Delivers sub-2s UI loads independently of backend latency.
* .NET Core & Azure API Management: Provides robust API orchestration and security.
* Azure Container Apps: Serverless Kubernetes abstraction mitigates the team's low cloud experience.
* Azure Service Bus & Azure Functions: Asynchronous messaging guarantees transactional consistency and respects batch windows.
* Azure App Configuration: Enables the 1-day rollback requirement per claim type.
* Azure SQL Database: ACID compliance ensures no data loss during incremental migration.

## Rationale
This hybrid architecture isolates the fragile on-premises mainframe while leveraging Azure's scalable services for modern frontend and backend processing. It satisfies strict consistency, performance, and maintainability requirements with minimal cloud expertise.