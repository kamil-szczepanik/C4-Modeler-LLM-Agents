## Overview
The Apache Kafka message broker provides asynchronous, fault-tolerant event processing for the Clinic Management System. It ensures decoupled, high-throughput delivery of billing and clinical data streams across hybrid infrastructure.

## Key Elements
- Broker Node Engine: Manages cluster coordination and partition leadership via KRaft protocol.
- Partition Log Manager: Handles immutable segment files and tiering to object storage.
- Access Control & Auth Interceptor: Enforces security policies, mTLS, and token validation.
- Core API Service: Publishes billing and event streams [TCP].
- Billing Worker: Consumes event streams for financial processing [TCP].

## Relationships
- Core API Service -> Access Control & Auth Interceptor: Publishes billing messages securely [TCP over TLS 1.3 / SASL/SCRAM].
- Billing Worker -> Partition Log Manager: Consumes billing and event streams [TCP].
- Broker Node Engine <-> Broker Node Engine: Handles internal cluster consensus and replication [TCP over mTLS using KRaft].

## Technology Stack
- Apache Kafka: Event broker selected for high availability and throughput.
- KRaft: Metadata management protocol chosen to eliminate external coordination overhead.
- Strimzi: Kubernetes operator used for multi-zone deployment and lifecycle automation.
- Apache Ranger: Authorization framework for role- and attribute-based access control (RBAC/ABAC).
- AES-256 / TLS 1.3: Encryption standards implemented for data at rest and in transit.

## Rationale
This architecture ensures 99.99% system availability and strict HIPAA/GDPR compliance through isolated component boundaries and encrypted event streaming. It decouples high-volume clinic transactions to guarantee low-latency user interfaces and prevent data loss.