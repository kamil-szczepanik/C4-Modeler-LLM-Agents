## Overview
This system modernizes a 30-year-old regional insurer mainframe claims platform by migrating claim types incrementally to Azure while maintaining business continuity. The architecture uses a hybrid cloud approach to safely bridge legacy infrastructure with modern cloud services over a 3-year migration window.

## Key Elements
- End Customers & Brokers
- Claims Adjusters
- API Gateway (Azure API Management / NGINX)
- Customer Portal (React / Node.js)
- Adjuster Workspace (React / .NET Core API)
- Integration & Anti-Corruption Layer (.NET Core / MassTransit)
- Configuration & Feature Store (Azure App Configuration)
- Legacy Mainframe (COBOL/DB2)
- Corporate Active Directory

## Relationships
- Customers & Brokers to Customer Portal via HTTPS/TLS 1.3
- Adjusters to Adjuster Workspace via HTTPS/TLS 1.3
- Services to Configuration & Feature Store via HTTPS with Azure Managed Identities
- Integration & Anti-Corruption Layer to Legacy Mainframe via IBM MQ / TCP
- Users to Corporate Active Directory via OpenID Connect / OAuth 2.0 (SSO)

## Technology Stack
- **Cloud Platform:** Microsoft Azure (West Europe region) for minimal operational overhead
- **Compute & Integration:** .NET Core and MassTransit for reliable message handling
- **Frontend:** React for responsive user interfaces
- **Configuration & State:** Azure App Configuration with native SDK caching and jittered polling
- **Security:** Azure Active Directory for Single Sign-On and Azure RBAC for access control

## Rationale
The hybrid architecture allows incremental migration of claim types while keeping the mainframe as the system of record. Azure App Configuration and local SDK caching ensure sub-millisecond flag evaluations to protect performance SLAs without adding operational complexity for a cloud-inexperienced team.