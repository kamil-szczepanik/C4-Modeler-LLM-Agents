## Overview
The system is a hybrid cloud insurance claims modernization platform designed to gradually replace a 30-year-old mainframe while ensuring continuous legacy operation. It provides modern online claim submission and adjuster workflows via secure web applications.

## Key Elements
- Customers and Brokers
- Claims Adjusters
- Customer Portal and Adjuster Workspace SPAs (React, Azure Static Web Apps)
- Azure API Management (Azure API Management)
- Claims Core Service (.NET 8, Azure Container Apps)
- Mainframe Integration Adapter (.NET 8, Azure Container Apps)
- Azure SQL Database (Azure SQL Database, Entity Framework Core)
- Azure Service Bus (Azure Service Bus)
- Legacy Mainframe (COBOL/DB2)
- Azure Active Directory

## Relationships
- Customers and Brokers -> Customer Portal and Adjuster Workspace SPAs: Submit online claims [HTTPS]
- Claims Adjusters -> Customer Portal and Adjuster Workspace SPAs: Manage and process claims [HTTPS]
- Customer Portal and Adjuster Workspace SPAs -> Azure API Management: Send API requests [HTTPS (REST/JSON)]
- Customer Portal and Adjuster Workspace SPAs -> Azure Active Directory: Authenticate users [OIDC/OAuth2]
- Azure API Management -> Claims Core Service: Route modern claim traffic [HTTPS (REST/JSON)]
- Claims Core Service <-> Azure SQL Database: Store modern claim data [T-SQL / EF Core]
- Claims Core Service -> Azure Service Bus: Publish domain events [AMQP]
- Mainframe Integration Adapter <-> Legacy Mainframe: Exchange batch and sync data [SNA / MQ / File Transfer]

## Technology Stack
- Azure Static Web Apps with React: Minimized operational overhead for team with limited cloud experience
- .NET 8 on Azure Container Apps: Robust, scalable backend microservices framework
- Azure SQL Database: Managed relational storage with Entity Framework Core
- Azure Service Bus: Asynchronous, reliable messaging for decoupled claim processing
- Azure API Management: Centralized security, rate limiting, and routing boundary

## Rationale
This hybrid architecture isolates expensive legacy mainframe interactions while enabling independent, cloud-native migration of claim types. It guarantees system consistency and sub-two-second adjuster UI response times despite legacy latency constraints.