## Overview
The Clinic Management System is an event-driven healthcare platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It provides secure, highly available clinical workflows across hybrid cloud infrastructures while maintaining strict regulatory compliance.

## Key Elements
- **Event Ingestion & Routing Engine**: Apache Kafka brokers handling high-throughput client connections and partition leader balancing.
- **Schema Registry**: Confluent Schema Registry enforcing strict Avro/Protobuf schema evolution and validation.
- **Cluster Controller (KRaft)**: ZooKeeper-free metadata manager reducing operational complexity.
- **Event Mirroring & Replication Agent**: Kafka MirrorMaker 2 managing cross-datacenter replication between on-prem-k8s and `eu-central-1`.
- **Stream Processing & State Store**: Apache Kafka Streams with local RocksDB executing real-time appointment scheduling resource clash checks.
- **Broker Security & Authorization Manager**: Apache Ranger / Kafka ACLs integrated with Keycloak for topic-level access control and HIPAA compliance.

## Relationships
- Services (Patient, EMR, Billing, FHIR) -> **Schema Registry**: Validates event schemas [HTTPS/REST]
- Services -> **Event Ingestion Engine**: Publishes and consumes encrypted domain events [SASL/SCRAM over TLS, TCP/9094]
- **Event Ingestion Engine** -> **Event Mirroring Agent**: Replicates encrypted topics across hybrid boundaries [TLS, TCP/9094]
- **Event Ingestion Engine** -> **Audit & Archival Store**: Streams long-term event logs for 10-year retention [Kafka Connect / HTTPS]
- **Event Ingestion Engine** -> **Stream Processing**: Processes event streams [In-memory / Local RocksDB]
- **Stream Processing** -> **Distributed Cache**: Synchronizes materialized views [Redis Protocol over TLS]
- **Keycloak Container** -> **Security Manager**: Synchronizes OAuth2/OIDC tokens for authorization [HTTPS/REST]

## Technology Stack
- **Apache Kafka (KRaft mode)**: Selected for distributed, highly available (99.99%) asynchronous event routing.
- **Confluent Schema Registry**: Ensures backward/forward compatibility for clinical data.
- **Kafka Streams & RocksDB**: Enables low-latency stateful event processing for scheduling.
- **Kafka MirrorMaker 2**: Facilitates hybrid cloud disaster recovery across on-prem and AWS `eu-central-1`.
- **Keycloak & Kafka ACLs**: Provides HIPAA-compliant authentication and fine-grained authorization.

## Rationale
This event-driven architecture guarantees 99.99% active-active uptime and meets strict HIPAA/GDPR security controls through robust encryption and ACLs. Furthermore, it easily scales to support high-performance EMR screens and satisfies the 10-year data retention mandate via reliable hybrid replication and streaming to archival storage.