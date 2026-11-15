## Overview
This architecture establishes a modern hybrid cloud platform to gradually replace a legacy mainframe insurance claims system. It ensures zero data loss, sub-two-second adjuster UI response times, and rapid fallback capabilities.

## Key Elements
- **Adjuster Workspace:** React Single Page Application hosted on Azure App Service
- **Workspace Shell Component & Security Context Component:** React components handling layout, session, and Azure AD / Entra ID SSO via MSAL.js [OIDC/JWT]
- **Claim Interaction Controller & Caching & Synchronization Client:** React/Redux and IndexedDB/Service Worker components managing local state and masking slow backend latencies
- **Conflict Resolution UI Handler & Telemetry & Audit Component:** React components managing concurrent updates and OpenTelemetry metrics
- **API Gateway Client Layer & Feature Flag & Routing Client:** Axios/Fetch communication layer and dynamic routing toggle component
- **Backend Services:** Claims Processing Service (Java / Spring Boot on Azure Container Apps), Claim Routing Service (Azure Service Bus), and Mainframe Integration Adapter (IBM MQ on-premises)
- **Data Stores:** Azure SQL Database, Azure Cosmos DB / Redis, and COBOL/DB2 Mainframe

## Relationships
- **Claims Adjuster -> Adjuster Workspace:** Accesses platform via web browser [HTTPS/TLS]
- **Adjuster Workspace -> API Management Proxy:** Transmits API requests with bearer tokens [HTTPS/JSON via Interceptors]
- **API Management Proxy -> Claims Processing Service:** Routes backend calls [HTTPS/gRPC]
- **Claims Processing Service <-> Claim Routing Service:** Publishes and consumes asynchronous claim events [AMQP]
- **Claims Processing Service <-> Mainframe Integration Adapter:** Exchanges legacy payloads via IBM MQ [MQ Telemetry Transport / TCP]

## Technology Stack
- **Frontend:** React, Redux, MSAL.js, IndexedDB, Service Worker, OpenTelemetry SDK on Azure App Service for responsive client-side operations
- **Backend & Integration:** Java, Spring Boot on Azure Container Apps, Azure Service Bus, IBM MQ for scalable microservices and resilient message queuing
- **Databases:** Azure SQL Database and Azure Cosmos DB/Redis for flexible relational and cached data persistence
- **Security & Infrastructure:** Azure Active Directory (Entra ID), Azure API Management, Azure Static Web Apps, and Hybrid Cloud (Azure West Europe and On-Premises Mainframe)

## Rationale
This hybrid architecture isolates the expensive, slow legacy mainframe while using local client-side caching to meet strict performance requirements. It decouples legacy dependencies, ensuring seamless migration of claim types with minimal risk and high maintainability.