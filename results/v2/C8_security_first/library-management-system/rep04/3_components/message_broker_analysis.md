## Overview
[The Library Management System is a solution for public and academic libraries to catalogue items and manage circulation. It uses an Apache Kafka message broker to ensure asynchronous, fault-tolerant event-driven communication.]

## Key Elements
*   Message Broker: Apache Kafka
*   Producers: Core Circulation Service
*   Consumers: Notification Worker, Analytics Service
*   Internal Components: Kafka Broker Nodes, KRaft Controller Quorum, Schema Registry
*   Infrastructure: EU Kubernetes Cluster, EU Cloud Provider's HSM, Fluentbit Audit Logging Sidecar

## Relationships
*   Core Circulation Service -> Message Broker: Publishes circulation events [Kafka Protocol via TCP over TLS 1.3]
*   Message Broker -> Notification Worker: Consumes event messages for alerts [Kafka Protocol]
*   Message Broker -> Analytics Service: Consumes event messages for processing [Kafka Protocol]
*   Producers/Consumers -> Schema Registry: Fetches and validates Avro schemas [HTTPS]

## Technology Stack
*   Apache Kafka: Selected for distributed commit log architecture, at-least-once delivery, and configurable retention.
*   KRaft: Replaces ZooKeeper for cluster metadata coordination and streamlined Kubernetes deployment.
*   Avro / Schema Registry: Enforces payload contracts and backward compatibility.
*   TLS 1.3 / mTLS & SASL/SCRAM: Secures client authentication and data in transit.
*   AES-256: Encrypts data at rest via EU Cloud Provider's HSM to meet EU data residency constraints.

## Rationale
[Apache Kafka provides guaranteed low-latency event delivery required for real-time library self-service portals and circulation updates. Hardened Kubernetes deployment with strict replication and encryption satisfies performance goals and EU data residency constraints.]