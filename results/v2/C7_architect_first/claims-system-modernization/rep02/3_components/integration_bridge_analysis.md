## Overview
[The system is a Hybrid Cloud Insurance Claims Modernization Platform that gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure-based platform. Its core purpose is to enable online claims processing while ensuring zero data loss and maintaining business continuity.]

## Key Elements
* Integration Bridge (Apache Camel / Azure Integration Services Container)
* Route Orchestrator (Apache Camel Core Component)
* Mainframe Adapter Component
* Dead Letter Queue (DLQ) Handler Component
* Circuit Breaker & Rate Limiting Component
* Fallback Routing Switch Component
* Key Vault Secrets Provider Component
* Reconciliation & Business Dashboard Adapter Component
* On-Premises COBOL/DB2 Mainframe
* Azure Service Bus
* Azure Key Vault

## Relationships
* Claims Processing Service -> Route Orchestrator: Sends asynchronous messages [Azure Service Bus]
* Route Orchestrator -> Mainframe Adapter: Internal routing [Direct VM / In-Memory]
* Mainframe Adapter -> On-Premises COBOL/DB2 Mainframe: Secure legacy communication [TCP/IP via mTLS over IPsec VPN/ExpressRoute]
* Key Vault Secrets Provider -> Azure Key Vault: Dynamically fetches credentials and secrets [HTTPS / Managed Identity]
* DLQ Handler -> Notification Service: Triggers business exception alerts [REST API]

## Technology Stack
* Apache Camel: Selected for enterprise integration patterns, message transformation (JSON to EBCDIC), and routing.
* Azure Service Bus: Used for reliable asynchronous messaging between microservices and the Integration Bridge.
* Azure Key Vault: Utilized with Managed Identities for secure storage and dynamic hot-reload of mTLS certificates and legacy credentials.
* Resilience4j: Implemented via Camel for circuit breaking and backpressure to protect the legacy mainframe.
* OpenTelemetry: Deployed for distributed tracing across the hybrid Azure-on-premises boundary.

## Rationale
[This architecture successfully bridges modern cloud services with a rigid legacy mainframe while adhering to strict constraints like minimal mainframe changes and zero data loss. It ensures high maintainability, allowing rapid fallback per claim type and robust security via hybrid networking and managed credentials.]