## Overview
The Apache Kafka event streaming broker provides asynchronous, decoupled communication for the Clinic Management System to ensure high availability and HIPAA/GDPR compliance. It manages clinical, billing, and audit event streams across hybrid on-premise Kubernetes and AWS (eu-central-1) environments.

## Key Elements
- **KRaft Controller Quorum**: Java-based ZooKeeper-less metadata management for cluster consensus.
- **Kafka Brokers**: Java/Netty-based brokers handling client connections, partition log replication, and disk I/O.
- **Kafka Connect**: Java framework for offloading historical data to long-term storage.
- **Kafka Streams Engine**: Java Kafka Streams API handling stateful routing, retries, and dead-letter queues.
- **Core Services, EMR Service, & Integration Service**: Producer/consumer microservices.

## Relationships
- **Microservices to Kafka Brokers**: Produce and consume events via TCP using TLS 1.3 and SASL/SCRAM-SHA-512.
- **Kafka Connect to ClickHouse / Object Storage**: Exports historical audit and clinical event topics via HTTP/JDBC.
- **KRaft Controllers to Kafka Brokers**: Manages cluster metadata and consensus.

## Technology Stack
- **Apache Kafka (Java / Netty)**: Core event streaming platform chosen for high throughput and fault tolerance.
- **KRaft Mode**: Eliminates ZooKeeper dependencies to streamline metadata management and support 99.99% availability.
- **Kafka Connect**: Offloads long-term data to prevent broker disk bloat and meet 10-year retention rules.
- **Kafka Streams**: Enables stateful routing for dead-letter queues and automated retry topics.
- **TLS 1.3, mTLS, & SASL/SCRAM-SHA-512**: Secures all client-to-broker and inter-broker communications.
- **AES-256**: Encrypts storage volumes and log segments at rest to satisfy security mandates.

## Rationale
This architecture ensures 99.99% uptime and high availability by decoupling critical patient workflows from external system outages. Furthermore, it securely enforces HIPAA and GDPR compliance through robust encryption, strict ACL isolation, and automated long-term data archiving.