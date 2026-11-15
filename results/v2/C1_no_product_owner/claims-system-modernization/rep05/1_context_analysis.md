## Overview
The Insurance Claims Modernization system gradually replaces a legacy 30-year-old mainframe claims platform with a modern, cloud-native hybrid architecture. It enables online claim submissions and adjuster workflows while maintaining seamless integration with the on-premise system of record.

## Key Elements
* **Users:** Customers, Brokers, and Claims Adjusters
* **Cloud Platform:** Modern Claims Platform hosted in Azure West Europe
* **Integration Gateway:** Azure API Management (APAM)
* **On-Premise Systems:** Legacy Mainframe (COBOL/DB2) and Active Directory
* **Security & Governance:** Azure Key Vault, Azure Monitor, and Azure Sentinel

## Relationships
* **Customers/Brokers -> Modern Claims Platform:** HTTPS for online claim submission
* **Claims Adjusters -> Modern Claims Platform:** HTTPS for claims handling workflows
* **Modern Claims Platform -> Active Directory:** OIDC/SAML over HTTPS for Single Sign-On (SSO) and MFA
* **Modern Claims Platform <-> Legacy Mainframe:** Asynchronous messaging/ETL routed via Azure API Management over secure VPN/ExpressRoute with mTLS encryption

## Technology Stack
* **Cloud Provider:** Hybrid deployment utilizing Azure West Europe and on-premise infrastructure
* **Integration Layer:** Azure API Management for protocol translation, circuit-breaking during batch windows, and decoupling legacy interfaces
* **Infrastructure-as-Code:** Azure Bicep/Terraform to support teams with low cloud experience
* **Security & Observability:** Azure Key Vault for secrets management, Azure App Insights for distributed tracing, and Azure Monitor/Sentinel for auditing

## Rationale
This hybrid architecture isolates expensive mainframe changes and respects strict batch windows while delivering a performant, cloud-native experience for adjusters. Managed Azure services and automated infrastructure reduce operational risk for a team with limited cloud expertise.