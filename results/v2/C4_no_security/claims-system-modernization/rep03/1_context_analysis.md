## Overview
[The system modernizes a regional insurer's 30-year-old COBOL/DB2 mainframe claims platform by introducing a hybrid cloud application. It enables incremental claim-type migration while ensuring zero data loss and maintaining legacy system-of-record operations.]

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Business Operations / Compliance Officers
- New Claims Platform (Azure West Europe)
- Legacy Mainframe (On-premise COBOL/DB2)
- Insurer's Active Directory / Azure AD
- Payment Gateway (Third-party SaaS)
- Notification Service (Email/SMS provider)

## Relationships
- Customers & Brokers -> New Claims Platform: HTTPS (Web/Mobile UI)
- Claims Adjusters -> New Claims Platform: HTTPS (Web App < 2s load time)
- New Claims Platform <-> Legacy Mainframe: Asynchronous messaging via Azure Service Bus and ESB
- New Claims Platform -> Payment Gateway: HTTPS/REST (Claim settlements)
- New Claims Platform -> Notification Service: HTTPS/API (Customer alerts)
- New Claims Platform -> Insurer's Active Directory: OIDC/OAuth2 (Single Sign-On)

## Technology Stack
- Microsoft Azure West Europe: Cloud provider chosen for managed services and team enablement.
- Azure Landing Zones: Enforces security compliance to compensate for low cloud experience.
- Azure Service Bus: Asynchronous event-driven messaging with outbox pattern for data consistency.
- Azure Monitor & OpenTelemetry: End-to-end distributed tracing and audit logging.
- GitHub Actions / Azure DevOps: CI/CD pipelines enabling the 1-day migration rollback requirement.

## Rationale
[The hybrid event-driven architecture insulates the modern Azure UI from legacy mainframe latencies to meet strict performance targets. Using managed Azure services bridges the team's cloud skill gap while guaranteeing financial consistency and rapid rollback capabilities.]