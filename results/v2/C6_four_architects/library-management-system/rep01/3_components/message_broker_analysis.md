## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It utilizes an event-driven architecture to guarantee EU-only data residency and sub-800ms search performance.

## Key Elements
* Patrons and Librarians (Users)
* EU-Tenant Identity Provider (IdP)
* EU-Hosted Payment Gateway
* Notification Service (Email/SMS)
* Digital Content Repository / DRM Provider
* Web Application (SPA) [React, Nginx]
* API Gateway [Spring Cloud Gateway, Java]
* Core Domain Service [Spring Boot, Java]
* Search Service [OpenSearch]
* Notification & Payment Worker / DRM Worker [Python, Celery]
* Message Broker [Apache Kafka (KRaft Mode)]
* Caching Layer [Redis]
* Database [PostgreSQL]
* Message Broker Components: Kafka Broker Engine, Topic Manager, Schema Registry [Confluent Schema Registry], Producer/Consumer Connection Manager, Log Compaction & Storage Engine, Partition Replicas Manager, Metrics & Health Exporter [Prometheus/HTTP], ACL Authorizer

## Relationships
* Core Domain Service -> Message Broker: Publishes domain events [Apache Kafka]
* Message Broker -> Search Service: Consumes events to update search index [Apache Kafka]
* Message Broker -> Notification & Payment Worker / DRM Worker: Consumes asynchronous task events [Apache Kafka]
* Core Domain Service -> Schema Registry: Validates event schemas [HTTP/REST]
* Kafka Broker Engine -> Topic Manager: Provisions partitioned event logs [TCP]
* Core Domain Service & Workers -> Kafka Broker Engine: Publishes/Consumes domain events and tasks [TCP/SASL_SSL]
* Kafka Broker Engine -> Schema Registry: Caches and validates event schemas at runtime [HTTP/REST]
* Kafka Broker Engine -> Log Compaction & Storage Engine: Persists and flushes event logs to local storage [POSIX I/O]
* Kafka Broker Engine -> Partition Replicas Manager: Synchronizes partition state and ISR [TCP]
* Kafka Broker Engine -> Metrics & Health Exporter: Feeds internal broker telemetry [In-memory]
* Producer/Consumer Connection Manager -> ACL Authorizer: Validates topic-level produce/consume permissions [In-memory]

## Technology Stack
* Apache Kafka (KRaft Mode): Eliminates ZooKeeper dependencies and handles event-driven decoupled communication.
* Confluent Schema Registry: Enforces payload contracts (Avro/JSON Schema) for backward compatibility.
* Spring Boot & Spring Cloud Gateway: Powers core domain logic and API routing.
* OpenSearch: Fulfills sub-800ms search performance requirements.
* Python/Celery: Executes asynchronous notifications, payments, and DRM workflows.
* Prometheus: Monitors broker telemetry and consumer lag.

## Rationale
The event-driven Kafka architecture guarantees strict EU data residency via isolated clusters and SASL/TLS boundaries. Component-level replication and log compaction ensure high availability and sub-800ms search response times.