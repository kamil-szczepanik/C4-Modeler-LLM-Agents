## Overview
[The hybrid Insurance Claims Modernization platform gradually replaces a legacy mainframe system while ensuring uninterrupted operations. It provides secure digital claim submissions and high-performance adjuster workflows while maintaining strict data consistency.]

## Key Elements
- Customers / Brokers: External users submitting claims online via web interfaces.
- Claims Adjusters: Internal staff processing claims in the new web application.
- Insurance Claims Modernization Platform: Target hybrid solution hosted in Azure West Europe and on-premises.
- Legacy Mainframe: 30-year-old COBOL/DB2 system of record (IBM z/OS).
- Active Directory / Microsoft Entra ID: Identity provider for Single Sign-On.
- Payment Gateway: External system handling claim payouts.

## Relationships
- Customer / Broker -> Insurance Claims Modernization Platform: Submit claims [HTTPS / TLS 1.3, OIDC/OAuth 2.0].
- Claims Adjuster -> Insurance Claims Modernization Platform: Process claims [HTTPS / TLS 1.3, OIDC/OAuth 2.0].
- Insurance Claims Modernization Platform -> Legacy Mainframe: Synchronize claims and process transactions [SFTP / MQ via On-Premises Gateway, respecting the 23:00-05:00 batch window].
- Insurance Claims Modernization Platform -> Active Directory: Federated authentication [SAML/OIDC].
- Insurance Claims Modernization Platform -> Payment Gateway: Process payouts [REST / HTTPS API].

## Technology Stack
- Azure Cloud & Azure Bicep: Infrastructure platform and Infrastructure as Code to accommodate the team's low cloud experience and prevent configuration drift.
- Azure Service Bus / On-Premises Gateway: Asynchronous messaging to decouple cloud components from legacy batch windows and guarantee zero data loss.
- Azure Application Insights: Distributed tracing across hybrid boundaries to resolve consistency and performance bottlenecks.
- Microsoft Entra ID & Azure Key Vault: Secure credential management, RBAC, and OAuth 2.0 / OIDC authentication enforcing mTLS and TLS 1.3.

## Rationale
[This hybrid architecture mitigates strict mainframe constraints and interface change limits through asynchronous decoupling and caching layers that achieve sub-2-second response times. It guarantees business continuity, secure data handling, and rapid rollbacks within one day if migrated claim types require reversion.]