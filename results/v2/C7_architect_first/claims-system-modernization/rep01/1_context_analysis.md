## Overview
The system is a hybrid Modern Claims Platform built on Azure that incrementally replaces a 30-year-old on-premise mainframe system. Its core purpose is to modernize customer submissions and adjuster workflows while keeping the legacy COBOL/DB2 system as the system of record.

## Key Elements
* Modern Claims Platform (Azure Container Apps / PaaS)
* Mainframe Claims System (IBM z/OS, COBOL, DB2)
* Hybrid Integration Gateway (Azure ExpressRoute, mTLS, IPsec VPN)
* Azure Service Bus & Azure API Management (APIM)
* Corporate Active Directory
* External Payment Gateway
* External Actors: Customers, Brokers, and Claims Adjusters

## Relationships
* Customers and Brokers interact with the Modern Claims Platform via HTTPS / TLS 1.3 (R-01).
* Adjusters utilize the Modern Claims Platform web application with asynchronous caching to meet <2s load times (R-02, R-05).
* The Modern Claims Platform synchronizes data with the Mainframe Claims System via Azure Service Bus and Hybrid Integration Gateway.
* The platform authenticates users against Corporate Active Directory using OIDC / OAuth2 (R-07).
* The platform integrates with the External Payment Gateway for automated claim payouts.

## Technology Stack
* Azure West Europe: Cloud provider region hosting the modern microservices architecture.
* Azure Container Apps / PaaS: Compute platform for running the modern claims web applications.
* Azure Service Bus: Asynchronous messaging to decouple cloud services from the mainframe batch window constraints.
* Azure API Management (APIM) & Azure Key Vault: Secure API gateway proxy and managed secrets management using Managed Identities.
* ExpressRoute, mTLS, IPsec: Hybrid networking and transport security protocols bridging Azure and on-premise infrastructure.
* IBM z/OS, COBOL, DB2: Legacy on-premise system of record.

## Rationale
The hybrid architecture allows gradual, risk-managed migration of claim types one-by-one while insulating the constrained mainframe from real-time traffic spikes. Asynchronous messaging and managed Azure services mitigate the team's limited cloud experience while guaranteeing data consistency and strict one-day rollback capabilities.