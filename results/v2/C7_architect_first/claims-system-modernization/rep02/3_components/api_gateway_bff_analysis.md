## Overview
[Modernizes a regional insurer's legacy mainframe claims platform using a hybrid cloud architecture to gradually migrate claim types while maintaining continuous legacy operations.]

## Key Elements
- [Azure Front Door]
- [API Gateway / BFF (Node.js/TypeScript Container)]
- [Customer Portal & Adjuster Workspace (React Web Apps)]
- [Claims Processing Service & Integration Bridge]
- [Redis Container]
- [Insurer Active Directory]

## Relationships
- [Customers and Brokers -> Azure Front Door: HTTPS]
- [Azure Front Door -> API Gateway / BFF: HTTPS/TLS 1.3]
- [API Gateway / BFF -> Insurer Active Directory: OpenID Connect (OIDC)]
- [API Gateway / BFF -> Redis Container: TCP]
- [API Gateway / BFF -> Claims Processing Service & Integration Bridge: gRPC/mTLS]

## Technology Stack
- [Node.js / TypeScript: Simplifies BFF development for teams with low cloud experience]
- [Azure Container Apps: Provides container hosting with automated horizontal autoscaling]
- [Azure Front Door: Handles geo-routing, SSL offloading, and DDoS protection]
- [Redis: Stores dynamic claim-type routing rules and fallback flags]
- [OpenID Connect & JWT: Enables single sign-on with Active Directory]

## Rationale
[This hybrid architecture isolates complex cloud infrastructure behind manageable container deployments while enabling safe, gradual claim migration. It meets stringent performance, security, and fallback requirements without overwhelming the team's cloud skill set.]