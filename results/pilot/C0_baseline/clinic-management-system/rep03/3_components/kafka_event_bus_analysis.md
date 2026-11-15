## Overview
The Kafka event bus acts as the asynchronous messaging backbone for the Clinic Management System, decoupling clinical operations from billing. It ensures real-time handoffs, audit logging, and high availability across hybrid cloud deployments.

## Key Elements
- Kafka Broker Cluster (Apache Kafka/KRaft via Strimzi)
- Confluent Schema Registry
- Kafka Connect
- Kafka Cruise Control
- MirrorMaker 2
- Core Clinical Services & Finance & Billing microservices

## Relationships
- Core Clinical Services -> Kafka Broker Cluster: Publishes clinical and scheduling events using Kafka Producer API [TCP/TLS, mTLS, SASL/SCRAM-512]
- Finance & Billing -> Kafka Broker Cluster: Consumes billing and claim events using Kafka Consumer API [TCP/TLS, mTLS, SASL/SCRAM-512]
- Kafka Broker Cluster -> Kafka Connect: Offloads audit trails to cold storage [TCP/TLS]
- On-Prem Kubernetes Cluster <-> AWS eu-central-1: Geo-replication and cross-domain transit [MirrorMaker 2 via mTLS]

## Technology Stack
- Apache Kafka (KRaft mode): Chosen for high-throughput, fault-tolerant event streaming without ZooKeeper dependencies.
- Confluent Schema Registry (Avro): Enforces strict data contracts for clinical payload validation and HIPAA compliance.
- Strimzi: Automates Kafka cluster management across hybrid on-prem Kubernetes and AWS environments.
- HashiCorp Vault: Manages secrets for Kafka Connect sink connectors to satisfy AES-256 encryption-at-rest mandates.
- Apache Ranger / Native ACLs: Implements fine-grained role-based access control and least-privilege topic partitioning.

## Rationale
This event-driven architecture guarantees 99.99% availability and sub-second EMR responsiveness through asynchronous decoupling. It enforces strict HIPAA and GDPR compliance using client-side envelope encryption, mTLS transport security, and compact topics with tombstones for data expungement.