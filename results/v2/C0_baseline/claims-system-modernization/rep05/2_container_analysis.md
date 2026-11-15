## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid cloud platform while ensuring uninterrupted claims processing. It provides secure online submission for users and high-performance claim handling for adjusters.

## Key Elements
- Policyholder / Broker
- Claims Adjuster
- Legacy Mainframe (COBOL/DB2)
- Azure API Management / Migration Router
- Azure Static Web Apps / React Claims Web App
- Azure Container Apps (Adjuster Backend, Mainframe Integration Adapter)
- Azure App Service & Azure Cosmos DB (Migration Control Service)
- Azure Service Bus & Azure Functions (Integration & Sync Service)
- Azure Key Vault
- Active Directory / Entra ID

## Relationships
- Policyholder / Broker accesses Claims Web App via HTTPS through Azure API Management
- Claims Adjuster interacts with Claims Web App via REST/GraphQL using OAuth 2.0 / OIDC
- Azure API Management dynamically routes traffic to Mainframe Integration Adapter or Azure Container Apps
- Mainframe Integration Adapter connects to Legacy Mainframe via TLS 1.3 with mTLS and IP whitelisting
- Integration & Sync Service communicates asynchronously via Azure Service Bus
- Migration Control Service manages routing rules stored in Azure Cosmos DB

## Technology Stack
- Azure API Management: Single entry point and dynamic claim-type routing
- Azure Container Apps: Scalable hosting for backend microservices and mainframe adapter
- React / Azure Static Web Apps: Modern, responsive frontend for claims adjusters
- Azure Service Bus & Functions: Event-driven asynchronous synchronization
- Azure Cosmos DB: State management and audit reconciliation tracking
- Azure Key Vault & Entra ID: Secure secrets management and OAuth 2.0 / OIDC single sign-on

## Rationale
This hybrid architecture isolates expensive mainframe dependencies while meeting sub-two-second performance goals via asynchronous caching and event-driven patterns. It enables incremental migration and one-day rollbacks per claim type without extending the rigid nightly batch window.