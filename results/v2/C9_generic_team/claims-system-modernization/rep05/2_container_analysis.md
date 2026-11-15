## Overview
[The system is a hybrid cloud-based Insurance Claims Modernization platform that gradually replaces a legacy COBOL/DB2 mainframe. Its core purpose is to enable online submissions and streamlined adjuster workflows while ensuring continuous synchronization with the legacy system of record.]

## Key Elements
- Customers and Brokers (Users)
- Claims Adjusters (Users)
- COBOL/DB2 Mainframe (External System of Record)
- API Gateway Container
- Customer BFF Container and Adjuster BFF Container
- Modular Monolith Container (Azure)
- Anti-Corruption Layer (ACL) Container
- Routing / Feature Flag Container
- Data Sync / Reconciliation Container
- Asynchronous Messaging & Caching Layer (Azure Service Bus and Redis)
- IAM Proxy / Token Exchange Container
- Observability & Logging Container (Azure Application Insights)
- Configuration & Secrets Management Container (Azure Key Vault)

## Relationships
- Customers/Brokers interact with Customer BFF via HTTPS (TLS 1.3)
- Claims Adjusters interact with Adjuster BFF via HTTPS (TLS 1.3)
- BFFs communicate with API Gateway via internal HTTPS/REST
- API Gateway routes traffic through Routing/Feature Flag Container to Modular Monolith via internal REST/gRPC
- Modular Monolith communicates with COBOL/DB2 Mainframe via Anti-Corruption Layer (ACL) over secure VPN/TLS
- Modular Monolith utilizes Azure Service Bus (AMQP) for async processing and Redis for caching
- IAM Proxy integrates with insurer's Active Directory via SAML/OAuth2/OIDC
- Observability layer collects telemetry from all Azure containers

## Technology Stack
- Azure West Europe: Primary cloud region for new platform components
- Azure App Service / Container Apps: Hosting environment for modular monolith and BFFs
- Azure Service Bus & Redis: Asynchronous messaging and caching to mitigate 5s mainframe latency
- Azure Application Insights: Centralized observability, distributed tracing, and synthetic monitoring
- Azure Key Vault: Centralized configuration and secrets management
- Azure DevOps / GitHub Actions: CI/CD automation and Infrastructure-as-Code (IaC)

## Rationale
[A hybrid Strangler Fig pattern with a modular monolith minimizes risk for a team with limited cloud experience while isolating complex legacy dependencies. Asynchronous caching and BFFs guarantee sub-2-second UI performance, and the ACL ensures strict 1-day rollbacks.]