## Overview
This hybrid architecture gradually modernizes a legacy insurance claims platform over three years. It decouples the new cloud-based user experience from the on-premises mainframe system of record.

## Key Elements
* Policyholders and Brokers (External Users)
* Claims Adjusters (Internal Users)
* Modern Claims Platform (Azure App Service / Azure SQL, West Europe)
* Anti-Corruption Layer (Azure Service Bus and Azure API Management)
* Legacy Mainframe (On-premises COBOL/DB2 System of Record)
* Identity Provider (Azure Active Directory / Entra ID)

## Relationships
* Users to Modern Claims Platform: HTTPS (REST/GraphQL) with OIDC/OAuth2 authentication via Azure AD
* Modern Claims Platform to Legacy Mainframe: mTLS (TLS 1.3) over secure hybrid connection via Anti-Corruption Layer
* Modern Claims Platform to Azure Key Vault: Managed Identities for secure credential retrieval

## Technology Stack
* Cloud Platform: Azure App Service and Azure SQL for managed hosting and minimal operational overhead
* Integration & Messaging: Azure Service Bus with dead-letter queues and Azure API Management for the Strangler Fig pattern and 1-day rollbacks
* Security & Auth: Azure AD (Entra ID) with MFA, OAuth2/JWT tokens, and Azure Key Vault for certificate management
* Infrastructure: Terraform or Bicep for Infrastructure as Code across the hybrid environment

## Rationale
The managed Azure services offset the team's low cloud experience while accelerating delivery of high-performance adjuster screens. The Anti-Corruption Layer and API Management insulate the fragile, change-constrained mainframe from cloud updates and guarantee zero data loss.