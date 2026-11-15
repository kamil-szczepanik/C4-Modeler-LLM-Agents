## Overview
Azure API Management (APIM) serves as the entry-point API Gateway for the hybrid insurance claims modernization platform. It abstracts legacy complexities, secures communications, and controls traffic routing between modern Azure cloud services and the on-premises mainframe.

## Key Elements
* API Gateway: Azure API Management (APIM)
* Downstream Consumers: Customers, Brokers, and Claims Adjusters
* Upstream Systems: Azure App Service (Modular Monolith) and On-Premises COBOL/DB2 Mainframe
* Identity Provider: Microsoft Entra ID (Azure Active Directory)
* Observability: Azure Application Insights

## Relationships
* Customers & Brokers -> Azure APIM: Submit online claims [HTTPS via TLS 1.3]
* Azure APIM -> Microsoft Entra ID: Authenticates requests [OpenID Connect / OAuth 2.0]
* Azure APIM -> Azure App Service: Forwards validated requests [HTTPS / W3C Trace Context]
* Azure APIM -> On-Premises Mainframe: Routes fallback/legacy claim types [ExpressRoute / HTTPS]
* Azure APIM -> Azure Application Insights: Exports sanitized telemetry [HTTPS]

## Technology Stack
* Azure API Management (APIM): Chosen for out-of-the-box routing, rate limiting, and policy enforcement to accommodate the team's limited cloud experience.
* OpenAPI 3.0 / JSON Schema: Enforces contract-first design and payload validation at the gateway level.
* Microsoft Entra ID: Provides enterprise Single Sign-On (SSO) and JWT token validation.
* W3C Trace Context: Standardizes correlation ID propagation for end-to-end distributed tracing.
* Infrastructure-as-Code (IaC): Stores all gateway policies and configurations in version control to prevent drift and ensure repeatability.

## Rationale
The API Gateway architecture decouples client applications from backend migration turbulence, enabling seamless, zero-downtime traffic switching between the cloud and the legacy mainframe. Furthermore, enforcing security, validation, and circuit-breaking policies at the gateway protects fragile downstream legacy systems while mitigating the team's limited cloud expertise.