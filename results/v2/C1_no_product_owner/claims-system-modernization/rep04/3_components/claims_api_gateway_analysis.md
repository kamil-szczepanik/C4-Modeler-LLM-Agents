## Overview
[The system modernizes a regional insurer's 30-year-old mainframe claims system via a hybrid cloud platform while ensuring legacy continuity. It gradually migrates claim types over three years using an Azure-based architecture.]

## Key Elements
- Claims API Gateway (Azure API Management)
- Routing & Policy Engine (APIM Policy XML / Policy Fragments)
- Token Validation & Claims Enriched Policy (APIM Policy XML)
- Dynamic Migration Router (APIM Named Values & Policy Fragments)
- Claims BFF (Node.js/Express on Azure App Service)
- Mainframe Integration Adapter (Azure App Service Worker)
- Insurer’s Active Directory

## Relationships
- Customer Portal / Adjuster Workspace -> Claims API Gateway via [HTTPS/REST]
- Claims API Gateway -> Claims BFF via [HTTPS/OIDC/OAuth2]
- Claims API Gateway -> Mainframe Integration Adapter via [HTTPS/REST via ExpressRoute/IPSec VPN with TLS 1.3]
- Claims API Gateway -> Insurer’s Active Directory via [OIDC/OAuth2]

## Technology Stack
- Azure API Management (APIM): Centralizes routing, security, and token validation with declarative policies due to team's limited cloud experience
- Azure App Service: Hosts BFF and integration adapter containers
- Azure Key Vault: Manages service-to-service credentials securely referenced via APIM named values
- Azure Monitor: Provides operational logging, tracing, and alerts

## Rationale
[This hybrid architecture abstracts backend migration complexity through API management while maintaining a secure perimeter. It decouples modern frontends from the legacy mainframe to meet strict operational constraints and ensure a one-day rollback capability.]