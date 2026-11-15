## Overview
The system is a hybrid modern claims platform that gradually replaces a 30-year-old COBOL/DB2 mainframe claims system while maintaining uninterrupted processing. It enables online claim submission for customers and a high-performance web interface for adjusters during a phased migration.

## Key Elements
- **Users:** Customers, Brokers, Claims Adjusters, Business Operations / Compliance Officers, IT Administrators.
- **Frontend Containers:** Customer Portal, Adjuster Web Application, Backend-For-Frontend (BFF) Container.
- **Integration & Core Containers:** Routing Container, Azure Service Bus, ArgoCD (GitOps).
- **External Systems:** COBOL/DB2 Mainframe (on-premises system of record), Azure Active Directory / Entra ID, Azure Key Vault.

## Relationships
- **Users to Frontend:** Customers/Brokers access the Customer Portal via HTTPS/TLS 1.3; Adjusters access the Adjuster Web Application using OAuth2/OIDC Single Sign-On authenticated against Azure AD.
- **Frontend to BFF:** Adjuster Web Application communicates with the BFF container via REST/HTTPS using OAuth2 Token Exchange (RFC 8693).
- **Platform to Mainframe:** Routing Container and BFF interact with the on-prem COBOL/DB2 Mainframe across a hybrid boundary secured by mTLS and circuit breakers.
- **Internal Messaging:** Containers exchange asynchronous events via Azure Service Bus with idempotent event publishing.

## Technology Stack
- **Cloud & Orchestration:** Hybrid deployment across On-Premises Mainframe and Azure West Europe using GitOps (ArgoCD) to standardize container rollouts and enable 1-day rollbacks.
- **Security & Identity:** Azure AD (Entra ID) for SSO/RBAC, Azure Key Vault with Managed Identities for secret management, and TLS 1.3 / mTLS for transport security.
- **Integration & Messaging:** Azure Service Bus for asynchronous message queuing and idempotent event publishing.
- **Observability:** OpenTelemetry for distributed tracing across Azure containers and the on-prem mainframe.

## Rationale
This hybrid architecture isolates incremental claim migrations while protecting the legacy mainframe during its 3-year phased retirement. The BFF caching layer and asynchronous messaging ensure adjuster UI performance targets are met despite slow legacy response times.