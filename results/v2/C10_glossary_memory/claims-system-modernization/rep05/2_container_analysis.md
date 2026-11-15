## Overview
The system is a cloud-based hybrid Modern Claims Platform that modernizes a regional insurer's 30-year-old legacy COBOL/DB2 mainframe claims system. It enables gradual claim type migration while ensuring business continuity and zero data loss.

## Key Elements
- End Customers and Brokers [person]
- Claims Adjusters [person]
- Migration Operations Managers [person]
- Customer Web Portal [container, SPA/React]
- Adjuster Web Application [container, Modular Monolith/.NET]
- Migration Operations Dashboard [container, Web App/.NET]
- Claims Core API Service [container, Modular Monolith/.NET]
- Claim Router & Integration Worker [container, .NET Worker Service]
- Modern Claims Platform [softwareSystem]
- Legacy Mainframe System [externalSystem]
- Corporate Active Directory / Entra ID [externalSystem]
- Integration Middleware / API Gateway [externalSystem]
- Azure Service Bus [container]

## Relationships
- End Customers and Brokers -> Customer Web Portal via HTTPS/REST
- Claims Adjusters -> Adjuster Web Application via HTTPS/REST
- Migration Operations Managers -> Migration Operations Dashboard via HTTPS/REST
- Modern Claims Platform -> Corporate Active Directory / Entra ID via OIDC/SAML
- Claim Router & Integration Worker -> Legacy Mainframe System via mTLS/VPN and signed JWT
- Claims Core API -> Azure Service Bus via AMQP

## Technology Stack
- Azure App Service: Hosts the modular monolith web applications and core APIs to reduce operational complexity
- Azure Static Web Apps: Hosts the React customer portal
- Azure Container Apps / App Service: Hosts the .NET Worker Service for asynchronous routing
- Azure Service Bus: Manages messaging, backpressure, dead-letter queues, and rate-limiting
- Azure Application Insights: Provides distributed tracing and observability across the hybrid boundary
- Azure Key Vault & Managed Identities: Secures credentials, secrets, and service-to-service authentication
- Bicep / Terraform: Automates Infrastructure-as-Code and blue-green deployments via Azure Deployment Slots

## Rationale
This hybrid architecture isolates asynchronous mainframe integration from synchronous web requests using a modular monolith and worker pattern, ensuring adjuster screens load in under two seconds despite slow legacy response times. Furthermore, per-claim-type feature flagging and versioned IaC pipelines guarantee the strict one-day emergency fallback and zero data loss requirements.