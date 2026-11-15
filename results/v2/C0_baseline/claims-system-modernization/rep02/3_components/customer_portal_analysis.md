## Overview
The system modernizes a 30-year-old regional insurance mainframe platform by introducing a cloud-based hybrid architecture. It ensures seamless online claim processing while maintaining operational stability during a 3-year migration.

## Key Elements
- Customers and Brokers
- Claims Adjusters
- Customer Portal (React / Azure Static Web Apps)
- Adjuster Workspace (Angular / Azure App Service)
- Claims Core Engine (Java / Spring Boot / Azure Container Apps)
- Routing & Integration Service (Azure Functions)
- Azure API Management (Azure API Management)
- Azure SQL Database & Azure Service Bus Topics
- Active Directory / Microsoft Entra ID & Payment Gateway
- Legacy COBOL/DB2 Mainframe

## Relationships
- Customer Portal -> Azure API Management: Routes HTTPS traffic for online claims [HTTPS / TLS 1.3]
- Adjuster Workspace -> Azure API Management: Submits adjuster transactions [HTTPS / TLS 1.3]
- Azure API Management -> Claims Core Engine: Forwards validated API requests [gRPC / HTTPS]
- Claims Core Engine -> Azure SQL Database: Persists modern claim data [TDS / JDBC]
- Claims Core Engine -> Azure Service Bus Topics: Publishes asynchronous domain events [AMQP]
- Routing & Integration Service -> Legacy Mainframe: Synchronizes data with legacy system [MQ / TCP]
- Customer Portal -> Azure App Configuration: Fetches dynamic feature toggles [HTTPS]

## Technology Stack
- Frontend: React and Angular with TypeScript for responsive web applications
- Backend Compute: Java with Spring Boot running on Azure Container Apps for microservices
- Integration & Messaging: Azure Functions and Azure Service Bus Topics for event-driven workflows
- Data & State: Azure SQL Database for relational persistence and Azure App Configuration for feature flags
- Security & Routing: Azure API Management, OAuth 2.0 with PKCE, and Microsoft Entra ID for SSO

## Rationale
This hybrid architecture isolates expensive legacy mainframe dependencies while delivering modern sub-2-second UI performance. It guarantees zero data loss and supports independent claim-type migrations with a one-day rollback capability.