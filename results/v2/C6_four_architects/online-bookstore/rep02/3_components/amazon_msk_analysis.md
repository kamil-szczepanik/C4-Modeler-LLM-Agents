## Overview
- An event-driven, scalable online bookstore built on AWS to support 1 million monthly active users globally.
- Features multi-currency transactions, secure checkout, real-time recommendations, and GDPR/CCPA compliance.

## Key Elements
- **Broker Nodes**: Apache Kafka Brokers running in Apache KRaft mode for message ingestion and replication.
- **Schema Registry**: Confluent/AWS Glue Schema Registry for Avro/JSON event validation.
- **Kafka Connect**: AWS MSK Connect for syncing stream data to DynamoDB and Aurora.
- **Client Authentication & Authorization Manager**: AWS IAM and SASL/SCRAM for ACL enforcement.
- **Cluster Monitoring & Metrics Exporter**: Amazon CloudWatch and Prometheus for telemetry.
- **Topic & Partition Manager**: Kafka Admin Client API for topic provisioning and retention.
- **Internal Storage Volumes**: Amazon EBS gp3 attached to broker nodes for persistent storage.

## Relationships
- Core E-Commerce Service & Notification Worker -> Broker Nodes: Publishes/consumes events [Kafka protocol over TLS]
- Core E-Commerce Service -> Schema Registry: Validates payloads [HTTP/REST over TLS]
- Broker Nodes -> Schema Registry: Validates event schemas [HTTP/REST]
- Core E-Commerce Service & Notification Worker -> Client Authentication & Authorization Manager: Authenticates connections [IAM / SASL over TLS]
- Broker Nodes -> Cluster Monitoring & Metrics Exporter: Emits telemetry [Prometheus metrics / AWS CloudWatch]
- Topic & Partition Manager -> Broker Nodes: Manages topic configurations [Kafka Admin Protocol over TLS]
- Broker Nodes -> Internal Storage Volumes: Persists event streams [NVMe/EBS block storage interface]
- Broker Nodes -> Recommendation Engine: Streams clickstream and order events [Kafka protocol over TLS]
- Broker Nodes -> AWS Glue & Athena: Streams transactional audit data via S3 sink connectors [HTTPS]

## Technology Stack
- **Amazon MSK (Apache Kafka)**: Chosen for high-throughput, fault-tolerant event streaming.
- **Apache KRaft**: Eliminates ZooKeeper dependencies to reduce operational complexity and improve metadata scalability.
- **Amazon EBS gp3**: Provides cost-effective, high-performance block storage for message persistence.
- **AWS IAM & SASL/SCRAM**: Ensures secure, fine-grained access control aligned with OWASP guidelines.
- **AWS Glue Schema Registry**: Enforces strict data contracts to prevent downstream schema drift.

## Rationale
- The event-driven Kafka architecture decouples core services, ensuring high availability (99.95% uptime) and seamless horizontal scalability for 1M MAU.
- Integrated TLS encryption, IAM authentication, and S3-based auditing fulfill stringent GDPR/CCPA compliance and security mandates.