## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure platform while ensuring continuous legacy claims processing. It uses a hybrid architecture with an Anti-Corruption Layer to safely migrate claim types incrementally.

## Key Elements
- Customer/Broker
- Claims Adjuster
- Insurer's Active Directory
- Legacy Mainframe (COBOL/DB2, On-Premises)
- API Gateway (Azure API Management)
- Customer Portal (Azure App Service - React/Node.js)
- Adjuster Workspace (Azure App Service - React/.NET Core API)
- Claims Anti-Corruption Layer / Core Domain Service (Azure Container Apps - .NET Core)
  - Claim Domain Model Component (.NET Core / C#)
  - ACL Translator Component (.NET Core / C#)
  - Mainframe Adapter Component (.NET Core / C#)
  - Repository Component (EF Core)
  - Outbox Pattern Component (EF Core)
- Integration & Sync Engine (Azure Service Bus + Azure Functions)
- Azure SQL Database

## Relationships
- Customer/Broker -> API Gateway: Submits online claims [HTTPS]
- Claims Adjuster -> API Gateway: Handles claims via web application [HTTPS]
- Customer Portal -> Claims Anti-Corruption Layer / Core Domain Service: Sends claim data [HTTPS]
- Adjuster Workspace -> Claims Anti-Corruption Layer / Core Domain Service: Sends and retrieves claim data [HTTPS]
- Claims Anti-Corruption Layer / Core Domain Service -> Integration & Sync Engine: Publishes messages [AMQP / Azure Service Bus]
- Integration & Sync Engine -> Legacy Mainframe: Synchronizes data [Batch / File Transfer]
- Applications -> Insurer's Active Directory: Authenticates users [OIDC / OAuth2 via Azure AD]

## Technology Stack
- Azure Container Apps (.NET Core / C#): Hosts the core domain service and ACL using hexagonal architecture for team maintainability.
- Azure Service Bus & Azure Functions: Manages asynchronous integration and synchronization messages with AMQP.
- EF Core & Azure SQL Database: Provides relational persistence and implements the Outbox Pattern for consistency.
- Polly: Handles resilient retries for mainframe latency up to 5 seconds.
- React / Node.js / .NET Core: Powers modern web interfaces.

## Rationale
This architecture fits requirements by isolating volatile legacy dependencies behind an Anti-Corruption Layer and Outbox pattern, guaranteeing zero data loss (R-04) and rapid fallback capabilities (R-06). It decouples modern sub-2-second adjuster screens (R-05) from slow mainframe responses while respecting strict budget constraints on legacy interface modifications.