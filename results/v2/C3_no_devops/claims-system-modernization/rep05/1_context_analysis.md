## Overview
[The hybrid system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern Azure-hosted platform while maintaining uninterrupted legacy operations.]

## Key Elements
* Personas: Customers, Brokers, Claims Adjusters, Migration Operations Managers.
* Core Systems: Modern Claims Platform (Azure West Europe), Legacy Mainframe (On-Premises), Integration/Anti-Corruption Layer (ACL).
* External Systems: Active Directory, Notification Service, Payment Gateway.
* Containers: Web Application, API Gateway, Microservices, Azure Service Bus, Azure Key Vault.

## Relationships
* Customers/Brokers to Modern Claims Platform: HTTPS/REST for online claim submission.
* Claims Adjusters to Modern Claims Platform: HTTPS/REST for claim management.
* Modern Claims Platform to Active Directory: OAuth2/OIDC via Azure API Management for single sign-on.
* Modern Claims Platform to Legacy Mainframe: Secure API calls through the Anti-Corruption Layer (ACL).
* Modern Claims Platform to Notification Service: Asynchronous event-driven messaging via Azure Service Bus.
* Modern Claims Platform to Payment Gateway: Synchronous HTTPS/REST with idempotency keys.

## Technology Stack
* Cloud Provider: Hybrid (Azure West Europe and On-Premises).
* Compute & Architecture: Azure managed PaaS microservices to accommodate team's low cloud experience.
* Integration: Azure Service Bus for asynchronous messaging and ACL for mainframe decoupling.
* Security & Identity: Azure Active Directory (OIDC/OAuth2), Azure Key Vault for secret management, TLS 1.3, and IPsec VPN with mTLS.

## Rationale
[This hybrid architecture isolates expensive mainframe dependencies via an Anti-Corruption Layer, protecting the rigid batch window and ensuring zero claim loss. Furthermore, managed Azure PaaS services simplify cloud adoption for an inexperienced team while meeting strict security and performance requirements.]