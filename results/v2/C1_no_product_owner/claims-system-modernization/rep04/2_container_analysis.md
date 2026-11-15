## Overview
This system modernizes a regional insurer's 30-year-old mainframe by gradually migrating claim types to a hybrid cloud platform. It ensures business continuity by maintaining the legacy system of record while delivering a modern web experience.

## Key Elements
- Customers and Brokers
- Claims Adjusters
- Insurer's Active Directory / Microsoft Entra ID
- Customer Portal (React SPA on Azure Static Web Apps)
- Adjuster Workspace (React SPA on Azure Static Web Apps)
- Claims API Gateway (Azure API Management)
- Claims BFF (Node.js/Express on Azure App Service)
- Claims Core Service (Java/Spring Boot on Azure App Service)
- Mainframe Integration Adapter (Azure App Service Worker)
- Message Broker (Azure Service Bus)
- Database (Azure SQL Database)
- Legacy Mainframe (COBOL/DB2, On-Premises)

## Relationships
- Customer Portal to Claims API Gateway via HTTPS/REST
- Adjuster Workspace to Claims BFF via HTTPS/REST
- Claims API Gateway to Claims BFF and Claims Core Service via HTTPS/OIDC/OAuth2
- Claims BFF and Claims Core Service to Azure SQL Database via TDS/Managed Identities
- Mainframe Integration Adapter to Legacy Mainframe via Site-to-Site VPN/ExpressRoute with mTLS
- Claims Core Service and Mainframe Integration Adapter to Azure Service Bus via AMQP/Managed Identities

## Technology Stack
- Azure App Service: Chosen for compute hosting to minimize operational overhead for a team with limited cloud experience.
- Azure API Management: Provides centralized routing, security enforcement, and token validation.
- Azure Service Bus: Handles reliable, transactional asynchronous messaging between cloud and mainframe to prevent data loss.
- Azure SQL Database: Provides relational storage with AES-256 encryption-at-rest for migrated claim types.
- Azure Static Web Apps: Hosts the React single-page applications for customers and adjusters.

## Rationale
The hybrid architecture balances modern web performance and maintainability with the strict constraint of keeping the legacy mainframe as the system of record. Utilizing managed Azure services reduces cloud operational complexity for an inexperienced team while meeting strict security, consistency, and sub-second UI performance requirements.