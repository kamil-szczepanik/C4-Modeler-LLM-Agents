## Overview
The Clinic Management System is a clinical IT platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict HIPAA/GDPR compliance, and 10-year data retention across a hybrid cloud topology.

## Key Elements
- **Broker Node Cluster (Apache Kafka):** Distributed partition-based messaging for high-throughput event streaming with AES-256 encryption.
- **Schema Registry (Confluent Schema Registry):** Enforces Avro/Protobuf schema validation for clinical events.
- **Kafka Connect Cluster:** Manages reliable integration sinks and sources, streaming audit events.
- **MirrorMaker 2:** Handles cross-region replication between on-prem-k8s and eu-central-1.
- **Strimzi Operator:** Manages Kubernetes-native Kafka deployment, automated rolling upgrades, and mTLS certificate rotation.

## Relationships
- **Microservices to Broker Node Cluster:** Produce and consume events via TCP [TLS 1.3 / mTLS & SCRAM-SHA-512].
- **Producer Services to Schema Registry:** Validate event schemas prior to publishing via HTTP/REST [mTLS].
- **Broker Node Cluster to Kafka Connect Cluster:** Stream CDC and audit data via internal TCP.
- **Kafka Connect Cluster to Regulatory Audit System:** Export immutable audit logs via HTTPS [TLS 1.3].
- **Broker Node Cluster (On-Prem) to MirrorMaker 2 to Broker Node Cluster (EU Cloud):** Replicate cross-region topics via encrypted TCP [mTLS].

## Technology Stack
- **Apache Kafka:** Core event backbone chosen for distributed partition streaming and high throughput.
- **Confluent Schema Registry:** Selected for strict Avro/Protobuf validation to maintain data integrity.
- **Strimzi Operator:** Utilized for automated Kubernetes-native lifecycle management and self-healing.
- **HashiCorp Vault / Kubernetes Secrets:** Implemented for dynamic SCRAM-SHA-512 credential injection and mTLS certificate rotation.

## Rationale
This architecture uses geo-local event streaming with MirrorMaker 2 and automated Strimzi orchestration to guarantee 99.99% availability in a hybrid environment. Strict ACLs, payload envelope encryption, and WORM-backed storage satisfy rigorous HIPAA and GDPR security and 10-year retention mandates.