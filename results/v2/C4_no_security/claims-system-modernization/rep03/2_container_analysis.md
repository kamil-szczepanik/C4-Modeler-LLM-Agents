## Overview
This system modernizes a regional insurer's legacy COBOL/DB2 mainframe claims platform by introducing a hybrid cloud architecture. It gradually migrates claim types over three years while ensuring continuous legacy processing and zero data loss.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Customer & Broker Portal (React SPA)
- Adjuster Web Application (React SPA)
- API Gateway / Backend-for-Fronend (Node.js/NestJS)
- Claims Core Processing Service (.NET Core / C# on Azure App Service)
- Mainframe Integration Adapter (Azure Functions / App Service)
- Azure Service Bus (Messaging & DLQ)
- Azure SQL Database
- Legacy Mainframe (COBOL/DB2 System of Record)
- Insurer's Active Directory / Azure AD

## Relationships
- Customers & Brokers interact with Customer & Broker Portal via HTTPS/JSON
- Claims Adjusters interact with Adjuster Web Application via HTTPS/JSON
- Portals communicate with API Gateway / BFF via HTTPS/REST
- API Gateway communicates with Claims Core Processing Service and Mainframe Integration Adapter via gRPC/HTTPS
- Claims Core Processing Service publishes and consumes messages via Azure Service Bus using AMQP
- Mainframe Integration Adapter communicates with Legacy Mainframe using legacy protocols (MQ/CICS) respecting the 23:00-05:00 batch window pause
- Services authenticate against Azure Active Directory using OAuth2/OpenID Connect

## Technology Stack
- Frontend: React hosted on Azure Static Web Apps
- Backend & BFF: Node.js/NestJS and .NET Core / C#
- Compute & Hosting: Azure App Service and Azure Functions (Managed PaaS)
- Database: Azure SQL Database
- Messaging: Azure Service Bus with Dead-Letter Queues (DLQ)
- Identity & Security: Azure Active Directory via OAuth2/OpenID Connect
- Infrastructure as Code: Terraform / Bicep

## Rationale
The hybrid PaaS architecture minimizes cloud complexity for an inexperienced team while decoupling the UI from slow mainframe responses to meet performance goals. Standardizing on Azure Service Bus and managed Azure services ensures reliable event handling, strict batch-window isolation, and a smooth three-year migration path.