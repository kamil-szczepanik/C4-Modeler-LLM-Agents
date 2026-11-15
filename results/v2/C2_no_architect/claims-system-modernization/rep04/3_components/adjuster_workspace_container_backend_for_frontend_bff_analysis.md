## Overview
This architecture summary outlines the modern cloud-native Adjuster Workspace Backend-For-Frontend (BFF) for the hybrid Insurance Claims Modernization platform. It enables rapid adjuster workflows while maintaining seamless integration with the legacy on-premises mainframe during the 3-year migration.

## Key Elements
- Claims Adjusters (Primary Users)
- Adjuster Workspace Container & BFF (Azure Container Apps)
- Azure Cache for Redis (PaaS)
- Azure API Gateway / Integration Container
- Azure Key Vault
- Azure Application Insights / Azure Monitor
- Azure Storage (WORM-enabled for audit logs)

## Relationships
- Claims Adjusters -> Adjuster Workspace Container & BFF: Manage claims via web interface [HTTPS/TLS 1.3]
- Adjuster Workspace Container & BFF -> Azure API Gateway / Integration Container: Routes microservice requests [Internal Azure VNets]
- Adjuster Workspace Container & BFF -> Azure Cache for Redis: Reads cached claim states and session data [Redis Protocol over TLS]
- Adjuster Workspace Container & BFF -> Azure Key Vault: Retrieves secrets and credentials [Azure Managed Identities]
- Adjuster Workspace Container & BFF -> Azure Storage: Streams tamper-evident audit logs [HTTPS/TLS 1.3]

## Technology Stack
- Azure Container Apps (ACA): Provides serverless container orchestration to minimize Kubernetes management complexity for a cloud-inexperienced team.
- Azure Cache for Redis: Delivers high-performance data caching to meet sub-2-second adjuster screen load requirements despite slow mainframe responses.
- Azure Active Directory / Entra ID: Enforces OpenID Connect (OIDC) Single Sign-On and RBAC at the BFF boundary.
- Azure Application Insights: Enables end-to-end distributed tracing and health monitoring across hybrid on-prem and cloud boundaries.
- Azure DevOps / GitHub Actions: Automates deployment pipelines and rollback triggers for rapid R-06 switchbacks.

## Rationale
The architecture decouples the modern adjuster workspace from legacy performance bottlenecks using caching and circuit breakers, strictly ensuring sub-2-second response times. Furthermore, it embeds enterprise-grade security, WORM audit logging, and managed cloud services to protect sensitive PII while mitigating operational risks for a team with limited cloud experience.