## Overview
The system is a hybrid insurance claims modernization platform that gradually migrates claim types from a legacy COBOL/DB2 mainframe to a modern Azure cloud environment. Its core purpose is to maintain continuous claims processing while delivering a fast, secure web application for users over a 3-year transition.

## Key Elements
* **People:** Policyholders (customers), Insurance Brokers, Claims Adjusters, Operations Managers.
* **Systems:** COBOL/DB2 Mainframe (System of Record), On-Premise Active Directory / Entra ID.
* **Azure Containers:** Azure API Gateway / WAF, Azure App Service (Web Application), Managed Redis Cache, Azure SQL Database.
* **Integration Components:** Azure Application Insights, Azure Key Vault.

## Relationships
* Policyholders & Brokers interact with Azure API Gateway via HTTPS/TLS 1.3 for online claim submission (R-01).
* Claims Adjusters & Operations Managers authenticate via OpenID Connect/OAuth 2.0 (Azure Active Directory / Entra ID) and access the Azure App Service via HTTPS.
* Azure App Service communicates with Managed Redis Cache and Azure SQL Database for fast data retrieval (<2s load times per R-05).
* Azure App Service connects to the on-premise COBOL/DB2 Mainframe via mTLS and TLS 1.3 for hybrid claim synchronization, respecting the 23:00-05:00 batch window.

## Technology Stack
* **Cloud Platform:** Azure West Europe (Hybrid deployment model with on-premise mainframe).
* **Compute & Frontend:** Azure App Service (Managed PaaS to mitigate team's low cloud experience).
* **Data & Caching:** Managed Redis Cache & Azure SQL Database (Enables CQRS/async patterns for <2s UI performance).
* **Security & Auth:** Azure API Gateway / WAF, Azure Active Directory / Entra ID, Azure Key Vault (OAuth 2.0, RBAC, mTLS, AES-256).
* **Observability:** Azure Application Insights & OpenTelemetry (Distributed tracing and hybrid error tracking).

## Rationale
This hybrid architecture isolates the expensive-to-change COBOL/DB2 mainframe behind a secure Azure integration layer, ensuring zero lost claims and a 1-day rollback capability per claim type. Utilizing managed Azure PaaS minimizes operational overhead for a team with limited cloud experience while meeting strict security, SSO, and performance constraints.