## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a cloud-native hybrid platform. It ensures continuous claims processing, zero data loss, and sub-two-second adjuster response times during the transition.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Azure API Management (BFF)
- Claims Portal (React on Azure App Service)
- Claims Modernization Core (Java Spring Boot on Azure Kubernetes Service)
- Integration & Sync Engine (Azure Service Bus)
- State Store (Azure SQL Database Managed Instance)
- Legacy Mainframe System (COBOL/DB2 on-premises)
- Active Directory / Azure AD

## Relationships
- Customers, Brokers, and Adjusters interact with Claims Portal via HTTPS / TLS 1.3
- Claims Portal routes requests through Azure API Management using OAuth 2.0 / OpenID Connect
- Claims Modernization Core communicates with Azure SQL Database via TDS over TLS
- Claims Modernization Core exchanges asynchronous messages with Legacy Mainframe via Azure Service Bus and IPsec VPN / ExpressRoute
- Hybrid boundary protected by mutual TLS (mTLS)

## Technology Stack
- Azure App Service & React: Hosts web frontend ensuring <2s page load performance
- Azure Kubernetes Service (AKS): Runs Java Spring Boot microservices for elastic scalability and blue/green deployments
- Azure Service Bus: Manages asynchronous message queuing to decouple modern services from mainframe batch windows
- Azure SQL Database Managed Instance: Provides transactional persistence and point-in-time recovery for rapid rollbacks
- Azure Active Directory & OAuth 2.0: Delivers centralized single sign-on (SSO) and role-based access control

## Rationale
The hybrid architecture respects the strict 3-year mainframe retention rule and expensive interface constraints by utilizing an incremental strangler fig pattern. Managed Azure services reduce operational overhead for a cloud-inexperienced team while guaranteeing security, data consistency, and rapid fallback capabilities.