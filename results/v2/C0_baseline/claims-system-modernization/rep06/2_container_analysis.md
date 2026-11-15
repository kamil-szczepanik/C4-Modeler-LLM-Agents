## Overview
[System: Hybrid Insurance Claims Modernization Platform]
[Core Purpose: Gradually replaces a legacy mainframe claims system while maintaining parallel operations and compliance over a 3-year migration window.]

## Key Elements
- Users: Customer, Broker, Claims Adjuster, Business Operations / Migration Manager
- External Systems: On-premise COBOL/DB2 Legacy Mainframe
- Cloud Infrastructure: Azure West Europe (VNet with Private Endpoints)
- Gateways & Routing: Azure API Management
- Compute Containers: Azure Container Apps (Java / Spring Boot for Claims Processing Service, React / Node.js for Migration Dashboard)
- Integration & Messaging: Azure Service Bus, Azure Logic Apps / Functions
- Data & Storage: Azure SQL Database
- Security & Observability: Azure Key Vault, Azure Active Directory (Entra ID), Azure Application Insights

## Relationships
- Customer / Broker -> Azure API Management: Online claim submission via HTTPS / REST
- Claims Adjuster / Migration Manager -> Azure API Management: Web application access via HTTPS / OAuth 2.0 (OpenID Connect)
- Azure API Management -> Azure Container Apps: Dynamic claim-type routing via internal VNet
- Azure Container Apps -> Azure SQL Database: ACID-compliant transaction persistence via TDS
- Azure Container Apps -> Azure Service Bus: Asynchronous event publishing and queuing
- Azure Service Bus -> On-premise COBOL/DB2 Legacy Mainframe: Hybrid integration bridge via TLS 1.3 / mTLS and Site-to-Site VPN / ExpressRoute
- Azure Container Apps -> Azure Key Vault: Managed Identity secret retrieval

## Technology Stack
- Azure API Management: Selected for dynamic feature-flag routing to guarantee R-06 one-day rollbacks per claim type without mainframe changes
- Java / Spring Boot on Azure Container Apps: Chosen for enterprise maturity to support teams with low cloud experience
- Azure SQL Database: Mandated for ACID compliance to satisfy R-04 (no lost or double-processed claims)
- Azure Service Bus & Logic Apps: Utilized for asynchronous queueing around the strict nightly batch window (23:00-05:00)
- Azure Active Directory (Entra ID): Implements SSO for R-07 security compliance
- Terraform / Bicep: Mandated as Infrastructure as Code for repeatable hybrid deployments

## Rationale
[This hybrid architecture decouples modern cloud workloads from the legacy mainframe via API Management and asynchronous messaging, satisfying strict constraints like batch windows and limited cloud experience.]
[It ensures zero data loss and rapid rollbacks through isolated domain services, robust ACID storage, and secure VNet connectivity.]