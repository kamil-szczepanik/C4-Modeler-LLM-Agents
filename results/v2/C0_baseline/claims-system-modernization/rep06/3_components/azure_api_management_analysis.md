## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a 30-year-old mainframe while ensuring continuous processing. It utilizes Azure cloud services integrated with an on-premise mainframe to enable seamless claim migrations and low-latency adjuster workflows.

## Key Elements
- Azure API Management (APIM): Internal VNet mode gateway acting as the single secure entry point.
- Azure Application Gateway with WAF: Fronts APIM to inspect incoming traffic for threats.
- Claims Processing Service: Java, Spring Boot service hosted in Azure Container Apps.
- Migration Dashboard: React, Node.js container application for migration management.
- On-premise COBOL/DB2 Legacy Mainframe: System of record connected via Azure Logic Apps and Azure Functions.
- Supporting Azure Services: Azure Service Bus, Azure SQL Database (TDS), Azure Key Vault, Azure Active Directory (Entra ID), Azure Application Insights.

## Relationships
- Customer / Broker -> Azure Application Gateway: Online claim submission via HTTPS / REST.
- Claims Adjuster -> Azure Application Gateway: Web application access via HTTPS / OAuth 2.0 / OpenID Connect.
- Azure Application Gateway -> Azure API Management: Secure traffic forwarding via internal VNet.
- Azure API Management -> Claims Processing Service: Dynamic claim-type routing via internal VNet using mTLS.
- Azure API Management -> Migration Dashboard: Dashboard traffic routing via internal VNet using mTLS.
- Azure API Management -> Azure Active Directory (Entra ID): JWT token validation via OAuth 2.0 / OpenID Connect.
- Azure API Management -> Azure Application Insights: Telemetry and metrics publishing via HTTPS.

## Technology Stack
- Azure API Management (Standard/Premium): Selected as the API gateway for routing and rate limiting.
- Azure Container Apps: Hosts microservices with low cloud operational overhead.
- Java & Spring Boot: Core runtime for modern claim processing logic.
- Azure Active Directory (Entra ID): Enforces Single Sign-On (SSO) and OAuth 2.0 / OpenID Connect.
- Bicep / Terraform & GitOps: Implements Infrastructure as Code for reliable deployments and rollbacks.
- Mutual TLS (mTLS) & Azure Key Vault: Secures service-to-service communication and secret management.

## Rationale
The hybrid architecture protects the fragile, expensive-to-change on-premise mainframe while incrementally migrating claim types to the cloud. Leveraging managed Azure services minimizes operational complexity for a team with limited cloud experience while meeting strict security, consistency, and fallback requirements.