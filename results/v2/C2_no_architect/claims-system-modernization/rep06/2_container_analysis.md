## Overview
[System: Hybrid Insurance Claims Modernization Platform]
[Core Purpose: Gradually replaces a 30-year-old mainframe claims system with a modern Azure cloud platform while maintaining legacy processing for 3 years.]

## Key Elements
* Policyholders and Insurance Brokers (External users submitting claims)
* Claims Adjusters (Internal users handling claims via web app)
* Operations Managers / Migration Leads (Users monitoring claim migration and rollbacks)
* Azure Portal & API Gateway (Web Application Firewall, ingress routing)
* Azure Container Apps / App Service (Hosting adjuster and portal containers)
* Azure SQL Database (Modern platform database with automated snapshots)
* COBOL/DB2 Mainframe (On-premise legacy system of record)
* Azure Active Directory / Entra ID (Identity and Access Management)

## Relationships
* Policyholders/Brokers -> Azure API Gateway via HTTPS (TLS 1.3) for online claim submission (R-01)
* Claims Adjusters -> Azure Web App via HTTPS / OAuth 2.0 / OIDC for claim management (R-02, R-07)
* Azure Containers -> COBOL/DB2 Mainframe via hybrid VPN / mTLS for legacy claim fallback (R-03, R-06)
* Azure API Gateway -> Azure SQL Database via TLS for data persistence
* Azure Application Insights -> Azure Containers via HTTPS for distributed tracing
* Azure Key Vault -> Azure Containers via Managed Identities for secret management

## Technology Stack
* Cloud Provider: Azure (West Europe region) & On-Premise Hybrid
* Compute/Containers: Azure Container Apps / App Service (chosen for simplicity for cloud-inexperienced team)
* Database: Azure SQL Database (enables automated snapshots for 1-day rollbacks)
* Security/Identity: Azure AD / Entra ID with OAuth 2.0 / OIDC and RBAC
* Infrastructure as Code: Terraform or Bicep templates for environment standardization
* Observability: Azure Application Insights with PII masking for distributed tracing
* Perimeter Defense: Azure Web Application Firewall (WAF) and mTLS via hybrid VPN

## Rationale
[This hybrid architecture isolates complex cloud mechanics to Azure while honoring the 3-year mainframe lifespan constraint.]
[It provides strict latency shielding, automated batch-window safeguards, and modular IaC to guarantee seamless 1-day rollbacks for cloud-inexperienced teams.]