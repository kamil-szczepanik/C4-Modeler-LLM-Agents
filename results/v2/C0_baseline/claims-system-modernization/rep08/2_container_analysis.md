## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe with a cloud-native architecture. It ensures seamless parallel processing and quick rollback capabilities while maintaining continuous business operations.

## Key Elements
* Customers and Brokers
* Claims Adjusters and Migration Operations Manager
* Customer Portal (SPA React/TypeScript)
* Adjuster Workspace (SPA React/TypeScript)
* API Gateway / Backend-for-Fronend (.NET 8 Web API)
* Claims Domain Services (.NET 8 Microservices on Azure Container Apps)
* Integration & Sync Engine (Azure Functions + Azure Service Bus)
* Azure App Configuration
* Legacy Mainframe (COBOL/DB2) and Enterprise Integration Bus
* Azure Key Vault and Azure Entra Institute / Active Directory

## Relationships
* Customers/Brokers to Customer Portal via HTTPS/REST
* Adjusters to Adjuster Workspace via HTTPS
* Adjuster Workspace to API Gateway via HTTPS/REST
* API Gateway to Claims Domain Services via gRPC/HTTPS
* Integration & Sync Engine to Legacy Mainframe via Enterprise Integration Bus using mTLS
* Services to Azure Key Vault and Azure App Configuration via Managed Identities

## Technology Stack
* Frontend: React/TypeScript via Azure CDN for fast global content delivery
* Backend: .NET 8 Web API and Azure Container Apps for manageable cloud microservices
* Integration: Azure Service Bus and Azure Functions for reliable asynchronous event processing
* Security & State: Azure Entra ID, Azure Key Vault, and Azure App Configuration for managed security and feature flagging
* Observability: Azure Application Insights for distributed tracing and synthetic monitoring

## Rationale
Managed Azure PaaS and Container Apps minimize operational overhead for a cloud-novice team. Event-driven synchronization, circuit breakers, and feature flags guarantee strict consistency, performance, and 1-day rollback capabilities without disrupting the legacy mainframe.