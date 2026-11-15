## Overview
[This system modernizes a regional insurer's legacy COBOL/DB2 mainframe claims platform by introducing a hybrid cloud architecture using Azure. It enables online claim submissions and adjuster workflows while maintaining zero claim loss and compliance standards.]

## Key Elements
- Policyholders and Brokers
- Claims Adjusters
- Compliance and Audit Officers
- COBOL/DB2 Mainframe
- Azure Active Directory / Entra ID
- Claims Web App (Azure AKS, ASP.NET Core / React)
- Integration Service (Azure AKS, .NET)
- Claim Reconciliation Service (Azure AKS, .NET)
- Azure Cache for Redis
- Azure Service Bus

## Relationships
- Claims Web App -> Azure Service Bus: Asynchronous message queueing for claim submissions [AMQP]
- Claims Web App -> Azure Active Directory: Single sign-on authentication [OIDC / OAuth 2.0]
- Integration Service -> COBOL/DB2 Mainframe: Synchronize claim data [HTTPS / TCP]
- Claims Adjusters -> Claims Web App: Handle claim types [HTTPS]

## Technology Stack
- Azure Service Bus: Asynchronous messaging with Topics, Subscriptions, and DLQ governance for decoupling and reliable claim ingestion
- Azure AKS (Kubernetes): Container orchestration for modern microservices with automated scaling
- ASP.NET Core & React: Modern web application framework for high-performance adjuster screens
- Azure Cache for Redis: In-memory caching layer to optimize UI response times under 2 seconds
- Azure Active Directory / Entra ID: Enterprise single sign-on and identity management
- Terraform / Bicep: Infrastructure-as-Code for consistent hybrid environment deployments

## Rationale
[This hybrid architecture decouples modern cloud ingestion from the legacy mainframe, satisfying the 3-year migration constraint and strict performance SLAs. It ensures zero claim loss and rapid rollback capabilities via Azure Service Bus routing and idempotent microservices.]