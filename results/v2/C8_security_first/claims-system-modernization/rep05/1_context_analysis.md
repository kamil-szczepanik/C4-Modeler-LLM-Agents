## Overview
Gradually replaces a 30-year-old on-premise mainframe claims system with a modern cloud-native platform in Azure. Maintains business continuity and data consistency during a three-year hybrid migration period.

## Key Elements
* End Customers & Brokers (Users)
* Claims Adjusters (Users)
* Operations & Migration Team (Users)
* New Insurance Platform (Azure West Europe)
* Legacy Mainframe (On-premise COBOL/DB2)
* Microsoft Entra ID (Identity Provider)
* Notification Service (Third-party SendGrid/Twilio)

## Relationships
* End Customers/Brokers -> New Platform: HTTPS (REST/GraphQL) for online claims
* Adjusters -> New Platform: HTTPS (OIDC/OAuth 2.0 via Entra ID)
* New Platform <-> Legacy Mainframe: Asynchronous messaging and secure API Gateway via mTLS over hybrid VPN/ExpressRoute
* New Platform -> Notification Service: HTTPS (REST API) via event-driven messaging

## Technology Stack
* Cloud Platform: Azure App Service / Azure Container Apps (managed PaaS to offset low cloud experience)
* Infrastructure-as-Code: Terraform / Bicep for automated, drift-free environments
* API Gateway & Security: Azure API Management (APIM) with mTLS (TLS 1.3), AES-256 encryption, rate-limiting, and circuit breakers
* Messaging & Routing: Azure Service Bus with feature flags for claim-type toggling and fallback
* Observability: OpenTelemetry and Azure Sentinel / Log Analytics for distributed tracing and audit logging

## Rationale
The hybrid architecture isolates the costly, rigid mainframe behind an asynchronous API gateway, protecting the strict nightly batch window. Cloud-native managed services and feature flags enable rapid adjuster screen performance and a one-day rollback safety net for migrated claim types.