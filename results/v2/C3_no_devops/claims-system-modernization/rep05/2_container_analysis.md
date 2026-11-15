## Overview
[The system modernizes a 30-year-old regional insurance mainframe by gradually migrating claim types to a hybrid cloud platform. It ensures continuous legacy operation, zero data loss, and sub-2-second adjuster response times during the 3-year transition.]

## Key Elements
- Users: Customers, Brokers, Claims Adjusters, Migration Operations Managers
- Frontend Containers: Web Application (React/Next.js on Azure App Service), Operations BFF & Admin Portal (.NET Core / React)
- Backend Containers: Claims API Gateway / Backend-for-Frontend (.NET Core on Azure Container Apps), Claims Processing Service (.NET Core Web API), Anti-Corruption Layer (ACL on Azure Container Apps / On-Prem VM)
- Integration & Storage: Azure Service Bus / Apache Kafka, Azure SQL Database
- External Systems: COBOL/DB2 Legacy Mainframe, Azure Active Directory, Payment Gateway, Notification Service

## Relationships
- Customers/Brokers/Adjusters to Web Application via HTTPS/TLS 1.3 (OIDC/OAuth2 SSO via Azure AD)
- Web Application & Admin Portal to BFFs via HTTPS REST/GraphQL
- BFFs to Claims Processing Service via gRPC with mTLS
- Claims Processing Service to Azure SQL Database via TDS/SQL over TLS 1.3
- Claims Processing Service to ACL and Azure Service Bus via AMQP/Kafka Protocol
- ACL to Legacy Mainframe via IBM MQ / TCP over ExpressRoute/VPN hybrid link with mTLS

## Technology Stack
- Azure App Service: Hosts React/Next.js frontend for sub-2-second user load times
- Azure Container Apps: Hosts .NET Core BFFs, Claims Processing Service, and ACL with managed scaling
- Azure SQL Database: Provides relational storage for migrated claim types ensuring rapid rollback capability
- Azure Service Bus / Apache Kafka: Manages asynchronous event streams ensuring zero data loss across hybrid boundaries
- Azure Key Vault & Managed Identities: Secures credentials and secrets without hardcoding
- Azure Active Directory: Enforces SSO, RBAC, and JIT privileged access

## Rationale
- The hybrid cloud architecture with an Anti-Corruption Layer decouples the modern Azure platform from the legacy mainframe while respecting expensive mainframe change constraints. CQRS and BFF patterns isolate slow mainframe responses to guarantee required adjuster performance.