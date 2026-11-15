## Overview
The Clinic Management System is an enterprise healthcare platform that handles patient admissions, EMRs, scheduling, and billing. It utilizes a resilient, event-driven messaging architecture to ensure high availability, HIPAA compliance, and sub-second performance.

## Key Elements
* Topic Partition Manager
* Confluent Schema Registry
* Kafka Connect Engine
* MirrorMaker 2
* Apache Kafka Streams

## Relationships
* Microservices -> Confluent Schema Registry: Validates event payloads synchronously via HTTP/REST [Avro, HTTP/REST]
* Kafka Connect Engine -> PostgreSQL Replicas and Elasticsearch Audit Trail: Streams persistent records securely [TLS 1.3, SCRAM-SHA-512]
* On-Premises Kubernetes Cluster -> AWS eu-central-1: Synchronizes clinical event streams via MirrorMaker 2 [TLS 1.3]
* Apache Kafka Streams -> Scheduling and Audit Sinks: Performs real-time resource clash checks and PHI data masking [In-memory processing]

## Technology Stack
* Apache Kafka: Core messaging backbone for decoupled event-driven communication
* Confluent Schema Registry: Enforces strict Avro schemas for HIPAA-compliant payload validation
* Kafka Connect: Secures encrypted data sinks using TLS 1.3 and SCRAM-SHA-512 authentication
* MirrorMaker 2: Facilitates cross-cluster replication for active-active hybrid disaster recovery
* Apache Kafka Streams: Executes real-time PHI masking and scheduling clash detection

## Rationale
This component architecture fulfills the 99.99% availability and 10-year data retention constraints through active-active hybrid replication and encrypted persistent sinks. Furthermore, strict schema validation and real-time PHI masking ensure continuous HIPAA and GDPR compliance without sacrificing sub-second performance.