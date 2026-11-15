## Overview
The Apache Kafka StatefulSet provides high-throughput event sourcing, asynchronous messaging, and streaming data infrastructure for the Clinic Management System. It ensures resilient, decoupled communication across microservices while meeting strict HIPAA, GDPR, and 10-year data retention requirements.

## Key Elements
- KRaft Controller Component
- Kafka Broker Engine
- Schema Registry (Confluent Schema Registry)
- Kafka Connect Components
- Authorizer Component (Native ACL / Apache Ranger)
- Cruise Control Component
- Metrics Exporter (Prometheus JMX Exporter)
- Tiered Storage Plugin
- MirrorMaker 2 Component
- Data Governance and Masking Interceptor
- Dead Letter Queue (DLQ) Management Engine
- Client Connection Multiplexer (Envoy proxy sidecars)
- Log Compaction and Segment Manager
- Backup and Snapshot Controller
- Health Check and Cluster Operator (Strimzi-based)
- Audit Logging Interceptor

## Relationships
- Patient & EMR Service -> Kafka Broker Engine: Publishes and consumes domain events [Asynchronous Messaging / Kafka Protocol]
- Schema Registry -> Microservices: Enforces Avro payload validation [HTTP/REST]
- Kafka Connect & Tiered Storage Plugin -> MinIO Object Storage Gateway: Offloads cold logs and streams [S3/HTTPS]
- MirrorMaker 2 -> Hybrid VPN Gateway: Replicates transaction streams across on-prem and cloud [Encrypted TCP]
- Metrics Exporter -> Observability Collector: Bridges telemetry data [OpenTelemetry / Prometheus]
- Audit Logging Interceptor -> Audit & Compliance Sidecar: Streams compliance logs [Internal IPC]

## Technology Stack
- Apache Kafka: Event streaming platform providing partition fault tolerance and replication.
- KRaft Consensus Protocol: Replaces ZooKeeper for streamlined, decentralized metadata quorum management.
- Confluent Schema Registry: Enforces strict Avro payload validation and backward compatibility.
- TLS 1.3 & SASL/SCRAM-SHA-512: Secures data in transit and inter-broker authentication.
- Prometheus JMX Exporter: Scrapes JVM and broker performance metrics.
- Strimzi-based Operator: Automates cluster operations and failover handling on Kubernetes.

## Rationale
The KRaft-based Kafka architecture eliminates single points of failure while supporting active-active multi-region replication via MirrorMaker 2 to satisfy 99.99% availability. Tiered storage and strict encryption interceptors ensure HIPAA and GDPR compliance alongside cost-effective 10-year data retention.