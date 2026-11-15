## Overview
This hybrid system gradually replaces a 30-year-old mainframe claims system with a modern cloud platform while maintaining legacy processing. It ensures zero data loss, low-latency UI performance, and rapid fallback capabilities during the 3-year migration.

## Key Elements
- Customers and Brokers
- Claims Adjusters
- Legacy Mainframe System (COBOL/DB2)
- Active Directory / Identity Provider
- Customer Portal (React/TypeScript SPA)
- Adjuster Web App (React/TypeScript SPA)
- Claims API Gateway (Azure API Management)
- Claims Core Services, Notification Service, Feature/Routing Service (Azure Container Apps)
- Integration / Anti-Corruption Layer (ACA Worker)
- Database (Azure SQL Database)
- Messaging (Azure Service Bus with DLQs)

## Relationships
- Customers/Brokers to Customer Portal via HTTPS/REST
- Claims Adjusters to Adjuster Web App via HTTPS/REST
- Customer Portal & Adjuster Web App to Claims API Gateway via HTTPS/REST (TLS 1.3, OAuth 2.0 / OIDC)
- API Gateway to Azure Container Apps via HTTPS/JSON
- Anti-Corruption Layer to Legacy Mainframe via mTLS over IPsec VPN / ExpressRoute
- Container Services to Azure Service Bus via AMQP

## Technology Stack
- Cloud Platform: Azure West Europe (Hybrid deployment)
- Compute: Azure Container Apps (chosen to reduce operational overhead for cloud-inexperienced team)
- Frontend: React / TypeScript hosted in Azure Static Web Apps
- API & Security: Azure API Management, Azure Key Vault, Managed Identities, OpenID Connect / OAuth 2.0
- Messaging & Database: Azure Service Bus, Azure SQL Database with transactional outbox pattern
- DevOps & Observability: GitHub Actions, OpenTelemetry, Azure Monitor

## Rationale
Azure Container Apps and Azure SQL Database simplify cloud operations for an inexperienced team while meeting strict security and performance requirements. Asynchronous messaging via Azure Service Bus and an Anti-Corruption Layer successfully isolate mainframe latency and guarantee zero data loss during hybrid migration.