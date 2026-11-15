## Overview
The Apache Kafka event streaming platform provides real-time data synchronization and immutable 10-year audit logging for the Clinic Management System across hybrid infrastructure. It ensures high availability, regulatory compliance, and seamless cross-region communication between clinical microservices and external systems.

## Key Elements
* Network Processor: Manages client TCP connections and inbound requests.
* Request Channel & KafkaRequestHandler Pool: Handles concurrency and request execution.
* Log Manager & LogSegment: Manages segment storage, NVMe local disks, and tiered object storage offloading.
* KRaft Metadata Quorum: Provides cluster coordination, controller election, and metadata consensus.
* Strimzi Operator: Automates Kubernetes lifecycle management, rolling upgrades, and pod anti-affinity.
* Cruise Control: Executes automated cluster rebalancing, self-healing, and workload redistribution.
* KafkaProducer & KafkaConsumer: Client libraries for application-level data publishing and consumption.

## Relationships
* Client Microservices -> Network Processor: Publishes and consumes audit events and streams via [TCP/TLS 1.3, mTLS].
* Kafka Brokers -> Tiered Object Storage: Offloads older log segments via [HTTPS/TLS].
* Kafka Brokers -> KRaft Quorum: Coordinates metadata consensus via [mTLS, TCP].
* On-Premises Kubernetes Cluster -> AWS eu-central-1: Replicates critical audit topics via [MirrorMaker 2, TLS 1.3].

## Technology Stack
* Apache Kafka: Selected as the core event backbone for high-throughput streaming and durability.
* Strimzi Operator: Chosen for declarative, native Kubernetes lifecycle management of Kafka clusters.
* KRaft Protocol: Replaces ZooKeeper for lightweight, scalable metadata quorum management.
* TLS 1.3 & mTLS: Mandated for secure, encrypted client-to-broker and inter-broker communications.
* Snappy Compression: Utilized to optimize cross-region bandwidth utilization.
* Tiered Storage & S3/Vault: Used to offload and encrypt long-term log segments for 10-year retention compliance.

## Rationale
This architecture guarantees 99.99% availability and zero data loss through rack-awareness and replication-factor=3 across hybrid boundaries. Furthermore, it satisfies strict HIPAA and GDPR mandates by enforcing mTLS, client-side envelope encryption, and immutable tiered storage.