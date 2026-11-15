## Overview
The Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing for clinical environments. It leverages a hybrid cloud architecture to ensure high availability, stringent security, and regulatory compliance.

## Key Elements
- **Event Ingestion & Routing Engine:** Apache Kafka for high-throughput, fault-tolerant event streams.
- **Lightweight Edge Broker:** NATS for low-latency, real-time local messaging on-premises.
- **Cross-Site Replication Manager:** Kafka MirrorMaker 2 with TLS Tunnels for multi-master synchronization.
- **Schema Registry:** Confluent Schema Registry for strict AVRO schema evolution.
- **Access Control Enforcer:** Apache Kafka built-in ACLs integrated with Keycloak.

## Relationships
- **Core Services -> Event Ingestion Engine:** Publishes and consumes domain events via OAuth2 Bearer Tokens over mTLS.
- **Core Services -> Schema Registry:** Validates and registers event schemas via HTTPS.
- **Event Ingestion Engine -> Cross-Site Replication Manager:** Synchronizes partitioned topics via Mutual TLS over IPSec.

## Technology Stack
- **Apache Kafka & Strimzi Operator:** Chosen for scalable, fault-tolerant event streaming and Kubernetes-native lifecycle management.
- **NATS:** Selected for lightweight, low-latency edge messaging in `on-prem-k8s`.
- **Confluent Schema Registry:** Implemented to enforce AVRO schemas and prevent breaking changes.
- **Keycloak & OAuth2/OIDC:** Utilized for fine-grained, token-based authorization and topic-level ACL enforcement.

## Rationale
This architecture ensures 99.99% uptime through active-active hybrid replication between `on-prem-k8s` and `eu-central-1`. Strict encryption, ACLs, and schema enforcement satisfy HIPAA and GDPR mandates while maintaining low-latency performance.