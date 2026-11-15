## Overview
[The system is a hybrid cloud insurance claims modernization platform that gradually replaces a legacy on-premises mainframe while maintaining continuous claim processing. Its core purpose is to enable online customer submissions and fast adjuster workflows through an incremental strangler-fig migration.]

## Key Elements
- End Customers & Brokers
- Claims Adjusters
- Operations & Finance Teams
- On-Premises COBOL/DB2 Mainframe (System of Record)
- Azure API Gateway / Integration Container (Anti-Corruption Layer)
- Customer & Broker Portal Container
- Adjuster Workspace Container & Backend-For-Frontend (BFF)
- Azure Container Apps (ACA) / Managed Kubernetes (AKS)
- Azure Cache for Redis (PaaS)
- Azure Key Vault

## Relationships
- Customers/Brokers interact with Customer & Broker Portal via HTTPS/TLS 1.3
- Adjusters interact with Adjuster Workspace Container via HTTPS/TLS 1.3
- API Gateway routes requests to internal microservices via internal Azure Virtual Networks (VNets)
- API Gateway communicates with On-Premises COBOL/DB2 Mainframe via mTLS and TLS 1.3
- Adjuster Workspace BFF queries Azure Cache for Redis (PaaS) for read-heavy caching and session state
- Azure Container Apps authenticate to Azure Key Vault and databases using Azure Managed Identities

## Technology Stack
- Azure Container Apps (ACA) / Managed Kubernetes (AKS): Container runtime providing managed PaaS to mitigate low cloud experience
- Azure API Gateway: Manages hybrid routing, OAuth 2.0 / OIDC authentication, and the strangler fig pattern
- Azure Cache for Redis (PaaS): Offloads session state and caching to meet the <2s adjuster screen latency requirement
- Azure AD / Entra ID: Federates with on-premises Active Directory for Single Sign-On (SSO)
- GitOps (GitHub Actions / ArgoCD) & IaC: Automates deployments and eliminates configuration drift
- OpenTelemetry & Prometheus: Centralized observability stack spanning Azure and on-prem boundaries

## Rationale
[This hybrid architecture satisfies strict business constraints by isolating the expensive, slow on-premises mainframe behind an integration and caching layer. It protects data consistency and ensures low-latency user experiences while incrementally migrating claim types over three years.]