## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a hybrid cloud platform in Azure West Europe while maintaining the legacy system of record. It enables online claim submissions, modern adjuster workflows, and incremental claim-type migrations without extending the nightly batch window (23:00-05:00).

## Key Elements
- **Users**: Customer, Broker, Claims Adjuster, Business Operations Manager, Migration Administrator
- **External Systems**: COBOL/DB2 Mainframe System of Record (on-premises)
- **Containers**: Modern Web Application (Customer/Broker portal and Adjuster UI), API Gateway / Ingress Controller, Azure Service Bus (async message broker), Azure Cache/Local Caching Layer, Business/Migration Analytics Container, Data Sync & Reconciliation Jobs
- **Infrastructure**: Azure Kubernetes Service (AKS), Azure Key Vault, Azure Active Directory (Azure AD)

## Relationships
- Customers and Brokers submit claims via HTTPS/OAuth2 to the Modern Web Application.
- Claims Adjusters interact with the Modern Web Application using RBAC and Azure AD SSO.
- Modern Web Application communicates with the Azure Service Bus and Azure Cache for asynchronous buffering and performance isolation.
- Data Sync & Reconciliation Jobs connect across the hybrid trust boundary to the on-premise COBOL/DB2 Mainframe using mTLS with certificate pinning.
- CI/CD pipelines deploy to Azure Kubernetes Service (AKS) using Terraform and ArgoCD with OIDC-based federation.

## Technology Stack
- **Cloud Provider**: Hybrid (On-premises mainframe and Azure West Europe)
- **Container Orchestration**: Azure Kubernetes Service (AKS) for containerized workloads
- **Integration & Messaging**: Azure Service Bus for asynchronous buffering to isolate mainframe latency
- **Caching & Data**: Azure Cache with Azure Key Vault (Customer-Managed Keys) for secure data-at-rest encryption
- **Security & Identity**: Azure AD with OAuth2/OIDC, mTLS for hybrid boundary traffic, eBPF-based runtime security
- **DevOps & Observability**: Terraform and ArgoCD (IaC/GitOps), OpenTelemetry for distributed tracing, synthetic monitoring

## Rationale
This hybrid architecture isolates the new cloud-native web application from mainframe latency and expensive legacy changes using asynchronous messaging and caching, meeting strict performance and zero-loss consistency requirements. Leveraging managed Azure services and GitOps mitigates the team's limited cloud experience while ensuring rapid rollout, robust security controls, and a reliable 1-day fallback mechanism.