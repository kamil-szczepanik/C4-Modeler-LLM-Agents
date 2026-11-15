## Overview
The system is an Insurance Claims Modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native Azure architecture. It uses a hybrid integration adapter to synchronize legacy batch data while ensuring zero claim loss and strict compliance with operational windows.

## Key Elements
* MQ Message Listener Component (Spring JMS)
* Data Transformation Component (Apache Camel)
* Schema Validation Sub-component (JSON Schema Validator)
* Outbound Dispatcher Component (Azure Service Bus SDK)
* Adapter Health & Audit Monitor Component (Micrometer / OpenTelemetry)
* Retry & Dead-Letter Manager Component (Spring Retry / IBM MQ DLQ handler)

## Relationships
* Legacy Mainframe -> MQ Message Listener: Dumps batch extracts [IBM MQ binary]
* Data Transformation -> Schema Validation: Validates JSON payload [In-memory]
* Schema Validation -> Outbound Dispatcher: Valid payload [In-memory]
* Outbound Dispatcher -> Data Sync Worker (Container): Sends stream [AMQP 1.0 via Azure ExpressRoute]
* Data Sync Worker -> Outbound Dispatcher: Sends processing ACKs [AMQP via Azure Service Bus]
* Outbound Dispatcher -> MQ Message Listener: Confirms successful delivery [JMS commit]
* Retry & Dead-Letter Manager -> MQ Message Listener: Re-queue or poison-message routing [IBM MQ API]

## Technology Stack
* Spring JMS: Consumes and manages IBM MQ messages on-premises reliably
* Apache Camel: Translates legacy EBCDIC fixed-length records into JSON domain events
* JSON Schema Validator: Intercepts malformed records before cloud transmission
* Azure Service Bus SDK: Securely routes transformed events to the cloud via AMQP 1.0
* Micrometer / OpenTelemetry: Emits health telemetry and audit metrics locally

## Rationale
This architecture isolates brittle EBCDIC parsing and network transport to protect the strict nightly batch window (23:00-05:00). A closed-loop ACK and retry mechanism guarantees at-least-once delivery semantics without requiring expensive changes to the legacy mainframe.