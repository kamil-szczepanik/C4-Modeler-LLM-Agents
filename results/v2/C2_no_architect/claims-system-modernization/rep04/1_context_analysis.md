## Overview
[The system is a hybrid insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure-hosted application while ensuring zero data loss and maintaining the legacy system of record.]

## Key Elements
* End Customers & Brokers (Users submitting claims online)
* Claims Adjusters (Users managing claims via the new web application)
* Operations & Finance Teams (Users monitoring regulatory compliance and consistency)
* Azure App Service (Hosting the modern claims web application and APIs)
* Azure SQL Database (Storing migrated claim types and operational data)
* Azure App Configuration (Managing feature flags for the 1-day fallback requirement)
* Azure Key Vault (Securing credentials, secrets, and customer-managed keys)
* Azure API Gateway (Validating and rate-limiting traffic to protect legacy interfaces)
* Azure Application Insights (Providing end-to-end distributed tracing across the hybrid boundary)
* On-Premises COBOL/DB2 Mainframe (System of record during the 3-year migration)

## Relationships
* End Customers & Brokers interact with Azure App Service via HTTPS/TLS 1.3 for online claim submission (R-01)
* Claims Adjusters interact with Azure App Service via HTTPS/TLS 1.3 for claim handling (R-02)
* Azure App Service communicates with Azure SQL Database via TCP/TLS for transactional data storage
* Azure App Service connects to the On-Premises COBOL/DB2 Mainframe via mTLS over a hybrid VPN/ExpressRoute for legacy claim processing
* Azure API Gateway intercepts and secures integration traffic routed to the On-Premises Mainframe interface
* Azure App Service authenticates users against Azure AD (Entra ID) using OpenID Connect (OIDC) (R-07)

## Technology Stack
* Microsoft Azure Platform (Managed PaaS selected to mitigate low team cloud experience)
* Azure App Service & Azure SQL Database (Managed hosting and relational storage to minimize operational overhead)
* Azure App Configuration & Feature Flags (Enables instant claim-type traffic toggling for the 1-day rollback requirement)
* Azure Key Vault & Managed Identities (Eliminates static credentials and secures cross-service authentication)
* Azure Application Insights (Provides distributed tracing to isolate hybrid performance bottlenecks)
* OpenID Connect (OIDC) & Azure AD / Entra ID (Secures single sign-on and multi-factor authentication)
* mTLS and API Gateway (Secures data in transit and protects the legacy mainframe interface)

## Rationale
[This hybrid architecture mitigates risk by keeping the 30-year-old mainframe as the system of record while incrementally migrating claim types to a managed Azure PaaS environment. It leverages managed services and feature flags to bridge the team's cloud skill gap, guarantee strict performance and consistency constraints, and enable rapid 1-day rollbacks if needed.]