## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native platform. It maintains dual-processing capabilities to ensure zero claim loss while migrating claim types sequentially.

## Key Elements
- End Customers & Brokers
- Claims Adjusters
- Legacy Mainframe (COBOL/DB2)
- Azure API Management / NGINX (API Gateway)
- Customer Portal (React / Node.js)
- Adjuster Workspace (React / .NET Core API)
- Integration & Anti-Corruption Layer (.NET Core / MassTransit)
- Claim Read Model Database (Azure Cosmos DB)
- Corporate Active Directory (Azure AD / Entra ID)

## Relationships
- Customer Portal -> API Gateway: Submits claims [HTTPS/REST]
- Adjuster Workspace -> API Gateway: Routes adjuster traffic [Internal HTTPS]
- Adjuster Workspace -> Claim Read Model Database: Reads claim data [TCP / Cosmos DB Direct Mode]
- Integration & Anti-Corruption Layer -> Legacy Mainframe: Syncs data and routes commands [AMQP / MQ]
- Workspace API Backend -> Corporate Active Directory: Validates Single Sign-On [OIDC / OAuth2 / TLS 1.3]

## Technology Stack
- React & TypeScript: Enables rapid UI state toggling and a platform fallback status banner for R-06.
- .NET Core Web API: Provides enterprise patterns and robust backend orchestration.
- Azure Cosmos DB: Delivers low-latency NoSQL reads to guarantee sub-2s screen loads (R-05).
- MassTransit & RabbitMQ: Manages asynchronous messaging and circuit breakers through the Anti-Corruption Layer.
- Azure Container Apps & Docker: Containerizes independent artifacts for reliable hybrid deployments.

## Rationale
This hybrid architecture decouples modern user experiences from the rigid mainframe, meeting strict performance and fallback requirements. It mitigates team cloud-incurred risks using managed Azure services while preserving system of record consistency.