## Overview
The Insurance Claims Modernization system gradually replaces a legacy mainframe with a hybrid cloud platform. It enables online claim submission and adjuster processing while maintaining data consistency across systems.

## Key Elements
* Customer / Broker (Person)
* Claims Adjuster (Person)
* Insurer's Active Directory (External System)
* Legacy Mainframe COBOL/DB2 (External System)
* API Gateway (Azure API Management)
* Customer Portal (Azure App Service - React/Node.js)
* Adjuster Workspace (Azure App Service - React/.NET Core API)
* Claims Anti-Corruption Layer / Core Domain Service (Azure Container Apps - .NET Core)
* Integration & Sync Engine (Azure Service Bus + Azure Functions)

## Relationships
* Customer/Broker -> HTTPS -> API Gateway
* Claims Adjuster -> HTTPS -> API Gateway
* API Gateway -> HTTPS -> Customer Portal
* API Gateway -> HTTPS -> Adjuster Workspace
* Customer Portal & Adjuster Workspace -> HTTPS -> Claims Anti-Corruption Layer
* Claims Anti-Corruption Layer -> AMQP / Azure Service Bus -> Integration & Sync Engine
* API Gateway -> OAuth2 / OpenID Connect -> Insurer's Active Directory
* Integration & Sync Engine -> Batch/File Transfer -> Legacy Mainframe

## Technology Stack
* Hybrid Cloud Deployment: Azure West Europe and On-Premises Mainframe (fits regional infrastructure and data residency).
* Azure API Management: Single HTTPS entry point for security, rate limiting, and SSO.
* Azure App Service: Hosts React and .NET Core frontends for rapid delivery given low cloud expertise.
* Azure Container Apps (.NET Core): Runs the Anti-Corruption Layer with manageable abstractions over raw Kubernetes.
* Azure Service Bus & Azure Functions: Provides reliable AMQP messaging for zero claim loss and data synchronization.

## Rationale
This hybrid architecture isolates the fragile, expensive-to-change mainframe while modernizing the user experience in Azure. Asynchronous messaging and CQRS patterns successfully decouple high-performance user interfaces from slow legacy response times.