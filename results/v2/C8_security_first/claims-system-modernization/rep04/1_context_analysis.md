## Overview
[This hybrid system gradually modernizes a legacy insurance claims platform by migrating claim types incrementally to Azure while the on-premise mainframe remains the system of record. It ensures continuous processing via an asynchronous architecture that decouples modern web applications from legacy mainframe latency.]

## Key Elements
* Customer / Policyholder (Person)
* Broker (Person)
* Claims Adjuster (Person)
* Modern Claims Platform (Azure Container Apps / App Service)
* Azure API Management (APIM) Gateway
* Legacy Mainframe System (On-Premises COBOL / DB2)
* Active Directory / Entra ID (Identity Provider)

## Relationships
* Customer/Broker/Adjuster -> Azure APIM Gateway via HTTPS / TLS 1.3
* Modern Claims Platform -> Azure APIM Gateway via internal HTTPS/REST
* Modern Claims Platform -> Legacy Mainframe via Asynchronous Message Queues / Secure File Drops over Azure ExpressRoute or IPsec VPN (mTLS)
* Modern Claims Platform -> Active Directory via OAuth 2.0 / OpenID Connect (Federated SSO)

## Technology Stack
* Azure (West Europe): Primary cloud provider hosting modern web applications and APIs, chosen for scalability despite the team's limited cloud experience.
* Azure API Management (APIM): Ingress gateway enforcing WAF policies, rate-limiting, and payload inspection.
* Terraform / Bicep: Infrastructure as Code (IaC) for declarative, pre-baked cloud deployments to prevent configuration drift.
* Azure Application Insights: Centralized observability and distributed tracing across the hybrid boundary.
* COBOL / DB2: Underlying legacy mainframe database and processing engine operating on-premise.

## Rationale
[An asynchronous anti-corruption layer isolates the modern Azure platform from legacy mainframe latency to meet the sub-2-second adjuster screen load requirement. A hybrid architecture with strict API gateways and secure VPN/ExpressRoute tunnels satisfies the security, compliance, and gradual incremental migration constraints without overhauling the immutable mainframe.]