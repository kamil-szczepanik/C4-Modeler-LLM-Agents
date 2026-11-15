## Overview
[The system modernizes a 30-year-old regional insurer's claims platform via a hybrid architecture. It gradually migrates claim types from the legacy mainframe to Azure while maintaining uninterrupted core operations.]

## Key Elements
- Customers & Brokers: External users submitting claims via web browser.
- Claims Adjusters: Internal staff handling claims via web application.
- New Claims Platform: Azure-hosted containerized application (.NET Core on AKS/App Service).
- Legacy Mainframe: On-premises IBM z/OS COBOL/DB2 system of record.
- Active Directory: On-premises identity provider.
- Notification Service: External SaaS (Twilio SendGrid/Azure Communication Services).
- Telemetry & Monitoring: Azure Application Insights/Azure Monitor.

## Relationships
- Customers/Brokers -> New Claims Platform: HTTPS (Online claim submission, R-01).
- Claims Adjusters -> New Claims Platform: HTTPS (Claim management, R-02, <2s load time).
- New Claims Platform <-> Legacy Mainframe: TLS via VPN/ExpressRoute with mTLS (Claim data proxying).
- New Claims Platform -> Active Directory: OIDC/OAuth 2.0 via Azure AD Connect (Single sign-on, R-07).
- New Claims Platform -> Notification Service: HTTPS REST API (SMS/Email dispatch).
- New Claims Platform -> Telemetry & Monitoring: HTTPS/Native Diagnostics (Metrics and logs).

## Technology Stack
- Azure App Service & AKS: Container hosting for the new platform, chosen for rapid feature delivery despite limited cloud experience.
- .NET Core: Backend application framework for high performance and strong enterprise support.
- IBM z/OS & DB2: Legacy system of record retained per 3-year migration constraint.
- Azure Key Vault: Secret management for third-party API keys.
- Azure Application Insights: Managed observability to compensate for team's low cloud experience.

## Rationale
[The hybrid Azure-on-premises architecture decouples the modern web front-end from the rigid legacy mainframe, satisfying performance and security constraints. Incremental claim-type migration minimizes expensive mainframe changes while guaranteeing system consistency and zero data loss.]