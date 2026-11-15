## Overview
[The system modernizes a regional insurer's 30-year-old COBOL/DB2 mainframe claims system via a hybrid cloud platform. It enables online claims processing while maintaining legacy integration.]

## Key Elements
[
• Customers and Brokers
• Claims Adjusters
• IT Administrators
• Legacy System (COBOL/DB2 Mainframe)
• Azure Active Directory (Entra ID)
• Customer Portal (React / HTTPS)
• Adjuster Web Application (React / OAuth2 / OIDC)
• Backend-For-Frontend (BFF) Container (Node.js / REST / HTTPS / Azure App Configuration / Azure Redis)
• Routing Container (Go / mTLS / Istio)
• Azure Service Bus (AMQP)
• ArgoCD (GitOps)
]

## Relationships
[
• Adjuster Web Application -> Backend-For-Frontend (BFF) Container: Exchanges tokens and data via REST/HTTPS with OAuth2 Token Exchange (RFC 8693)
• Backend-For-Frontend (BFF) Container -> COBOL/DB2 Mainframe: Interacts across hybrid boundary using mTLS, circuit breakers, and OpenTelemetry
• Backend-For-Frontend (BFF) Container -> Azure Service Bus: Exchanges asynchronous events via AMQP messaging
• Backend-For-Frontend (BFF) Container -> Azure Key Vault: Retrieves secrets securely via Managed Identities / HTTPS
• Routing Container -> COBOL/DB2 Mainframe: Manages ingress traffic and standardized resilience policies via mTLS
]

## Technology Stack
[
• React: Frontend UI for customer portal and adjuster web application
• Node.js: Backend-For-Frontend (BFF) container runtime providing caching and security perimeters
• Go: Routing container technology ensuring lightweight network performance
• Azure Service Bus: Asynchronous event messaging platform
• Azure App Configuration: Centralized feature flag management for incremental migration
• Azure Redis: Encrypted caching layer for session and claim data
• ArgoCD: GitOps deployment tool for zero-downtime Blue/Green rollouts
]

## Rationale
[The hybrid architecture preserves the stable legacy mainframe as the system of record while using Azure managed services to overcome the team's limited cloud experience. It decouples legacy dependencies through a secure BFF container and routing layer, ensuring sub-second UI performance and gradual claim type migration.]