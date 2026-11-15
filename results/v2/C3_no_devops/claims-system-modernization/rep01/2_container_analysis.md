## Overview
The system is a hybrid cloud platform that modernizes a regional insurer's 30-year-old mainframe claims system through incremental migration. It ensures zero data loss, sub-2-second adjuster screen loads, and seamless rollback capabilities.

## Key Elements
- **Users**: End Customers, Brokers, Claims Adjusters, Compliance/Audit Officers, Migration Support/Operations Team.
- **External Systems**: Legacy Mainframe (COBOL/DB2), Corporate Active Directory (Entra ID), Enterprise Service Bus (ESB), Audit & Compliance System.
- **Azure Containers**: Web Application Container (React/Node.js on Azure App Service), API Gateway Container (.NET/YARP on Azure Container Apps), Claims Core Domain Service (.NET Core), Read-Model & Caching Store (Azure Cosmos DB/Redis), Integration & Sync Worker (Azure Functions).
- **Data Stores**: Azure SQL Database (Transactional Store), Azure Key Vault.

## Relationships
- **Clients to Web App**: HTTPS/JSON via public internet, authenticated via OpenID Connect / OAuth 2.0.
- **Web App to API Gateway**: HTTPS/JSON with Azure AD token propagation.
- **API Gateway to Core Services**: gRPC/REST within Azure Container Apps using mTLS.
- **Core Services to Data Stores**: TCP/TLS to Azure SQL, Cosmos DB, and Redis.
- **Integration Worker to Legacy Mainframe**: Asynchronous messaging via Azure Service Bus across an IPsec VPN/ExpressRoute via the ESB.

## Technology Stack
- **Azure App Service**: Hosts the React/Node.js Web Application Container for managed scalability.
- **Azure Container Apps (.NET / YARP)**: Powers the API Gateway for dynamic routing, feature flagging, and edge security.
- **.NET Core**: Implements the Claims Core Domain Service business logic.
- **Azure Cosmos DB / Redis**: Provides asynchronous read-models and caching to maintain sub-2s screen loads.
- **Azure SQL Database**: Acts as the modern transactional data store for migrated claims.
- **Azure Service Bus & Azure Functions**: Delivers reliable asynchronous eventing and mainframe data synchronization.
- **Azure Key Vault & Entra ID**: Manages secrets dynamically via managed identities and enforces SSO/RBAC.

## Rationale
The hybrid architecture leverages Azure PaaS to deliver modern web performance while maintaining a secure, strangler-fig integration with the legacy mainframe system of record. Isolated microservices and asynchronous workers guarantee zero data loss, low cloud-experience mitigation, and strict one-day fallback compliance.