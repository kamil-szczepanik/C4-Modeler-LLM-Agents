## Overview
[The system is an Insurance Claims Modernization platform built as a hybrid cloud solution to gradually replace a legacy COBOL/DB2 mainframe system. Its core purpose is to enable online claim submission and adjuster workflows while maintaining synchronization with the legacy system of record.]

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Active Directory
- Legacy Mainframe System
- Claims Portal (React on Azure App Service)
- Azure API Management (BFF)
- Claims Modernization Core (Java Spring Boot on Azure Kubernetes Service)
- Integration & Sync Engine (Azure Service Bus)
- State Store (Azure SQL Database Managed Instance)

## Relationships
- Customers & Brokers -> Claims Portal: HTTPS / TLS 1.3
- Claims Adjusters -> Claims Portal: HTTPS / TLS 1.3
- Claims Portal -> Azure API Management: OAuth 2.0 / OpenID Connect
- Claims Portal -> Active Directory: OAuth 2.0 / OpenID Connect

## Technology Stack
- React on Azure App Service: Ensures responsive frontend performance and sub-2-second load times
- Java Spring Boot on Azure Kubernetes Service: Provides scalable backend processing for migrated claim types
- Azure Service Bus: Handles reliable asynchronous messaging and integration sync
- Azure SQL Database Managed Instance: Acts as the state store for modern claim records
- Azure API Management: Manages secure API routing and acts as a backend-for-frontend layer

## Rationale
- This hybrid architecture isolates expensive mainframe dependencies while delivering modern cloud capabilities to users. The phased approach guarantees system consistency, security via Active Directory, and meet performance targets despite limited cloud experience.