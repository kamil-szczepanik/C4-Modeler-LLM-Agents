## Overview
The Audit Logging Sidecar securely collects, redacts, encrypts, and streams compliance and audit logs for the Library Management System. It ensures GDPR compliance, protects patron PII, and maintains system performance without impacting core circulation services.

## Key Elements
- Audit Logging Sidecar (Vector): Co-located container deployed via Kubernetes Mutating Webhook
- Log Collector Component: Ingests raw logs via local Unix domain sockets
- Processor & Redaction Engine: Strips PII and applies HMAC-SHA256 pseudonymization
- Buffer & Encryption Manager: Handles local disk buffering with AES-256 encryption
- Log Egress Client: Streams signed log batches to external storage
- External Systems: Audit Log Stream, EU Cloud Provider's HSM, SPIFFE/SPIRE Identity Control Plane

## Relationships
- Application Containers -> Log Collector Component: Streams raw logs locally [Unix Domain Sockets]
- Buffer & Encryption Manager -> EU Cloud Provider's HSM: Retrieves keys for at-rest encryption [HTTPS/TLS]
- Log Egress Client -> Audit Log Stream: Streams encrypted, signed payloads [gRPC/TLS with SPIFFE/SPIRE mTLS]

## Technology Stack
- Vector: Chosen for high-throughput, low-overhead log aggregation and transformation
- Unix Domain Sockets: Enables secure, zero-copy local IPC between application and sidecar
- AES-256 / LUKS: Secures local disk buffers against node compromise
- HMAC-SHA256: Pseudonymizes sensitive patron IDs to prevent PII exposure
- gRPC / TLS: High-performance, secure protocol for external log streaming
- SPIFFE/SPIRE: Manages short-lived cryptographic certificates for zero-trust mTLS

## Rationale
This architecture isolates logging overhead to prevent degradation of the 99th-percentile search response time (<800 ms). It strictly enforces EU data residency and GDPR privacy mandates through rigorous local PII redaction and HSM-backed encryption.