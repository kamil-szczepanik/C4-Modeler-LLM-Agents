## Overview
[The Insurance Claims Platform modernizes a legacy COBOL/DB2 mainframe claims system by gradually migrating claim types while maintaining continuous operations. It bridges the hybrid boundary using an enterprise-grade Anti-Corruption Layer with robust event streaming and circuit breaking.]

## Key Elements
*   [Core Claims Service (Azure Container Apps)]
*   [Mainframe Anti-Corruption Layer (Azure Event Hubs / Kafka)]
*   [Ingress Event Router (Kafka Connect / Azure Functions)]
*   [Schema & State Registry (Confluent Schema Registry)]
*   [Protocol Adapter (Apache Camel)]
*   [Legacy COBOL/DB2 Mainframe]
*   [Operational Observability & Dead-Letter Container]

## Relationships
*   [Core Claims Service -> Ingress Event Router: Publishes JSON CloudEvents via Azure Event Hubs]
*   [Ingress Event Router -> Schema & State Registry: Validates payloads via Confluent Schema Registry]
*   [Schema & State Registry -> Protocol Adapter: Dispatches validated transformation payloads]
*   [Protocol Adapter -> Legacy COBOL/DB2 Mainframe: Transmits data via IBM MQ and SFTP over Azure ExpressRoute with mTLS and envelope encryption]
*   [Protocol Adapter -> Operational Observability & Dead-Letter Container: Routes poison pills to DLQ with automated PII masking]

## Technology Stack
*   [Azure Event Hubs (Kafka): Asynchronously decouples modern platform from legacy mainframe]
*   [Kafka Connect: Minimizes custom integration code for team with low cloud experience]
*   [Confluent Schema Registry: Enforces data contracts to limit mainframe changes to max one per quarter]
*   [Apache Camel: Provides enterprise integration patterns, circuit breaking, and retry logic]
*   [Azure Key Vault: Manages legacy service credentials dynamically via managed identities]

## Rationale
[This hybrid architecture isolates rigid mainframe legacy dependencies using bounded event-driven patterns and strict schema contracts. It guarantees zero claim loss, supports rapid daily rollbacks, and respects strict batch windows while upskilling a low-experience cloud team through managed services.]