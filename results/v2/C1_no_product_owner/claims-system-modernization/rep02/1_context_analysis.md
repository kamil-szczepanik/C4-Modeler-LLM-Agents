## Overview
[The system is a hybrid cloud insurance claims modernization platform that gradually replaces a 30-year-old mainframe while ensuring continuous operations. Its core purpose is to enable modern online submissions and adjuster workflows while safely synchronizing data with the legacy system.]

## Key Elements
* Customers and Brokers
* Claims Adjusters
* New Insurance Platform (Azure West Europe, .NET, Azure Kubernetes Service)
* API Gateway / Edge Security (Azure WAF, TLS 1.3)
* Enterprise Integration Bus / MQ Gateway
* Legacy Mainframe (On-premises COBOL/DB2 system of record)
* Identity Provider (On-premises Active Directory / Entra ID with OIDC/SAML)
* Notification Service (External SaaS)
* Azure Key Vault

## Relationships
* Customers/Brokers -> API Gateway: HTTPS/REST for online claim submissions (R-01)
* Adjusters -> New Insurance Platform: HTTPS web UI interactions with anti-corruption layer (<2s load time, R-02, R-05)
* New Insurance Platform <-> Legacy Mainframe: Asynchronous messaging via MQ Gateway with mTLS and payload encryption (≤1 interface change/quarter)
* New Insurance Platform -> Identity Provider: OIDC/SAML with phishing-resistant MFA and OAuth2/JWT token propagation (R-07)
* New Insurance Platform -> Notification Service: HTTPS/API via dead-letter queues and circuit breakers

## Technology Stack
* Azure Kubernetes Service (AKS): Simplifies microservices management for a team with limited cloud experience
* Azure West Europe: Primary cloud region for the new platform
* .NET: Core application framework for backend services
* Azure Key Vault: Centralized secret management with automated rotation for hybrid credentials and mTLS certificates
* ArgoCD: GitOps deployment pipeline ensuring automated, configuration-drift-free deployments

## Rationale
[This hybrid architecture allows gradual migration of claim types over three years while respecting strict mainframe limits and nightly batch windows. It bridges the performance gap and ensures data consistency, low-risk rollbacks, and enterprise-grade security.]