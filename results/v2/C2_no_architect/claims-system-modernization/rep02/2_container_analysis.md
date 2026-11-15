## Overview
Gradually replaces a 30-year-old on-premises COBOL/DB2 mainframe claims system with a modern hybrid platform hosted in Azure West Europe. It ensures zero data loss and sub-second performance during a three-year incremental migration.

## Key Elements
* **Users:** Policyholders, Brokers, Claims Adjusters, Compliance and Audit Officers
* **Containers (Azure AKS):** Claims Web App, Integration Service, Claim Reconciliation Service, API Gateway
* **External Systems:** COBOL/DB2 Mainframe (On-premises), Azure Active Directory / Entra ID

## Relationships
* **Policyholders / Brokers & Claims Adjusters -> API Gateway:** HTTPS / TLS 1.3 via OAuth2/OIDC Single Sign-On
* **Claims Web App -> Azure Redis:** In-memory caching for UI acceleration via TCP
* **Claims Web App -> Azure Service Bus:** Asynchronous message queueing for claim submissions via AMQP
* **Integration Service -> COBOL/DB2 Mainframe:** Hybrid integration over mTLS (TLS 1.3) with certificate pinning
* **Claim Reconciliation Service -> COBOL/DB2 Mainframe:** Audit data verification and state synchronization over mTLS

## Technology Stack
* **Cloud & Orchestration:** Azure Kubernetes Service (AKS) managed via Terraform/Bicep and ArgoCD GitOps to address low cloud experience.
* **Security & IAM:** Azure Active Directory / Entra ID for SSO; Azure Key Vault with Customer-Managed Keys (CMK) and Azure Managed Identities for secretless workloads.
* **Messaging & Caching:** Azure Service Bus for asynchronous messaging and Azure Redis for distributed caching to meet performance targets.
* **Observability:** Azure App Insights, Azure Monitor, and Azure Sentinel for distributed tracing, synthetic monitoring, and immutable audit logs.

## Rationale
The hybrid architecture decouples modern Azure containers from slow mainframe responses using asynchronous queues and caching, guaranteeing sub-2-second UI performance. Immutable deployments, mTLS security boundaries, and a dedicated reconciliation service ensure strict data consistency, compliance, and rapid claim-type rollbacks.