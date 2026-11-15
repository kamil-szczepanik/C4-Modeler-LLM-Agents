## Overview
[The Audit & Compliance Log Service is a backend microservice in Go designed to manage immutable regulatory audit trails, compliance reporting, and real-time anomaly alerting for the Clinic Management System. It ensures strict HIPAA and GDPR compliance with a mandatory 10-year data retention policy and 99.99% availability.]

## Key Elements
* Audit & Compliance Log Service (Go container)
* Event Ingestion Engine (Go component)
* Compliance API Handler (Go component)
* Retention & Archival Worker (Go component)
* Anomaly Detection & Alerting Engine (Go component)
* Event Bus (Apache Kafka / RabbitMQ)
* Databases (MongoDB)
* Object Storage (Encrypted S3-compatible with WORM Compliance Mode)
* Edge Container (Kong / Envoy)

## Relationships
* Edge Container -> Compliance API Handler: Routes requests via internal mTLS [gRPC and REST over mTLS]
* Event Bus -> Event Ingestion Engine: Consumes security and access events [Apache Kafka]
* Event Ingestion Engine -> MongoDB: Stores audit logs [TLS-encrypted connections]
* Event Ingestion Engine -> Anomaly Detection & Alerting Engine: Forwards streaming events [Internal Go Channel]
* Retention & Archival Worker -> Object Storage: Archives historical logs [TLS with WORM Compliance Mode]
* Anomaly Detection & Alerting Engine -> Edge Container: Dispatches webhooks/alerts [HTTPS over TLS]

## Technology Stack
* Go: Chosen for high-throughput, non-blocking concurrency via Go routines and low memory footprint.
* Apache Kafka / RabbitMQ: Provides reliable event streaming, dead-letter queues (DLQ), and backpressure handling.
* MongoDB: Stores active audit logs securely with AES-256 encryption at rest.
* Encrypted S3-compatible Object Storage: Enforces AWS Object Lock in Compliance Mode for tamper-proof 10-year data retention.
* OpenTelemetry & Prometheus: Monitors ingestion lag, processing latency, and archival job success rates.

## Rationale
[Decomposing the service into dedicated ingestion, archival, API, and alerting components isolates heavy workloads and protects ingestion throughput. This architecture satisfies rigorous healthcare security mandates, high availability, and 10-year regulatory retention without performance degradation.]