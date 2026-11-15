## Overview
The Clinic Management System is an asynchronous, event-driven hybrid cloud platform designed to manage patient admissions, EMRs, scheduling, and billing while ensuring HIPAA/GDPR compliance and 99.99% availability. It securely decouples clinical and financial operations to guarantee uninterrupted patient care workflows.

## Key Elements
- KRaft Controller Quorum (Java/Scala)
- Kafka Broker (Apache Kafka runtime)
- Storage Tier Manager (Kafka LogSegments)
- Schema Registry (Confluent Schema Registry, Java)
- Strimzi Operator (Kubernetes)
- Tiered Storage (S3-compatible Storage)

## Relationships
- Clinical & Billing Services -> Kafka Broker: Publishes and consumes domain events [TCP / Kafka Protocol with SASL/TLS]
- Kafka Broker <-> KRaft Controller Quorum: Replicates cluster state [TCP]
- Kafka Broker -> Tiered Storage: Offloads historical log segments [HTTPS / S3 API]
- Kafka Broker <-> Schema Registry: Validates event schemas [HTTP/REST over TCP]

## Technology Stack
- Apache Kafka: Event-driven messaging broker for asynchronous service decoupling and high availability.
- KRaft Protocol: Replaces ZooKeeper for cluster metadata management and faster failovers.
- Confluent Schema Registry: Enforces Avro/Protobuf data contracts for long-term data governance.
- S3-compatible Tiered Storage: Satisfies the 10-year data retention mandate with AES-256 encryption.
- Strimzi Operator: Manages Kubernetes-native deployment across hybrid environments.

## Rationale
This event-driven architecture ensures 99.99% uptime and low-latency EMR performance by decoupling critical admission and billing services. Strict data contracts, encryption, and automated tiered storage integration satisfy rigorous HIPAA, GDPR, and 10-year retention mandates.