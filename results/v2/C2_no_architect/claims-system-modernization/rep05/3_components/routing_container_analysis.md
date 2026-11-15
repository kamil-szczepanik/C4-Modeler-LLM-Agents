## Overview
[The system is a hybrid cloud Insurance Claims Modernization platform that gradually replaces a 30-year-old on-premises mainframe with a modern Azure-hosted solution while ensuring continuous business operations.]

## Key Elements
- Customers and Brokers
- Claims Adjusters
- IT Administrators
- Legacy System (COBOL/DB2 Mainframe)
- Azure Active Directory (Entra ID)
- Customer Portal (React / HTTPS)
- Adjuster Web Application (React / OAuth2 / OIDC)
- Backend-For-Frontend (BFF) Container (Node.js / REST / HTTPS)
- Routing Container (Go / mTLS)
- Azure Service Bus (Azure Messaging)
- ArgoCD (GitOps)

## Relationships
- Customer Portal -> BFF Container: Submits claims online [HTTPS]
- Adjuster Web Application -> BFF Container: Handles claims [HTTPS]
- BFF Container -> Azure Service Bus: Publishes claim events [AMQP]
- Routing Container -> COBOL/DB2 Mainframe: Routes claims traffic to legacy system [mTLS]
- Routing Container -> ArgoCD: Synchronizes routing tables via GitOps configuration pipeline [Git]

## Technology Stack
- Go: Chosen for the Routing Container for high-performance network handling and low memory footprint.
- mTLS: Enforces strict bidirectional TLS with certificate pinning for secure hybrid communication.
- Azure Key Vault: Secures private keys and certificates for hybrid bridging, preventing plain-text storage.
- OpenTelemetry: Mandated for distributed tracing across the Azure boundary and on-premises mainframe.
- ArgoCD: Manages GitOps-driven configuration for rapid 1-day claim type rollbacks.

## Rationale
[This hybrid architecture isolates expensive mainframe dependencies while gradually migrating claim types via a resilient Routing Container. It satisfies strict latency, consistency, and security requirements through modern cloud patterns and GitOps control.]