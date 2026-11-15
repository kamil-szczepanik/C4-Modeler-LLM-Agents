## Overview
The Managed Event Bus handles asynchronous event streaming and change data capture for the Library Management System. It ensures reliable, secure communication across internal microservices while maintaining strict EU data residency compliance.

## Key Elements
- Event Broker Engine: Apache Kafka via Strimzi operator on Kubernetes
- Schema Registry: Confluent Schema Registry
- Connectors: Kafka Connect with Debezium
- Management: Topic Management Operator
- Consumers: Notification Service, Search Service
- Producers: Core Domain Service, PostgreSQL Database

## Relationships
- Core Domain Service -> Managed Event Bus: Publishes and consumes domain events [TLS-encrypted TCP, SASL/OAuth2]
- Core Domain Service -> Kafka Connect: Emits database transaction logs [JDBC/TLS]
- Notification Service -> Managed Event Bus: Consumes domain events for patron alerts [TLS-encrypted TCP, SASL/OAuth2]
- Search Service -> Managed Event Bus: Consumes catalogue mutation events for synchronization [TLS-encrypted TCP, SASL/OAuth2]
- Topic Management Operator -> Event Broker Engine: Provisions and configures topics and ACLs [Kubernetes API]

## Technology Stack
- Apache Kafka: Chosen over AWS EventBridge for strict EU-only data residency and sovereignty guarantees
- Strimzi Operator: Enables declarative Kubernetes-native management of Kafka clusters and topics
- Confluent Schema Registry: Enforces payload validation and backward compatibility using Avro/JSON
- Kafka Connect (Debezium): Implements reliable change data capture for outbox pattern delivery
- Prometheus: Monitors consumer lag, connector health, and broker metrics

## Rationale
This architecture guarantees strict EU data residency via sovereign Kubernetes deployments while preventing distributed transaction failures through CDC and the outbox pattern. Fine-grained RBAC, encryption, and automated schema enforcement ensure enterprise-grade security and system availability.