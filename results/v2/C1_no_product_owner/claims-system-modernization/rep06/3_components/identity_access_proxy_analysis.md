## Overview
[The Identity & Access Proxy container secures and routes traffic for the Insurance Claims Modernization platform using Azure API Management. It federates hybrid cloud identities with the on-premise Active Directory while enforcing Zero-Trust policies.]

## Key Elements
- Token Validator Component (APIM Policy, OAuth2, OIDC)
- Claims API Gateway Router (APIM Policies, Backend Pools)
- Rate Limiter & Throttling Policy (APIM Built-in Policy)
- Token Exchange & Claims Transformation Component (APIM Liquid Templates)

## Relationships
- Token Validator Component -> Insurer's Active Directory: Validates OIDC tokens and caches validation states [HTTPS/OIDC]
- Token Validator Component -> Token Exchange & Claims Transformation Component: Passes verified identity context [Internal]
- Token Exchange & Claims Transformation Component -> Claims API Gateway Router: Forwards requests with transformed internal JWTs [Internal]
- Claims API Gateway Router -> Claims Core API: Routes secured requests over container networks [HTTPS/mTLS]

## Technology Stack
- Azure API Management (APIM): Abstracts complex ingress routing and security to accommodate low cloud experience teams
- OAuth2 & OIDC: Standardizes authentication federation with Insurer's Active Directory
- Azure Monitor: Tracks federation latency and streams security audit logs for compliance
- Azure Key Vault & CSI Secret Store Drivers: Securely injects API keys, certificates, and secrets

## Rationale
[This architecture uses managed Azure services to minimize operational complexity for a team with limited cloud experience while enforcing strict security boundaries. Caching and token transformation protect legacy system performance and ensure reliable hybrid authentication.]