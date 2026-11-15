## Overview
The Event Broker provides asynchronous, decoupled messaging for the Clinic Management System across hybrid on-premise and AWS environments. It guarantees zero message loss and HIPAA/GDPR compliance for critical clinical and billing events.

## Key Elements
- Kafka Broker Core (Apache Kafka in KRaft mode)
- Schema Registry (Confluent Schema Registry)
- Kafka Connect
- MirrorMaker 2
- S3 / Object Storage
- Billing & Claims Service
- EMR & Scheduling Service

## Relationships
- Billing & Claims Service -> Schema Registry: Validates event schemas [HTTP/REST]
- Billing & Claims Service -> Kafka Broker Core: Publishes billing events [TCP / mTLS / SASL]
- EMR & Scheduling Service -> Schema Registry: Validates EMR event schemas [HTTP/REST]
- EMR & Scheduling Service -> Kafka Broker Core: Publishes clinical events [TCP / mTLS / SASL]
- Kafka Broker Core -> Kafka Connect: Streams events for long-term retention [TCP / mTLS]
- Kafka Connect -> S3 / Object Storage: Offloads aged log segments via Tiered Storage [HTTPS / TLS 1.3]
- MirrorMaker 2 -> Kafka Broker Core: Replicates cross-site events between on-prem-k8s and eu-central-1 [TCP / mTLS]

## Technology Stack
- Apache Kafka (KRaft mode): Eliminates ZooKeeper overhead for lower latency and simpler operations.
- Confluent Schema Registry: Enforces strict Avro/Protobuf contracts to prevent schema drift and consumer breakage.
- Kafka Connect with S3 Tiered Storage: Offloads 10-year audit logs to cloud storage to prevent local disk bloat.
- MirrorMaker 2: Handles asynchronous cross-site replication between hybrid environments.
- mTLS & SASL/SCRAM-512: Secures data in transit across the hybrid boundary.

## Rationale
Using a decentralized Kafka architecture with KRaft and MirrorMaker 2 prevents hybrid network partition risks while maintaining 99.99% availability. Tiered storage and strict encryption ensure HIPAA/GDPR compliance and 10-year data retention without unsustainable local storage costs.