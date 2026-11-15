## Overview
[The hybrid Insurance Claims Modernization platform gradually replaces an on-premise mainframe system while ensuring continuous, zero-loss claim processing during the 3-year transition. It empowers customers, brokers, and adjusters with modern cloud-native web applications hosted in Azure West Europe.]

## Key Elements
- **Customers & Brokers:** External users performing online claim submissions (R-01).
- **Claims Adjusters:** Internal users handling claims via the new web application (R-02).
- **Insurance Claims Modernization Platform:** Cloud-native target system hosted in Azure West Europe.
- **Legacy Mainframe:** On-premise COBOL/DB2 system of record (3-year retention constraint).
- **Azure AD (Entra ID):** Identity provider for Single Sign-On (R-07).
- **Payment Gateway:** External financial system for automated claim payouts.
- **Core Notification Service:** External system for automated SMS/email updates.
- **Enterprise Service Bus (ESB/MQ):** Hybrid messaging intermediary.

## Relationships
- **Customers/Brokers -> Platform:** HTTPS (REST/GraphQL) for claim submissions.
- **Adjusters -> Platform:** HTTPS for UI interactions (sub-2s latency via R-05).
- **Platform <-> Legacy Mainframe:** Asynchronous messaging via ESB/MQ and secure queue transfers (respecting the 23:00–05:00 batch window).
- **Platform -> Azure AD:** OpenID Connect / OAuth 2.0 via HTTPS for SSO and RBAC.
- **Platform -> Payment Gateway:** HTTPS (REST with OAuth 2.0) with idempotency tokens.
- **Platform -> Notification Service:** Asynchronous Webhooks via Azure Event Grid (HTTPS).

## Technology Stack
- **Cloud Provider:** Hybrid (Azure West Europe + On-Premise Mainframe) chosen for phased migration.
- **Infrastructure as Code (IaC):** Terraform / Bicep to mitigate low cloud team experience.
- **Integration & Messaging:** Enterprise Service Bus / MQ for asynchronous decoupling and R-06 rollback support.
- **Security Protocols:** mTLS for hybrid boundaries, AES-256 via Azure Key Vault for data at rest.
- **API & Traffic Management:** API Gateway with dynamic routing and automated feature toggling for instant claim-type rollbacks.

## Rationale
[Asynchronous messaging via an ESB completely decouples the cloud platform from the brittle on-premise mainframe, protecting the immutable nightly batch window. Furthermore, dynamic traffic routing and automated feature toggles fulfill the strict one-day fallback SLA (R-06), mitigating risks associated with the team's low cloud experience.]