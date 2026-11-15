## Overview
[The system is a hybrid cloud insurance claims modernization platform designed to gradually replace a 30-year-old COBOL/DB2 mainframe while maintaining continuous claims processing. It provides secure, scalable web applications for customers, brokers, and adjusters while ensuring strict data consistency and seamless fallback capabilities.]

## Key Elements
- Modern Claims Platform [softwareSystem]
- End Customers and Brokers [person]
- Claims Adjusters [person]
- Migration Operations Managers [person]
- Legacy Mainframe System [externalSystem]
- Corporate Active Directory / Entra ID [externalSystem]
- Integration Middleware / API Gateway [externalSystem]
- Customer Web Portal (SPA/React) [container]
- Adjuster Web Application (Modular Monolith/.NET) [container]
- Migration Operations Dashboard (Web App/.NET) [container]
- Claims Core API Service (Modular Monolith/.NET) [container]
- Claim Router & Integration Worker (.NET Worker Service) [container]
- Azure Service Bus (Azure Messaging Service) [container]
  - Topic Router Component [component]
  - Session Manager Component [component]
  - Dead-Letter Monitor Component [component]
  - Claim Message Schema Registry Component [component]
  - Backpressure & Throttling Controller Component [component]

## Relationships
- End Customers and Brokers -> Customer Web Portal (HTTPS/REST)
- Claims Adjusters -> Adjuster Web Application (HTTPS/REST)
- Migration Operations Managers -> Migration Operations Dashboard (HTTPS/REST)
- Customer Web Portal -> Corporate Active Directory / Entra ID (OIDC/SAML)
- Adjuster Web Application -> Corporate Active Directory / Entra ID (OIDC/SAML)
- Migration Operations Dashboard -> Corporate Active Directory / Entra ID (OIDC/SAML)
- Claim Router & Integration Worker -> Legacy Mainframe System (mTLS/VPN and signed JWT)
- Claims Core API Service -> Azure Service Bus (AMQP)
- Claims Core API Service -> Claim Message Schema Registry Component (AMQP)
- Claim Message Schema Registry Component -> Topic Router Component (Internal memory/pipelining)
- Topic Router Component -> Claim Router & Integration Worker (AMQP via Azure Service Bus Subscriptions)
- Topic Router Component -> Session Manager Component (AMQP)
- Session Manager Component -> Claim Router & Integration Worker (AMQP)

## Technology Stack
- Azure Service Bus Premium Tier: Selected for geo-disaster recovery, VNet service endpoints, and auto-inflate capabilities to handle high throughput securely.
- .NET (Modular Monolith & Worker Services): Chosen for core backend logic and asynchronous claim routing due to robust enterprise capabilities.
- React (SPA): Used for interactive, modern customer and broker portal interfaces.
- Microsoft Entra ID (RBAC) with Managed Identities: Replaces SAS keys to enforce least-privilege security across all microservices.
- Terraform: Enforces Infrastructure-as-Code for consistent, automated, and drift-free deployments.
- Azure Key Vault: Manages Customer-Managed Keys (CMK) for encryption at rest and automated key rotation.

## Rationale
[This hybrid architecture bridges the legacy on-premises COBOL/DB2 mainframe with modern cloud services by leveraging Azure Service Bus as a reliable buffer to prevent data loss and enforce backpressure during strict batch windows. It mitigates the team's low cloud experience through managed Azure components and automated infrastructure deployment while fulfilling all regulatory, performance, and gradual migration constraints.]