## Overview
[Insurance Claims Modernization]
Gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure cloud platform while maintaining uninterrupted legacy claim processing.

## Key Elements
- Web Portal: React SPA on Azure Static Web Apps for customers and brokers
- Adjuster Workspace: React app on Azure App Service for claims handlers
- API Management Proxy: Azure API Management gateway
- Claims Processing Service: Java/Spring Boot on Azure Container Apps
- Messaging & Datastores: Azure Service Bus, Azure SQL Database, Azure Cosmos DB / Redis, IBM MQ (on-premises)
- Backend Integration: Data Sync Worker (Java/Spring Boot), Audit and Reconciliation Service (Azure Functions)

## Relationships
- Customer & Broker -> Web Portal: Submits claims [HTTPS/TLS]
- Web Portal -> API Management Proxy: Routes portal traffic [HTTPS/TLS]
- Notification Banner (Adjuster Workspace) -> API Management Proxy: Receives real-time alerts [WebSocket/WSS]
- API Management Proxy -> Claims Processing Service: Forwards validated requests [HTTPS/REST]
- Claims Processing Service <-> Mainframe Integration Adapter: Syncs hybrid workloads [IBM MQ / on-premises]

## Technology Stack
- Frontend: React / TypeScript with TanStack Query and MSAL.js for UI performance (R-05) and Azure AD SSO (R-07)
- Backend Compute: Azure Container Apps with Java / Spring Boot for microservices
- Data Layer: Azure SQL Database for primary relational store, Azure Cosmos DB / Redis for read models
- Integration: Azure Service Bus for messaging, IBM MQ for mainframe connectivity

## Rationale
[Hybrid Cloud Architecture]
A hybrid approach isolates expensive mainframe changes while leveraging managed Azure services to meet strict performance and zero-loss migration constraints.