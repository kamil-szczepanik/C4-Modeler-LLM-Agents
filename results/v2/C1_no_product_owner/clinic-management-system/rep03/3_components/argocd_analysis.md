## Overview
The system is ArgoCD, a GitOps continuous delivery tool deployed across hybrid Kubernetes clusters (`on-prem-k8s` and `eu-central-1`) to automate application deployments. Its core purpose is to maintain high availability (99.99%) and strict compliance for the Clinic Management System.

## Key Elements
- **API Server**: Manages Web UI, CLI, webhook receivers, and OIDC/MFA authentication.
- **Repository Server**: Clones Git repositories and renders Helm charts without caching unencrypted data.
- **Application Controller**: Core reconciliation engine executing state synchronization with Kubernetes API servers.
- **Redis Cache**: In-memory data store providing HA state caching and session management.
- **HashiCorp Vault**: Secure secret management and dynamic runtime decryption provider.

## Relationships
- **API Server** uses **Internal gRPC** to command the **Repository Server** and **Application Controller**.
- **API Server** and **Application Controller** interact with **Redis Cache** via **TCP/TLS**.
- **Application Controller** communicates with `on-prem-k8s` and `eu-central-1` clusters via **HTTPS/Kubernetes API**.
- **API Server** delegates user authentication to **Enterprise IdP** via **HTTPS/OIDC**.
- **Repository Server** integrates with **HashiCorp Vault** for runtime secret injection.

## Technology Stack
- **Go**: Core language for ArgoCD components, providing high performance and concurrency.
- **Redis**: In-memory cache for state persistence and high-availability reconciliation scaling.
- **HashiCorp Vault**: Secure credential management ensuring HIPAA/GDPR compliance for data at rest.
- **Kubernetes / Helm**: Container orchestration and packaging format for hybrid cloud deployment.

## Rationale
This decoupled microservices architecture ensures 99.99% availability and swift reconciliation loops across hybrid cloud environments. Strict mTLS, OIDC/MFA integration, and runtime Vault injection satisfy rigorous HIPAA and GDPR compliance constraints.