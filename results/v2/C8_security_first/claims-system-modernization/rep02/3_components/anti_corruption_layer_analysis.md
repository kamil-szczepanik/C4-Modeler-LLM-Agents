## Overview
The system is an Insurance Claims Modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe claims system. It enables online claim submission and adjuster workflows in Azure while maintaining the legacy mainframe as the system of record.

## Key Elements
- Policyholders and Brokers: External users submitting claims online
- Claims Adjusters: Internal users managing claims in the web application
- Customer Portal: React SPA hosted in Azure Container Apps
- Adjuster Workspace: Node.js/Java application hosted in Azure Container Apps
- Anti-Corruption Layer (ACA Integration Service): Middleware container isolating the mainframe
- Internal Components: Routing Mediator, Domain Translator, Outbox Processor, DLQ Management, Telemetry Publisher
- Azure Service Bus: Messaging broker using AMQP
- On-Premises COBOL/DB2 Mainframe: Legacy system of record accessed via CICS Transaction Gateway

## Relationships
- Customer Portal -> Anti-Corruption Layer: Submits online claims [HTTPS/REST]
- Adjuster Workspace -> Anti-Corruption Layer: Manages claims [HTTPS/REST]
- Anti-Corruption Layer -> Azure Service Bus: Publishes and consumes events [AMQP]
- Routing Mediator -> Domain Translator: Forwards requests [gRPC]
- Domain Translator -> On-Premises COBOL/DB2 Mainframe: Translates and sends requests [Mutual TLS over Azure ExpressRoute / CICS Transaction Gateway]
- DLQ Management Component -> Azure Service Bus: Processes poisoned messages [AMQP]

## Technology Stack
- Azure Container Apps: Container hosting for cloud components chosen for managed simplicity given limited cloud experience
- Spring Cloud Gateway / .NET Yarp: Routing Mediator implementation for dynamic traffic steering and circuit breaking
- Apache Camel / custom mapping engine: Domain Translator for JSON to COBOL copybook mapping
- Azure Service Bus: Reliable messaging backbone enforcing transactional outbox and DLQ patterns
- Azure Key Vault: Secure credential storage for isolated service accounts
- OpenTelemetry & Azure Monitor: Centralized hybrid observability and business metric telemetry

## Rationale
This hybrid architecture safely decouples modern Azure cloud applications from the fragile legacy mainframe using an Anti-Corruption Layer. It guarantees business continuity, transactional consistency (R-04), and a rapid 1-day fallback per claim type (R-06) while respecting strict mainframe batch windows and cost constraints.