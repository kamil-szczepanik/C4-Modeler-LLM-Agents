## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old on-premises COBOL/DB2 mainframe with a hybrid cloud platform on Azure West Europe. It enables online claim submission and adjuster workflows while maintaining data consistency and supporting rapid rollback.

## Key Elements
* Customer / Broker & Claims Adjuster (Users)
* Legacy Mainframe System (On-Premises System of Record)
* Active Directory (Identity Provider)
* Web App Portal (React SPA, Azure App Service)
  * Authentication Wrapper (MSAL.js)
  * Claim Submission & Routing Module
  * Adjuster Workspace Module
  * Feature Flag Client (Azure App Configuration SDK)
* Claims API Gateway / BFF (.NET Core, Azure API Management)
* Core Claims Service (.NET Core, Azure Container Apps)
* Integration & Sync Service (Azure Service Bus, Azure Functions)
* Claims Database (Azure SQL Database)

## Relationships
* Customer / Broker -> Web App Portal: Accesses portal to submit claims [HTTPS]
* Claims Adjuster -> Web App Portal: Accesses portal for claim workflows [HTTPS]
* Web App Portal -> Claims API Gateway / BFF: Communicates with backend APIs [HTTPS/REST]
* Claims API Gateway / BFF -> Core Claims Service: Routes application traffic [gRPC/HTTPS]
* Core Claims Service -> Claims Database: Persists modern claims data [T-SQL]
* Integration & Sync Service -> Legacy Mainframe System: Synchronizes claim states [MQ/Batch]
* Authentication Wrapper -> Active Directory: Authenticates users via SSO [OIDC/OAuth2]

## Technology Stack
* React & Azure App Service: Delivers sub-2s SPA load times independent of backend latency.
* .NET Core & Azure Container Apps: Provides scalable microservices for claims processing.
* Azure API Management & Azure Service Bus: Secures API traffic and enables reliable asynchronous synchronization.
* Azure SQL Database & Azure App Configuration: Stores claim data and manages dynamic claim-type migrations.

## Rationale
This hybrid architecture isolates the modern cloud UI and backend from high mainframe latency and expensive legacy change cycles. It uses feature flags and decoupled services to meet strict performance, security, and one-day fallback requirements.