## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMR, scheduling, and billing for medium-sized healthcare facilities. Its core purpose is delivering highly available, HIPAA/GDPR-compliant clinical workflows.

## Key Elements
- **EMR Core Service Containers (Java 21 / .NET 8):** Hosts the *Chart & Encounter Manager* and *Authorization & Policy Component*.
- **Crypto & FHIR Sidecars:** Dedicated sidecar containers for envelope encryption/decryption and HL7 FHIR serialization.
- **Data Tier:** PostgreSQL with Citus (Multi-Master) deployed on Kubernetes.
- **Message Broker:** NATS JetStream / Kafka handling transactional outbox events.
- **API Gateway:** Kong/Envoy (Rust/Go) managing ingress traffic.

## Relationships
- **API Gateway -> EMR Core Service:** Routes clinical requests using **gRPC over mTLS**.
- **EMR Core Service -> Sidecars:** Inter-container communication uses **gRPC over Unix Domain Sockets**.
- **EMR Core Service -> Data Tier:** Reads and writes clinical records via **SQL over TLS 1.3**.
- **EMR Core Service -> Message Broker:** Publishes transactional outbox events using **NATS/Kafka protocol**.
- **FHIR Interoperability Adapter -> External Systems:** Exchanges clinical data via **HL7 FHIR APIs** secured with OAuth2 and mTLS.

## Technology Stack
- **Java 21 / .NET 8:** Powers the EMR Core Service for robust enterprise domain modeling.
- **PostgreSQL with Citus:** Provides distributed, highly scalable multi-master relational data storage.
- **gRPC & Unix Domain Sockets:** Ensures ultra-low latency inter-process communication within Kubernetes pods.
- **OpenTelemetry:** Handles distributed tracing with automated regex PHI redaction across hybrid boundaries.
- **FIPS 140-2 Level 3 HSM / KMS:** Secures annual envelope key rotation for encryption at rest.

## Rationale
This architecture isolates heavy workloads like cryptography and FHIR serialization into dedicated sidecars to prevent runtime heap pauses and guarantee sub-second P95 latency. Active-active hybrid deployment across `on-prem-k8s` and `eu-central-1` ensures 99.99% availability and strict regulatory compliance.