## Overview
Modernizes a regional insurer's legacy 30-year-old mainframe claims system by introducing a hybrid cloud platform using Azure API Management. This architecture enables gradual claim type migration while maintaining system reliability and security.

## Key Elements
- Azure API Management (APIM): Primary entry point and API Gateway
- API Gateway Component (Azure APIM Gateway Core): Handles incoming HTTPS/TLS traffic and rate limiting
- Policy Enforcement & Validation Component (APIM Policy Fragment Engine): Validates JWT/OIDC tokens
- API Versioning & Routing Component (APIM Path-based Routing): Maps endpoints and delegates routing
- Developer Portal Component (APIM Managed Developer Portal): Exposes OpenAPI specs
- Microsoft Entra ID: Identity provider for Single Sign-On (SSO)
- Routing & Integration Service (Azure Functions): Handles dynamic claim-type routing

## Relationships
- Customers / Brokers -> Azure API Management: Submits claims via API gateway [HTTPS / TLS]
- Claims Adjusters -> Azure API Management: Accesses adjuster workspace via API gateway [HTTPS / TLS]
- API Gateway Component -> Policy Enforcement & Validation Component: Evaluates security policies [Internal]
- Policy Enforcement & Validation Component -> Microsoft Entra ID: Token validation [OIDC / HTTPS]
- API Gateway Component -> Routing & Integration Service: Delegates dynamic claim-type routing [HTTP/HTTPS]

## Technology Stack
- Azure API Management (Premium Tier): Centralized ingress, security enforcement, and policy management
- Azure Functions: Executes lightweight dynamic routing logic to prevent brittle APIM policies
- Microsoft Entra ID: Manages Single Sign-On and OIDC/OAuth 2.0 token validation
- Azure Key Vault: Secures backend certificates and credentials via managed identity
- Bicep/Terraform: Enforces Infrastructure as Code and GitOps workflows

## Rationale
This architecture securely abstracts the hybrid transition from end-users while accommodating the team's low cloud experience through managed services. It supports incremental migration of claim types without disrupting legacy mainframe operations.