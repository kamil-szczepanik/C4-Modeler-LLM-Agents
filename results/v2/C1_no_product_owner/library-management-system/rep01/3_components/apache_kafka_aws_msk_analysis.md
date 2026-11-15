## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within an EU-only data residency constraint. The architecture uses an event-driven model centered on Apache Kafka (AWS MSK) to meet high-performance search requirements.

## Key Elements
- **Zookeeper / KRaft Metadata Controller Quorum**: Manages cluster metadata and broker coordination.
- **Kafka Broker Nodes (Managed MSK)**: Stateless/Stateful message storage nodes handling partition leaders across 3 Availability Zones in Frankfurt (`eu-central-1`).
- **Schema Registry (AWS Glue / Managed)**: Enforces Avro schema validation for domain events.
- **Catalogue & Search Service, Circulation & User Service, Notification Worker Service**: Event producers and consumers.

## Relationships
- **Catalogue, Circulation, Notification Services -> Kafka Broker Nodes**: Publishes and consumes event streams via Apache Kafka Binary Protocol over TLS 1.3 [TCP Port 9094].
- **Kafka Broker Nodes -> Schema Registry**: Validates event schemas dynamically during serialization [HTTPS/REST over TLS].
- **Kafka Broker Nodes -> Zookeeper / KRaft Quorum**: Internal cluster state synchronization [TCP].

## Technology Stack
- **AWS MSK (Managed Streaming for Apache Kafka)**: Manages infrastructure while guaranteeing Frankfurt (`eu-central-1`) data residency.
- **TLS 1.3 & SASL/SCRAM / AWS IAM**: Enforces transport security, client authentication, and least-privilege topic ACLs.
- **Prometheus & Grafana**: Tracks consumer group lag and under-replicated partitions to protect performance SLAs.
- **Apache Avro**: Ensures schema consistency across domain events.

## Rationale
This architecture ensures 99th-percentile search responses under 800ms through decoupled, event-driven components. Furthermore, it strictly enforces EU-only data residency using Frankfurt-isolated AWS MSK, private VPC subnets, and customer-managed KMS encryption keys.