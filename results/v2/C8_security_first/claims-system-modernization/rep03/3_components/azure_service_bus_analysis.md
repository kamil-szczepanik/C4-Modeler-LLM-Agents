## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old on-premises mainframe with a cloud-native Azure platform to handle customer claim submissions and adjuster workflows.]

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Legacy Mainframe System (COBOL/DB2)
- Azure Active Directory / Entra ID
- Azure API Gateway with Rate Limiter
- Customer Portal & Adjuster Web Apps (Azure Static Web Apps)
- Claim Management API, Claim Router/ACL, Audit & Reconciliation Service (Azure Container Apps, .NET 8)
- Azure Service Bus (Standard/Premium Tier)
- Azure SQL Database, Azure Key Vault, Azure App Configuration

## Relationships
- Customers & Brokers -> Customer Portal [HTTPS/TLS]: Submits online claims
- Claims Adjusters -> Adjuster Web Apps [HTTPS/TLS]: Handles claims via web UI
- Claim Management API -> Azure Service Bus Topics [AMQP over TLS with User-Assigned Managed Identities]: Publishes domain events
- Claim Router/ACL -> `mainframe-outbox` Queue [AMQP over TLS]: Buffers messages during batch windows
- Audit & Reconciliation Service -> DLQ Subscriptions [AMQP over TLS]: Consumes poisoned messages for analysis
- Azure Container Apps -> Azure Active Directory [OpenID Connect/OAuth 2.0]: Performs single sign-on

## Technology Stack
- Azure Service Bus: Core messaging broker providing publish-subscribe and FIFO session-enabled queues for decoupled migration
- .NET 8: Containerized microservices runtime for APIs and routers
- Azure Container Apps: Scalable hosting platform for backend services
- Azure SQL Database: Relational data store for modern claim records
- Bicep/Terraform: Infrastructure as Code for configuration consistency

## Rationale
[This hybrid architecture isolates expensive mainframe changes behind an Anti-Corruption Layer and Azure Service Bus, guaranteeing zero message loss during strict batch windows. It enables gradual claim type migration while accommodating the team's limited cloud experience.]