## Overview
The Audit & Compliance Container is a secure microservice within the Clinic Management System designed to ingest, cryptographically verify, and store telemetry logs to guarantee strict HIPAA and GDPR compliance. It provides real-time anomaly detection and automated reporting capabilities to mitigate regulatory risks and enforce data integrity across the hybrid cloud infrastructure.

## Key Elements
- **Event Ingestion Engine**: Go-based Kafka consumer for raw security and access events.
- **Log Integrity & Hash Chain Service**: Go component implementing cryptographic hash-chains for tamper-evident logs.
- **Anomaly Detection & Alert Engine**: Go stream-processing component evaluating real-time threat thresholds.
- **Compliance Storage Repository**: PostgreSQL paired with S3 Glacier Vault Lock using WORM controls.
- **Audit Reporting API**: Node.js/Go REST/gRPC service for generating cryptographically signed compliance reports.
- **Compliance/IT Auditor**: Primary human user role enforcing regulatory oversight.

## Relationships
- **Event Ingestion Engine** consumes from **Apache Kafka** [Kafka Protocol over mTLS with SASL/SCRAM]
- **Event Ingestion Engine** feeds **Anomaly Detection & Alert Engine** [Internal IPC / Go Channels]
- **Log Integrity & Hash Chain Service** persists to **Compliance Storage Repository** [SQL / S3 API with AES-256 and Field-Level Encryption]
- **Audit Reporting API** serves **Compliance/IT Auditor** [HTTPS / REST with RBAC, ABAC, and KMS Digital Signatures]

## Technology Stack
- **Go / Node.js**: Selected for high-throughput concurrency in stream processing and API handling.
- **Apache Kafka**: Used for scalable, fault-tolerant event streaming.
- **PostgreSQL & S3 Glacier Vault Lock**: Implemented for hot operational logging and 10-year WORM-compliant cold-tier retention.
- **mTLS & KMS**: Enforced for secure transport, field-level encryption, and cryptographic export signatures.

## Rationale
This architecture uses immutable hash-chaining, WORM storage, and real-time anomaly alerting to satisfy strict 10-year data retention and HIPAA/GDPR compliance mandates. Hybrid-cloud decoupling via Kafka and Kubernetes ensures high availability and resilience under peak clinical workloads.