## Overview
This hybrid architecture gradually modernizes a legacy regional insurance claims system by decoupling online submission and adjuster interfaces from an on-premise mainframe. It balances low cloud team experience with strict consistency and performance requirements using managed Azure services and asynchronous integration patterns.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Finance & Compliance Auditors
- New Claims Platform (Azure West Europe)
- Azure Service Bus
- Enterprise Service Bus / Integration Gateway (On-premise)
- Legacy Mainframe COBOL/DB2 System of Record (On-premise)
- Insurer Active Directory (On-premise)

## Relationships
- Customers & Brokers → New Claims Platform (HTTPS / JSON): Online claim submission
- Claims Adjusters → New Claims Platform (HTTPS / HTML): Web application handling
- New Claims Platform ↔ Azure Service Bus (AMQP / HTTPS): Asynchronous event queuing
- Azure Service Bus ↔ Enterprise Service Bus (IPsec VPN / Azure ExpressRoute, TLS 1.3): Hybrid message transit
- Enterprise Service Bus → Legacy Mainframe (Managed File Transfer / MQ / APIs): Gradual data synchronization
- New Claims Platform → Insurer Active Directory (OIDC / OAuth2 via Entra ID Connect): Single sign-on and MFA

## Technology Stack
- Azure App Service: Container hosting for the New Claims Platform due to low cloud experience and managed PaaS simplicity
- Azure Service Bus: Asynchronous message broker to buffer events and protect against the 23:00-05:00 mainframe batch window
- Azure ExpressRoute / IPsec VPN: Secure hybrid network interconnect with mutual TLS (mTLS)
- OpenTelemetry & Azure Monitor: Distributed tracing and observability to monitor sub-2s adjuster screen performance and zero-loss consistency

## Rationale
The hybrid approach isolates expensive mainframe changes to at most once per quarter while migrating claim types individually. Asynchronous queuing and Azure-hosted UI buffering satisfy performance and consistency requirements without extending the rigid nightly batch window.