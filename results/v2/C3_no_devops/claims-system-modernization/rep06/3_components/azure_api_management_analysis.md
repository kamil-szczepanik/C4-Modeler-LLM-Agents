## Overview
[The system modernizes a 30-year-old regional insurance claims mainframe by gradually migrating claim types to a cloud platform. Azure API Management acts as the central hybrid routing and security gateway.]

## Key Elements
* Azure API Management (APIM) Container
* API Gateway Component (Edge proxy, JWT validation, rate-limiting)
* Policy Engine Component (XML dynamic routing, correlation ID injection)
* Azure Kubernetes Service (AKS)
* On-Premises COBOL/DB2 Mainframe
* Azure Entra ID
* Azure Application Insights

## Relationships
* API Gateway Component -> Azure Kubernetes Service: Forwards modernized claim requests [HTTPS / REST]
* API Gateway Component -> On-Premises COBOL/DB2 Mainframe: Routes legacy traffic [mTLS over ExpressRoute / IPsec VPN]
* API Gateway Component -> Azure Entra ID: Validates OIDC/OAuth2 tokens [HTTPS / REST]
* Policy Engine Component -> Azure Application Insights: Streams sanitized telemetry and metrics [HTTPS]

## Technology Stack
* Azure API Management (Internal VNet Mode): Manages hybrid routing and protects the legacy mainframe
* Azure Entra ID: Enforces Single Sign-On and OAuth2/OIDC JWT token validation
* Azure Key Vault: Manages certificate lifecycle and pinning for mainframe mTLS integration
* Azure Application Insights: Collects sanitized operational telemetry and business metrics

## Rationale
[This architecture uses Azure API Management in Internal VNet Mode to safely route traffic between modern microservices and the legacy mainframe. This design ensures seamless gradual migration and rapid one-day rollbacks while protecting sensitive data.]