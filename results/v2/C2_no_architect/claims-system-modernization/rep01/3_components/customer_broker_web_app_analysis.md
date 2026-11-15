## Overview
[A hybrid cloud insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe while maintaining continuous claims processing.]

## Key Elements
* Customers and Brokers
* Claims Adjusters
* Customer/Broker Web App (Azure Container Apps)
* Claims Adjuster Web App (Azure Container Apps)
* API Gateway (Azure Container Apps)
* Integration/Messaging Container (Azure Service Bus)
* Azure SQL Database
* Azure Blob Storage
* On-Premises COBOL/DB2 Mainframe System of Record
* Azure Active Directory (Entra ID)

## Relationships
* Customers and Brokers -> Customer/Broker Web App: Submits and tracks claims [HTTPS / OpenID Connect / OAuth2]
* Customer/Broker Web App -> Azure Blob Storage: Uploads accident photos [HTTPS / SAS Tokens]
* Customer/Broker Web App -> Azure SQL Database: Persists draft claims [TDS / TLS 1.3]
* Customer/Broker Web App -> API Gateway: Routes requests [mTLS / Azure Entra Managed Identities]
* Customer/Broker Web App -> Integration/Messaging Container: Publishes async messages [Azure Service Bus Protocol]
* Customer/Broker Web App -> Azure Active Directory (Entra ID): Authenticates users [OAuth 2.0 / OIDC]

## Technology Stack
* Azure Container Apps: Hosts web applications and APIs for scalable, stateless deployment with built-in blue/green capabilities.
* Azure SQL Database: Persists draft claims with Transparent Data Encryption (TDE) for security and reliability.
* Azure Blob Storage: Handles direct photo uploads via SAS tokens to prevent container memory exhaustion.
* Azure Service Bus: Manages asynchronous messaging to decouple the modern platform from legacy mainframe latency.
* OpenTelemetry & Application Insights: Provides distributed tracing and Real User Monitoring to bridge observability gaps.

## Rationale
[This hybrid architecture mitigates low cloud experience through managed Azure services while strictly respecting mainframe constraints and transaction consistency. It isolates legacy dependencies to ensure rapid UI responsiveness and compliance with the one-day migration rollback requirement.]