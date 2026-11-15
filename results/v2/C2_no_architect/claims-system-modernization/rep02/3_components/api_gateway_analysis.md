## Overview
[The system is a hybrid cloud insurance claims modernization platform that incrementally replaces a legacy mainframe with modern Azure services. Its core purpose is to migrate claim types gradually while ensuring zero data loss and maintaining uninterrupted operations.]

## Key Elements
- Policyholders and Brokers
- Claims Adjusters
- Compliance and Audit Officers
- Azure API Gateway
- Claims Web App (Azure AKS)
- Integration Service (Azure AKS)
- Claim Reconciliation Service (Azure AKS)
- Azure Cache for Redis
- Azure Service Bus
- COBOL/DB2 Mainframe (On-premises)
- Azure Active Directory / Entra ID

## Relationships
- Policyholders & Brokers -> Azure API Gateway: Claim submissions [HTTPS / TLS 1.3 via OAuth2/OIDC SSO]
- Claims Adjusters -> Azure API Gateway: Claims management [HTTPS / TLS 1.3 via OAuth2/OIDC SSO]
- Compliance & Audit Officers -> Azure API Gateway: Audit monitoring [HTTPS / TLS 1.3 via OAuth2/OIDC SSO]
- Azure API Gateway -> Claims Web App: Internal traffic routing [HTTPS with JWT validation]
- Claims Web App & Services -> COBOL/DB2 Mainframe: Legacy claims processing [SNA / IBM MQ / Batch]

## Technology Stack
- Azure API Gateway: Perimeter routing, WAF, schema validation, rate-limiting, and circuit-breaking
- Azure Kubernetes Service (AKS): Hosting modern microservices (.NET / React)
- Azure Service Bus: Asynchronous messaging for reliable claim reconciliation
- Azure Cache for Redis: Caching layer to meet the 2-second adjuster SLA
- Azure Active Directory / Entra ID: Single Sign-On integration
- Bicep / Terraform: Infrastructure-as-Code for routing and deployment management
- OpenTelemetry & Azure Monitor: Distributed tracing and observability

## Rationale
- This hybrid architecture isolates the expensive, risk-prone mainframe while enabling incremental claim type migration over three years. Configuration-driven routing and IaC ensure rapid rollbacks within one day if needed, compensating for the team's low cloud experience.