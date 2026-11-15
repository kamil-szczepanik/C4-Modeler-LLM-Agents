## Overview
The Mainframe Integration Adapter securely bridges the modern Azure-hosted adjuster platform with the on-premise COBOL/DB2 legacy mainframe. It translates modern data models into legacy formats while providing resilience against mainframe latency and batch constraints.

## Key Elements
- Adapter API Controller (Spring Boot, REST)
- Mainframe Translation Engine (Java, Apache Camel)
- Legacy Protocol Gateway (TCP/IP with mTLS)
- Integration Queue Router (Spring Integration / Azure Service Bus SDK)
- Azure Key Vault
- Azure Monitor / Microsoft Sentinel

## Relationships
- Adjuster Backend Service -> Adapter API Controller: Internal API [REST over HTTPS]
- Adapter API Controller -> Integration Queue Router: Asynchronous handover [AMQP]
- Adapter API Controller -> Mainframe Translation Engine: In-memory validation [Java]
- Integration Queue Router -> Mainframe Translation Engine: Event-driven dispatch [Internal]
- Mainframe Translation Engine -> Legacy Protocol Gateway: Internal routing [Direct]
- Legacy Protocol Gateway -> Legacy Mainframe: Secure legacy transport [TCP over mTLS via VPN/ExpressRoute]
- Mainframe Integration Adapter -> Azure Key Vault: Dynamic certificate injection [Managed Identity]
- Mainframe Integration Adapter -> Azure Monitor / Microsoft Sentinel: Telemetry and audit streaming [HTTPS]

## Technology Stack
- Java / Spring Boot / Spring Integration: Core framework for robust enterprise service integration and routing.
- Apache Camel: Efficient transformation between modern JSON and fixed-width EBCDIC/COBOL copybooks.
- Azure Container Apps: Container hosting platform providing automated scaling and integration with Azure virtual networks.
- Azure Service Bus: Enterprise messaging broker featuring Dead-Letter Queues to guarantee zero data loss (R-04).
- Azure Key Vault: Secure centralized repository for dynamic mTLS client certificates and private keys.

## Rationale
This architecture isolates fragile legacy systems from modern cloud services using protocol translation, asynchronous queuing, and circuit breakers. It meets stringent performance and consistency requirements despite high mainframe latency and strict batch window constraints.