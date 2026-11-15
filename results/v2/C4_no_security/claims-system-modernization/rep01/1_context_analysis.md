## Overview
[The system modernizes a 30-year-old regional insurer mainframe claims platform by introducing a cloud-based web application while keeping the legacy system as the primary data store. Core purpose is enabling gradual, risk-mitigated claim migration without disrupting ongoing operations or batch windows.]

## Key Elements
- Policyholders and Brokers (External Users)
- Claims Adjusters (Internal Users)
- New Claims Platform (Azure App Service, Azure Functions)
- Anti-Corruption Layer (ACL) Gateway
- Legacy Mainframe (IBM z/OS, COBOL, DB2)
- Microsoft Entra ID (Identity Provider)
- Azure Service Bus & Azure App Configuration

## Relationships
- Users to New Claims Platform via HTTPS/TLS for claim submission and adjuster workflows
- New Claims Platform to Microsoft Entra ID via OpenID Connect (OIDC) / OAuth 2.0 for Single Sign-On
- ACL Gateway to Legacy Mainframe via Asynchronous Messaging (Azure Service Bus) and Managed File Transfer (MFT)
- New Claims Platform to Azure App Configuration via REST API for feature flag evaluation

## Technology Stack
- Azure App Service & Azure Functions (PaaS/Serverless): chosen to offset the team's low cloud experience
- Microsoft Entra ID: enforces enterprise Single Sign-On and role-based access control (R-07)
- Azure Service Bus & Outbox Pattern: guarantees at-least-once message delivery and prevents data loss (R-04)
- Azure App Configuration: manages feature flags for instant 24-hour claim type rollbacks (R-06)
- OpenTelemetry & Azure Application Insights: provides distributed tracing for hybrid performance monitoring (R-05)

## Rationale
[The hybrid cloud architecture isolates modern user experiences from legacy latency using an Anti-Corruption Layer and asynchronous queues. This approach protects the immutable mainframe while meeting strict compliance, zero-data-loss, and rapid rollback mandates.]