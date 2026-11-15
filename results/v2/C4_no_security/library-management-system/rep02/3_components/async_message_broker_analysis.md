## Overview
The Library Management System is a comprehensive digital solution for public and academic libraries designed to catalogue items, manage circulation, and provide self-service patron portals. It operates under a strict EU-only data residency constraint while delivering high-performance search and real-time event processing.

## Key Elements
- **Async Message Broker**: Apache Kafka cluster deployed in EU-restricted Kubernetes nodes.
- **Topic Manager / Partition Coordinator**: Manages topic creation, partitioning, and leader election.
- **Event Log Storage Engine**: Handles append-only disk I/O and zero-copy network transfers with LUKS volume encryption.
- **Consumer Group Coordinator**: Manages offsets and rebalances using cooperative sticky assignors.
- **Schema Registry**: Confluent Schema Registry enforcing Apache Avro schema validation.
- **Producers & Consumers**: Core Domain Services and Notification Dispatcher.

## Relationships
- Core Domain Services -> Async Message Broker: Publishes validated domain events [Apache Kafka Protocol, HTTP/REST for Schema Validation]
- Async Message Broker -> Notification Dispatcher: Consumes events for time-sensitive notifications [Apache Kafka Protocol]
- Schema Registry -> Kafka Broker: Stores schemas in a compacted Kafka topic [Apache Kafka Protocol]

## Technology Stack
- **Apache Kafka**: JVM-based event streaming platform for reliable event distribution and durability.
- **Confluent Schema Registry**: Java-based registry for enforcing event data governance and schema evolution.
- **Strimzi Kubernetes Operator**: For managing EU-restricted Kafka deployments with persistent volume encryption.
- **Kafka TCP Protocol & HTTP/REST**: For message transmission and schema validation checks.

## Rationale
This architecture ensures low-latency event distribution and high reliability to meet strict notification SLAs and search performance goals. Simultaneously, EU-restricted deployment configurations and strict schema enforcement guarantee compliance with European data residency and privacy regulations.