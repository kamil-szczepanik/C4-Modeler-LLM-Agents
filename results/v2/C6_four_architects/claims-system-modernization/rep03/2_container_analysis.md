## Overview
The system is an Insurance Claims Modernization platform that gradually replaces a 30-year-old on-premises mainframe with a cloud-native architecture. It runs in a hybrid environment to ensure continuous claims processing during migration.

## Key Elements
- Users: Customer, Broker, Claims Adjuster
- External Systems: Active Directory, Core Rating & Underwriting Engine, Payment Gateway, Notification Service, Legacy Mainframe
- Containers: API Gateway / BFF, Web Portal, Adjuster Web Application, Claims Management App, Integration & Sync Service, Claim Routing Service, Claims Database, Mainframe Data Ingestion Worker, Notification & Document Store, Observability & Audit Container
- Components (Claims Management App): API / Controller Layer, Domain / Business Logic Layer, Data Access Layer, Mainframe Anti-Corruption Layer (ACL)

## Relationships
- Users -> Web Portal & Adjuster Web Application via HTTPS
- Web Portal & Adjuster Web Application -> API Gateway via HTTPS
- API Gateway -> Claims Management App via gRPC/HTTP
- Claims Management App -> Claim Routing Service via gRPC/REST
- Claims Management App -> Integration & Sync Service via AMQP/Azure Service Bus
- Claims Management App -> Claims Database via Entity Framework Core / TDS
- Claims Management App -> Notification & Document Store via HTTPS/Blob SDK
- Integration & Sync Service -> Mainframe Data Ingestion Worker via Azure Service Bus
- Integration & Sync Service -> Legacy Mainframe via secure FTP/MQ
- All Azure Containers -> Observability & Audit Container via OpenTelemetry/HTTPS

## Technology Stack
- Frontends: React / TypeScript on Azure Static Web Apps for unified web interfaces
- API Routing & SSO: Azure API Management and Node.js with Active Directory integration
- Compute & Services: Azure Container Apps, Azure Functions, Azure Service Bus, Azure Data Factory
- Databases & Storage: Azure SQL Database, Azure Cosmos DB, Azure Blob Storage
- Observability: Azure Application Insights and Azure Monitor

## Rationale
This hybrid architecture uses managed Azure services to compensate for the team's limited cloud experience while strictly isolating the expensive-to-change legacy mainframe. It guarantees zero data loss and rapid one-day rollbacks per claim type via a dedicated routing service and caching layer.