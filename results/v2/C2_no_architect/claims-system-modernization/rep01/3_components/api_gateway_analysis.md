## Overview
[The system is an API Gateway implemented on Azure Container Apps that manages, secures, and dynamically routes traffic for an insurance claims modernization platform. Its core purpose is to decouple web applications from backend data stores while facilitating the hybrid migration of claim types between Azure microservices and a legacy on-premises mainframe.]

## Key Elements
- API Gateway (Azure Container Apps)
- Customers and Brokers (External Users)
- Claims Adjusters (Internal Users)
- Azure WAF (Web Application Firewall)
- Azure Active Directory / Entra ID
- Azure SQL Database
- On-Premises COBOL/DB2 Mainframe System of Record
- Azure Service Bus

## Relationships
- Customers / Brokers -> Azure WAF: Sends public API requests [HTTPS / TLS 1.3]
- Azure WAF -> API Gateway: Forwards sanitized HTTP traffic [HTTPS]
- Claims Adjuster Web App -> API Gateway: Routes authenticated requests [mTLS / Azure Entra Managed Identities]
- API Gateway -> Azure SQL: Removed; direct database access is prohibited in favor of domain containers
- API Gateway -> On-Premises COBOL/DB2 Mainframe: Dynamically routes unmigrated claim traffic [HTTPS / VPN / ExpressRoute]
- API Gateway -> Azure Microservices: Dynamically routes migrated claim traffic [gRPC / HTTPS]

## Technology Stack
- Azure Container Apps: Hosts the API Gateway with native traffic-splitting capabilities for canary deployments.
- Azure WAF: Deployed in front of the API Gateway to mitigate OWASP Top 10 threats.
- Azure Active Directory (Entra ID): Provides Single Sign-On (SSO) and JWT-based authentication.
- Azure ExpressRoute / VPN: Secures hybrid networking tunnels to the on-premise mainframe.
- OpenAPI / JSON Schema Validation: Enforced at the gateway layer for payload sanitization.

## Rationale
[This architecture enforces a strict security perimeter and decouples legacy components without violating business constraints. It provides the dynamic routing and circuit-breaking necessary to safely shift claim types to Azure while maintaining a one-day rollback window.]