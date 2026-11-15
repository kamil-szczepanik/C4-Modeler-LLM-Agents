## Overview
[The system modernizes a regional insurer's legacy COBOL/DB2 mainframe claims platform using a hybrid cloud architecture. Its core purpose is to incrementally migrate claim types to a cloud-native platform while ensuring continuous business operations.]

## Key Elements
* Web Frontend (React/TypeScript on Azure Static Web Apps)
* Auth Component (TypeScript / MSAL.js)
* Customer Portal UI (React)
* Adjuster Workspace UI (React)
* Migration Feature Flag Adapter (TypeScript)
* API Gateway / Backend-for-Frontend (BFF) (Azure Container Apps (Node.js/Go))
* Core Claims Service (Azure Container Apps (Java/Spring Boot or .NET))
* Data Sync Engine (Azure Service Bus & Azure Functions)
* Azure SQL Database (Azure SQL Database)
* Legacy Mainframe System (COBOL/DB2)
* Enterprise Identity Provider (Active Directory / Entra ID)

## Relationships
* Customers and Brokers -> Web Frontend [HTTPS/TLS (REST/GraphQL)]
* Claims Adjusters -> Web Frontend [HTTPS/TLS (REST/GraphQL)]
* Web Frontend -> API Gateway / Backend-for-Frontend (BFF) [HTTPS/TLS (REST/GraphQL)]
* Web Frontend -> Enterprise Identity Provider [OpenID Connect (OIDC)]
* API Gateway / Backend-for-Frontend (BFF) -> Core Claims Service [HTTPS/TLS (gRPC/REST)]
* Core Claims Service -> Azure SQL Database [TDS with encryption]
* Data Sync Engine -> Legacy Mainframe System [Encrypted TCP/MQ with mTLS via Enterprise Service Bus]

## Technology Stack
* Azure Static Web Apps: Hosts the React/TypeScript frontend with global CDN distribution.
* Azure Container Apps: Runs the BFF and Core Claims Services using Node.js/Go and Java/.NET for scalable microservices.
* Azure SQL Database: Provides cloud data storage with Transparent Data Encryption (TDE).
* Azure Service Bus & Azure Functions: Powers reliable messaging and asynchronous data synchronization.
* MSAL.js: Manages OIDC authentication and Single Sign-On session tokens.

## Rationale
[This hybrid architecture isolates expensive mainframe changes while delivering high-performance cloud UI experiences under strict latency targets. It guarantees incremental migration with rapid fallback capabilities and robust security controls.]