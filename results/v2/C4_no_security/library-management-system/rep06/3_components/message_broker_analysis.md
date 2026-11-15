## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals for academic and public libraries. It uses an event-driven architecture to offload background tasks and maintain high performance.

## Key Elements
- **Library Patrons, Staff, Clerks, Administrators**: End-users of the system.
- **API Gateway (Kong / NGINX)**: Manages incoming traffic.
- **Self-Service Portal & Staff Dashboard (React / TypeScript)**: Frontend interfaces.
- **Core API Application (Spring Boot / Java)**: Handles business logic and publishes events.
- **Search Engine (OpenSearch)**: Handles item catalog searches.
- **Primary Database (Managed PostgreSQL)**: Persists relational application data.
- **Message Broker (Apache Kafka)**: Manages asynchronous event streams via components: Event Log Manager, Topic Router, Schema Registry, Consumer Group Coordinator, and Access Control & Auth Module.
- **Async Workers (Spring Boot / Java)**: Consumes asynchronous events for background processing.
- **External Systems**: Payment Gateway, LDAP/IdP, Digital Content Providers, Notification Service, Log Aggregator, APM Tool.

## Relationships
- Core API Application -> Message Broker: Publishes asynchronous events [Kafka binary protocol over TCP, TLS]
- Async Workers -> Message Broker: Consumes asynchronous events [Kafka binary protocol over TCP, TLS]
- Message Broker -> APM and Synthetic Monitoring Tool: Exports JMX metrics [TCP]
- Core API Application & Async Workers -> Access Control & Auth Module: Authenticates via SASL/SCRAM and TLS client certificates [TLS]

## Technology Stack
- **Apache Kafka**: Chosen for the Message Broker to provide durable, partitioned commit logs, strict EU-only data residency, and high-throughput messaging.
- **Spring Boot / Java**: Powers the Core API Application and Async Workers for robust backend processing.
- **Avro & Schema Registry**: Enforces backward-compatible event schemas between producers and consumers.
- **Kubernetes (HPA)**: Scales Async Workers dynamically based on consumer lag thresholds.

## Rationale
This architecture ensures 99th-percentile search responses under 800 ms by offloading heavy background tasks from the synchronous request path. Apache Kafka with a replication factor $\ge 3$ guarantees reliable message delivery, zero data loss, and EU-only data residency compliance.