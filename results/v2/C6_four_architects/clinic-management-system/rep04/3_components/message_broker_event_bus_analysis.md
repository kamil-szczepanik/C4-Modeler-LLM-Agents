## Overview
• Manages patient admissions, EMR, scheduling, and billing for clinics via a hybrid cloud platform.
• Ensures 99.99% availability, strict HIPAA/GDPR compliance, and ≥ 10-year data retention.

## Key Elements
• Users: Doctors, Nurses, Receptionists, Billing Staff, SRE / Operations
• External Systems: Identity Provider (IdP), Payment Gateway, Insurance Clearinghouse, External Lab & Imaging Systems, Immutable Object Storage
• Containers: Single-Page Application, API Gateway, Core Clinical Microservice, Scheduling Microservice, Billing & Claims Microservice, Integration / FHIR Service, FHIR Integration Broker, Distributed Relational Database, Message Broker / Event Bus, State Caching Layer, Key Management Service, Audit Log Store, Observability & Telemetry Collector, Service Mesh
• Message Broker Components: Broker Cluster, Schema Registry, Kafka Connect, Stream Processor, Topic Access Control Manager, DLQ Manager, Kafka UI

## Relationships
• Microservices -> Broker Cluster: Produces and consumes asynchronous CloudEvents [mTLS / TCP/TLS]
• Core Clinical Microservice -> Schema Registry: Validates event schemas [HTTP/REST over TLS]
• Kafka Connect -> Audit Log Store / Immutable Object Storage: Streams audit events and offloads historical data [HTTPS]
• SRE / Operations -> Kafka UI: Monitors cluster health and consumer lag [HTTPS]

## Technology Stack
• Hybrid Cloud: on-prem-k8s and eu-central-1 for high availability
• Frontend: React / TypeScript for SPA interface
• Backend Microservices: Spring Boot (Core Clinical), Go (Scheduling), .NET (Billing), Node.js (Integration)
• Messaging & Data: Apache Kafka (Event Bus), Confluent Schema Registry, Apache Flink / Kafka Streams (Stream Processor), CockroachDB / PostgreSQL (Relational DB), Redis Enterprise (Caching)
• Security & Observability: Vault / Cloud KMS, Istio (Service Mesh), OpenTelemetry / Prometheus / Loki

## Rationale
• Hybrid active-active multi-region deployment guarantees 99.99% availability and low-latency access.
• Kafka-based event-driven architecture with encryption (AES-256, mTLS, TLS) ensures strict HIPAA/GDPR compliance and ≥ 10-year retention.