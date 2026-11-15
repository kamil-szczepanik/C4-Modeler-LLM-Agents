## Overview
[The system is a modern hybrid claims platform replacing a 30-year-old mainframe while ensuring continuity. Its core purpose is providing online claim submission and tracking for customers and brokers via a secure, cloud-hosted portal.]

## Key Elements
* Customer Portal (Azure App Service, React SPA, .NET BFF)
* API Gateway (Azure API Management)
* Claims Read/Write Database (Azure Database for PostgreSQL)
* Corporate Active Directory
* Legacy Mainframe System (COBOL/DB2)

## Relationships
* Customer Portal -> Customer Portal BFF: Forwards UI requests [HTTPS]
* Customer Portal BFF -> API Gateway: Forwards authenticated API requests [HTTPS/REST]
* API Gateway -> Claims Read/Write Database: Reads and writes claim data [Azure Managed Identities]
* Customer Portal BFF -> Corporate Active Directory: Authenticates via SSO [OIDC / SAML]

## Technology Stack
* Azure App Service: Hosts the React SPA and .NET Backend-for-Frontend (BFF) securely in a co-located setup.
* React: Powers the customer-facing SPA with accessibility and local session autosave.
* .NET Minimal API: Implements the BFF pattern to handle secure token management and cookie-based authentication.
* Azure API Management: Secures and routes all traffic, enforcing strict server-side validation.
* Azure Database for PostgreSQL: Stores application data with Azure Managed Identities.

## Rationale
[This architecture decouples the legacy mainframe via a hybrid cloud approach, meeting strict security and performance requirements. The BFF pattern and Azure App Service deployment slots ensure maintainability, rapid rollbacks, and protection against token theft for the inexperienced cloud team.]