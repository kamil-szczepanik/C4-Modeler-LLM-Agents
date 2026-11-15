## Overview
- Modernizes a 30-year-old regional insurer mainframe claims system through a gradual hybrid cloud migration.
- Replaces legacy claims processing incrementally while maintaining continuous business operations.

## Key Elements
- End Customers and Brokers
- Claims Adjusters
- Customer Portal (React SPA / Azure Static Web Apps)
- Adjuster Workspace (Node.js/Spring Boot BFF + React)
- Azure API Management (Azure API Management)
- Migration Control & Routing Engine (Azure Functions & Azure Cosmos DB)
- Claims Processing Core (Azure Container Apps)
- Anti-Corruption Layer & Integration (Azure Service Bus & Apache Camel)
- Legacy Mainframe System (COBOL/DB2)
- Azure Active Directory / Identity Provider
- Azure Key Vault
- Azure Monitor & Azure Sentinel

## Relationships
- Customer Portal -> Azure API Management: Consumes services [OAuth 2.0 / OpenID Connect, HTTPS]
- Adjuster Workspace -> Azure API Management: Consumes services [OAuth 2.0 / OpenID Connect, HTTPS]
- Azure API Management -> Migration Control & Routing Engine: Routes claim submissions [REST / HTTPS, mTLS]
- Migration Control & Routing Engine -> Anti-Corruption Layer & Integration: Dispatches messages [Azure Service Bus]
- Anti-Corruption Layer & Integration -> Legacy Mainframe System: Synchronizes records [SNA / Custom Protocol]

## Technology Stack
- Azure API Management: Central gateway for security, routing, and policy enforcement due to low team cloud experience.
- Azure Functions & Cosmos DB: Serverless routing engine for dynamic claim type switching.
- Azure Container Apps: Host for claims processing core and microservices.
- Azure Service Bus & Apache Camel: Asynchronous messaging and integration for hybrid mainframe communication.
- Azure Active Directory: Single sign-on and identity management.
- Azure SQL Ledger: Tamper-evident audit and reconciliation ledger.

## Rationale
- Decouples frontends from internal routing complexity to support seamless, one-day claim type fallbacks to the mainframe.
- Enforces hybrid security, zero-loss consistency, and low-latency adjuster screens via managed Azure PaaS services.