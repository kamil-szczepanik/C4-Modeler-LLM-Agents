## Overview
[The Mainframe Integration Adapter bridges modern cloud applications with the legacy COBOL/DB2 mainframe using a hybrid Azure architecture. It securely routes and translates claims data while protecting the legacy system of record during the multi-year migration.]

## Key Elements
* COBOL Gateway Client (Java/Spring Integration TCP/IP adapter)
* Message Translator (Apache Camel)
* Resilience & Queue Manager (Resilience4j)
* Azure App Service Worker (Hosting infrastructure)
* Azure Service Bus (Message Broker)
* Legacy Mainframe (COBOL/DB2 System of Record)

## Relationships
* Claims Core Service -> Message Translator: Inbound commands via [Azure Service Bus / AMQP]
* COBOL Gateway Client -> Legacy Mainframe: Socket communication via [TCP/IP over Site-to-Site VPN with mTLS]
* Message Translator -> Azure Monitor: Audit logging via [HTTPS/TLS]
* COBOL Gateway Client -> Azure Key Vault: Credential retrieval via [Managed Identities / REST API]

## Technology Stack
* Java / Spring Integration: Chosen for robust TCP/IP socket handling in the COBOL Gateway Client.
* Apache Camel: Selected for dynamic, externalized copybook schema routing without container redeployments.
* Resilience4j: Implemented for strict retry policies, dead-lettering, and deduplication to ensure consistency (R-04).
* Azure Key Vault with Managed Identities: Used for secure, rotating access to mainframe RACF/ACF2 tokens without static credentials.
* Azure Service Bus: Deployed for asynchronous buffering to mitigate the 5-second mainframe latency constraint (R-05).

## Rationale
[This component-based architecture isolates brittle mainframe networking logic from business transformations while using asynchronous messaging to prevent performance bottlenecks. It satisfies strict constraints regarding legacy change limits and batch windows through stateless cloud design and secure hybrid networking.]