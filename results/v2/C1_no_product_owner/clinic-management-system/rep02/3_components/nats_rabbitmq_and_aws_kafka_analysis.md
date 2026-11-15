## Overview
The Clinic Management System is a hybrid-cloud healthcare platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing securely. It provides highly available, HIPAA and GDPR-compliant clinical IT operations across on-premise Kubernetes clusters and AWS (`eu-central-1`).

## Key Elements
* Envoy API Gateway & Istio Service Mesh
* Microservices: Patient & Scheduling Service, EMR Core Service, Billing & Integration Service
* Apache Kafka (AWS MSK and Strimzi on-premise)
* Confluent Schema Registry
* Kafka MirrorMaker 2
* PostgreSQL with Patroni
* WORM-compliant S3 / MinIO
* HashiCorp Vault

## Relationships
* Microservices -> Apache Kafka: Publishes and consumes events [Kafka Protocol over mTLS 1.3]
* Apache Kafka -> Confluent Schema Registry: Validates event schemas [HTTPS over TLS 1.3]
* On-premise Strimzi Kafka -> AWS MSK: Cross-site data replication [Kafka MirrorMaker 2 over TLS 1.3 and IPsec/WireGuard]
* Microservices -> PostgreSQL with Patroni: Persists operational data [PostgreSQL Wire Protocol over TLS 1.3]
* Microservices -> HashiCorp Vault: Manages secrets and PKI [HTTPS over TLS 1.3]

## Technology Stack
* Apache Kafka / AWS MSK / Strimzi: Chosen as a single consolidated event broker to eliminate operational overhead and support high-throughput streaming.
* Confluent Schema Registry: Enforces strict Avro/Protobuf data governance and prevents breaking API changes.
* HashiCorp Vault: Automates short-lived mTLS certificate rotation for strict security posture.
* PostgreSQL with Patroni: Provides high-availability relational data storage.
* S3 / MinIO: Ensures WORM-compliant storage meeting the 10-year data retention mandate.

## Rationale
This consolidated event-driven architecture simplifies operational complexity while ensuring the 99.99% availability and rigorous security mandated by healthcare compliance. Using hybrid-cloud Kafka with automated replication and encryption guarantees low latency, high throughput, and HIPAA/GDPR adherence.