## Overview
[The system modernizes a 30-year-old regional insurance claims mainframe by gradually migrating claim types to a hybrid cloud platform. It ensures continuous claims processing, zero data loss, and rapid rollback capabilities.]

## Key Elements
- IT Administrators (Users)
- ArgoCD (GitOps Container)
- Azure Active Directory / Entra ID (External Authentication System)
- Routing Container (Go / mTLS)
- Azure Service Bus (Messaging Container)
- Azure Key Vault (Secret Management)
- Azure Monitor / SIEM (Observability)

## Relationships
- IT Administrators -> ArgoCD: Manages container rollouts and rollbacks via GitOps [HTTPS / Azure AD SSO]
- ArgoCD -> Azure Key Vault: Injects secrets securely at runtime [External Secrets Operator]
- ArgoCD -> Routing Container: Synchronizes routing configurations and feature flags [In-cluster API]
- ArgoCD -> Azure Monitor: Ships audit logs and application health metrics [HTTPS]

## Technology Stack
- ArgoCD: GitOps engine chosen to standardize rollouts and enable 1-day rollbacks for cloud-inexperienced teams.
- Azure Active Directory (Entra ID): Enforces SSO and RBAC for IT Administrator access.
- Azure Key Vault: Secures runtime secrets, preventing plain-text storage in Git.
- Azure Monitor: Collects audit logs and health metrics for operational visibility.

## Rationale
[This architecture uses declarative GitOps to simplify hybrid deployments and enable rapid rollbacks for a cloud-inexperienced team. It strictly separates deployment reconciliation from business logic, ensuring secure, compliant, and zero-downtime claim migrations.]