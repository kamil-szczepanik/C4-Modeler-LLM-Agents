## Overview
[The system is a hybrid Insurance Claims Modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern cloud-native architecture. Its core purpose is to enable online claim submission and adjuster management while maintaining zero data loss and compliance during a phased 3-year migration.]

## Key Elements
* Policyholders and Insurance Brokers (External Users)
* Claims Adjusters and Operations Managers (Internal Users)
* COBOL/DB2 Mainframe (System of Record)
* On-Premise Active Directory / Entra ID (Identity Provider)
* Azure API Gateway & WAF (Ingress & Security)
* Azure Container Apps / App Service (Compute Container for Microservices)
* Azure SQL Database (Modern Data Store)
* Azure Application Insights (Observability)
* Azure Key Vault (Secret Management)

## Relationships
* Claims Adjusters -> Azure Container Apps / App Service: Claim management and interaction [HTTPS, OAuth 2.0, OIDC]
* Operations Managers -> Azure Container Apps / App Service: Monitoring migration and rollbacks [HTTPS, OAuth 2.0, OIDC]
* Azure API Gateway & WAF -> Azure Container Apps / App Service: Routed HTTP traffic [HTTPS, TLS 1.3]
* Azure Container Apps / App Service -> COBOL/DB2 Mainframe: Legacy claim processing and fallback [Hybrid VPN, mTLS]
* Azure Application Insights -> Azure Container Apps / App Service: Distributed tracing telemetry [HTTPS]
* Azure Key Vault -> Azure Container Apps / App Service: Secret retrieval [Azure Managed Identities]

## Technology Stack
* Azure Container Apps (ACA): Chosen for managed container orchestration to offset limited team cloud experience while supporting rapid zero-downtime rollbacks.
* Azure API Gateway & WAF: Provides centralized entry, routing, and web application firewall protection.
* Azure Active Directory / Entra ID: Implements single sign-on (SSO) and token validation via OAuth 2.0 and OIDC.
* Azure Managed Identities: Eliminates hardcoded credentials for secure access to Key Vault and SQL.
* KEDA (Kubernetes Event-driven Autoscaling): Configured on ACA to maintain minimum replicas and prevent cold starts.
* Bicep / Terraform & GitHub Actions: Enforces Infrastructure-as-Code and automated pipelines to eliminate configuration drift.

## Rationale
[This hybrid architecture balances rapid feature delivery with rigorous risk mitigation by decoupling new cloud workloads from the legacy mainframe. It strictly satisfies business and non-functional constraints through native traffic-splitting for instant rollbacks, secure hybrid networking, and robust automated observability.]