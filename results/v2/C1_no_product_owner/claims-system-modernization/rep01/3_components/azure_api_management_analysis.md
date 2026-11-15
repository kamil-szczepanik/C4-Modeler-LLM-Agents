## Overview
[System: Hybrid Insurance Claims Modernization Platform]
[Core Purpose: Gradually replaces a legacy COBOL/DB2 mainframe claims system with a modern Azure-hosted platform while maintaining continuous processing and strict hybrid data consistency.]

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Claims Portal (React on Azure App Service)
- Azure API Management (Azure API Management (BFF))
- Claims Modernization Core (Java Spring Boot on Azure Kubernetes Service)
- Integration & Sync Engine (Azure Service Bus)
- State Store (Azure SQL Database Managed Instance)
- Legacy Mainframe System (COBOL/DB2, on-premise)
- Active Directory

## Relationships
- Claims Portal -> Azure App Gateway: HTTPS (TLS 1.3)
- Azure App Gateway -> Azure API Management: HTTPS (TLS 1.3)
- Azure API Management -> Claims Modernization Core: HTTPS with mTLS
- Azure API Management -> Legacy Mainframe System: HTTPS with mTLS
- Claims Portal -> Azure API Management: Routes requests using OAuth 2.0 / OpenID Connect

## Technology Stack
- Azure API Management: Acts as BFF and security gateway, using native XML policy fragments to avoid custom code and reduce operational overhead.
- Azure Kubernetes Service & Java Spring Boot: Hosts the Claims Modernization Core for modern microservices execution.
- Azure App Service & React: Hosts the Claims Portal web application for users.
- Azure Service Bus: Manages asynchronous messaging for the Integration & Sync Engine.
- Azure SQL Database Managed Instance: Acts as the state store for modern claims data.
- Bicep/Terraform & APIOps: Manages Infrastructure-as-Code and APIM configurations via CI/CD pipelines.

## Rationale
[This hybrid architecture isolates the expensive-to-change COBOL/DB2 mainframe behind a managed API gateway and microservices layer, fulfilling the 3-year migration constraint.]
[It leverages managed cloud services and declarative policies to accommodate a team with limited cloud experience while ensuring sub-2-second performance and high security.]