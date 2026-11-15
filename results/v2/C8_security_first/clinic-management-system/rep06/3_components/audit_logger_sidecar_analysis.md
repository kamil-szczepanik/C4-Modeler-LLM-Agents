## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities while ensuring strict HIPAA/GDPR compliance and 99.99% availability. It utilizes an immutable Audit Logger Sidecar architecture to stream secure, tamper-evident audit logs without impacting clinical performance.

## Key Elements
- **Main Application Containers**: Core clinical and billing microservices (Java/Spring Boot, Node.js, .NET Core)
- **Audit Logger Sidecar**: Lightweight container running Vector for log processing
- **Log Ingestor Component**: Local Unix Domain Socket receiver
- **Scrubbing & Hashing Component**: PII/PHI redaction and SHA-256 Merkle tree framing module
- **Buffer & Batching Component**: Ephemeral disk-backed buffer (`emptyDir`)
- **Log Exporter Component**: TLS 1.3 streaming mechanism
- **Central SIEM**: External secure log aggregation and 10-year retention storage

## Relationships
- Main Application Containers -> *(Unix Domain Socket / Localhost)* -> Audit Logger Sidecar (Log Ingestor)
- Audit Logger Sidecar -> *(TLS 1.3 over HTTPS)* -> Central SIEM
- Sidecar -> *(Prometheus scrape target)* -> DevOps Monitoring

## Technology Stack
- **Vector (by Datadog)**: Selected for Rust memory safety, low footprint (<30Mi RAM), and native disk buffering
- **Unix Domain Sockets / Fluent Forward**: For high-performance, non-blocking local inter-container communication
- **TLS 1.3 & AES-256**: For encrypted log transmission and data at rest security
- **VRL (Vector Remap Language)**: For real-time PII/PHI regex scrubbing
- **Kubernetes**: For container orchestration, sidecar injection via mutating webhooks, and resource limit enforcement

## Rationale
This architecture ensures zero latency impact on core clinical workflows (P95 EMR load < 1s) through asynchronous, non-blocking sidecar buffering. It satisfies strict HIPAA and GDPR regulations via local PII redaction, cryptographic tamper-evidence, and secure 10-year audit log retention.