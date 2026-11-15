## Overview
The system is the Modern Claims Platform, designed to gradually replace a 30-year-old COBOL/DB2 mainframe claims system via a hybrid architecture. Its core purpose is to enable online claim submissions and modern claims handling while maintaining data consistency and supporting incremental migration.

## Key Elements
- Customers and Brokers
- Claims Adjusters
- Operations and Support Staff
- Finance and Accounting
- Legacy Mainframe System (COBOL/DB2)
- Enterprise Identity Provider (Active Directory / Entra ID)
- Web Frontend (React/TypeScript on Azure Static Web Apps)
- API Gateway / Backend-for-Frontend (BFF) (Azure Container Apps (Node.js/Go))
- Core Claims Service (Azure Container Apps (Java/Spring Boot or .NET))
- Data Sync Engine (Azure Service Bus & Azure Functions)
- Azure SQL Database (Azure SQL Database with Azure SQL Ledger and Change Tracking)

## Relationships
- Customers and Brokers -> Web Frontend (HTTPS/TLS (REST/GraphQL))
- Claims Adjusters -> Web Frontend (HTTPS/TLS (REST/GraphQL))
- Operations and Support Staff -> Web Frontend (HTTPS/TLS (REST/GraphQL))
- Finance and Accounting -> Web Frontend (SFTP / encrypted API feeds)
- Web Frontend -> API Gateway / Backend-for-Frontend (BFF) (HTTPS/TLS (REST/GraphQL))
- Web Frontend -> Enterprise Identity Provider (OpenID Connect (OIDC))
- API Gateway / Backend-for-Frontend (BFF) -> Core Claims Service (HTTPS/TLS (gRPC/REST))
- Core Claims Service -> Azure SQL Database (TDS with TLS 1.2+ via Private Endpoint)
- Data Sync Engine -> Legacy Mainframe System (Encrypted TCP/MQ with mTLS via Enterprise Service Bus)

## Technology Stack
- Azure Static Web Apps with React/TypeScript for responsive frontend delivery
- Azure Container Apps (Node.js/Go) for API Gateway/BFF routing and orchestration
- Azure Container Apps (Java/Spring Boot or .NET) for domain logic execution
- Azure SQL Database with Azure SQL Ledger and Change Tracking for reliable cloud persistence and tamper-evident auditing
- Azure Service Bus and Azure Functions for asynchronous hybrid messaging and data synchronization
- Microsoft Entra ID for Single Sign-On and database authentication via Managed Identities

## Rationale
This architecture uses a hybrid approach with Azure Container Apps and Azure SQL Database to deliver sub-second adjuster screen loads and isolated cloud persistence. It ensures zero data loss and rapid one-day rollback capabilities to the legacy mainframe, mitigating migration risks for teams with limited cloud experience.