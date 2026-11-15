## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native architecture. Its core purpose is to enable online claims submission and fast adjuster workflows while maintaining seamless integration with the legacy system of record.

## Key Elements
- **Users**: Customers, Brokers, Claims Adjusters
- **Containers**: Customer Portal (Azure App Service / React), Adjuster Workspace (Azure App Service / React + Node.js BFF), API Gateway, Integration / ACL Service (Azure Container Apps / .NET)
- **Data & Messaging**: Claims Read/Write Database (Azure Database for PostgreSQL), Azure Service Bus
- **External Systems**: COBOL/DB2 Mainframe, Corporate Active Directory

## Relationships
- Customers & Brokers interact with Customer Portal via HTTPS/REST
- Claims Adjusters interact with Adjuster Workspace via HTTPS/REST
- API Gateway routes traffic to Customer Portal, Adjuster Workspace, and ACL Service via HTTPS
- ACL Service communicates with COBOL/DB2 Mainframe via mTLS over IPsec VPN / Azure ExpressRoute
- Containers connect to PostgreSQL and Azure Service Bus using Azure Managed Identities

## Technology Stack
- Azure App Service (PaaS): Lowers operational burden for cloud-inexperienced team
- Azure Container Apps: Balances microservices flexibility for Integration/ACL Service
- Azure Database for PostgreSQL: Provides local caching to achieve <2s adjuster screen loads
- Azure Service Bus: Orchestrates reliable asynchronous messaging for zero-loss consistency
- Azure Active Directory: Enables centralized single sign-on (SSO)

## Rationale
This hybrid architecture isolates the modern cloud UI from mainframe latency while respecting rigid operational constraints and batch windows. It enables incremental, claim-type-by-claim-type migration with a rapid fallback path.