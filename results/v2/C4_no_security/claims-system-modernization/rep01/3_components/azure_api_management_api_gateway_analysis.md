## Overview
The system is a hybrid cloud insurance claims modernization platform that gradually replaces a 30-year-old mainframe. It uses Azure API Management (APIM) as a centralized ingress security and dynamic routing layer.

## Key Elements
* Azure API Management (API Gateway) (Azure APIM)
* Token Validator Component
* API Router & Policy Engine
* Internal Developer Portal
* Rate Limiting & Quota Enforcer
* Backend Circuit Breaker & Retry Engine

## Relationships
* Policyholders -> Azure API Management (API Gateway): Single sign-on and secure entry [HTTPS, OIDC, OAuth2]
* Brokers -> Azure API Management (API Gateway): Single sign-on and secure entry [HTTPS, OIDC, OAuth2]
* Claims Adjusters -> Azure API Management (API Gateway): Single sign-on and secure entry [HTTPS, OIDC, OAuth2]
* API Router & Policy Engine -> Adjuster BFF: Routes authenticated adjuster requests [HTTPS, gRPC]
* API Router & Policy Engine -> Anti-Corruption Layer (ACL) Gateway: Routes unmigrated claim traffic to legacy endpoints [HTTPS, JSON]

## Technology Stack
* Azure API Management (APIM): Centralized ingress routing, security, and policy enforcement
* ASP.NET Core / OAuth2: Token validation and claim extraction
* XML-based APIM Policies: Dynamic backend routing, rate limiting, and circuit breakers
* GitHub Actions & Azure API Management DevOps Resource Kit: GitOps automation for APIM configurations
* Bicep / Terraform: Infrastructure as Code provisioning
* Azure Application Insights & Azure Monitor: Observability and latency tracking

## Rationale
This architecture decouples the legacy mainframe from modern frontends while ensuring high security, observability, and sub-2-second adjuster screen performance. APIM policies enable zero-downtime traffic shifting and one-day rollbacks without requiring expensive mainframe modifications.