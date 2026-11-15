## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a cloud-native Azure platform while maintaining uninterrupted claims processing. It provides modern interfaces for online claim submissions and adjuster workflows while keeping the mainframe as the system of record.

## Key Elements
- Claims Adjusters & Support Agents (Primary users)
- Customers & Brokers (External users)
- Legacy Mainframe (On-premises COBOL/DB2 system of record)
- Adjuster Workspace (Angular SPA hosted on Azure App Service)
- Azure API Management (API gateway)
- Claims Core Engine (Java / Spring Boot on Azure Container Apps)
- Azure SQL Database (Read-optimized data store)
- Azure Blob Storage (Document storage with private endpoints)
- Microsoft Entra ID (Identity provider)

## Relationships
- Adjuster Workspace -> Azure API Management: Routes all reads, commands, and document previews via REST/HTTPS (TLS 1.3)
- Azure API Management -> Claims Core Engine: Dispatches asynchronous business commands via Azure Service Bus Topics
- Adjuster Workspace -> Microsoft Entra ID: Authenticates users via OIDC with Authorization Code Flow + PKCE
- Claims Core Engine -> Legacy Mainframe: Synchronizes data via scheduled batch jobs

## Technology Stack
- Frontend: Angular hosted on Azure App Service for responsive UI rendering
- Backend Compute: Azure Container Apps with Java / Spring Boot for scalable microservices
- Database: Azure SQL Database for sub-2s read models and transactional data
- Integration & Messaging: Azure Service Bus Topics for asynchronous event-driven decoupling
- Security: Microsoft Entra ID for Single Sign-On and RBAC enforcement

## Rationale
This hybrid architecture isolates expensive mainframe changes behind a modern Azure integration layer, ensuring seamless migration of claim types. Localized read models and managed PaaS services guarantee high performance (<2s load times) despite team cloud-inexperience and legacy latency constraints.