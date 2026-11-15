## Overview
[The system modernizes a regional insurer's legacy COBOL/DB2 mainframe claims platform using a hybrid cloud architecture. Its core purpose is to gradually migrate claim types while maintaining continuous legacy operations and data consistency.]

## Key Elements
- **Users**: Customer, Broker, Claims Adjuster, Business Operations Manager
- **External Systems**: COBOL/DB2 Mainframe System of Record
- **Containers**: Modern Web Application (React, ASP.NET Core), API Gateway / Ingress Controller (Azure Application Gateway / NGINX), Azure Service Bus, Azure Cache for Redis, Business/Migration Analytics Container (Python, Azure Analytics), Data Sync & Reconciliation Jobs (Azure Container Instances / Functions)

## Relationships
- Customer -> API Gateway / Ingress Controller: Submits claims and interacts with portal [HTTPS/OAuth2]
- Broker -> API Gateway / Ingress Controller: Submits claims on behalf of customers [HTTPS/OAuth2]
- Claims Adjuster -> API Gateway / Ingress Controller: Interacts with adjuster UI [HTTPS, RBAC, Azure AD SSO]
- Business Operations Manager -> API Gateway / Ingress Controller: Accesses business dashboards [HTTPS]
- API Gateway / Ingress Controller -> Modern Web Application: Forwards HTTP requests [HTTP/REST]

## Technology Stack
- **API Gateway / Ingress**: Azure Application Gateway / NGINX for dynamic traffic splitting and circuit breaking.
- **Security & Identity**: Azure Active Directory SSO with edge JWT validation and encrypted session cookies.
- **Compute & Frontend**: React and ASP.NET Core hosted in Azure West Europe.
- **Infrastructure & Deployment**: Terraform/Bicep with GitOps pipelines (ArgoCD) for immutable gateway configurations.

## Rationale
- [The hybrid architecture bridges legacy on-premise mainframe constraints with modern cloud capabilities while ensuring zero data loss during incremental migration.]
- [Edge-based routing and automated secrets management compensate for the team's low cloud experience while enforcing strict performance and security NFRs.]