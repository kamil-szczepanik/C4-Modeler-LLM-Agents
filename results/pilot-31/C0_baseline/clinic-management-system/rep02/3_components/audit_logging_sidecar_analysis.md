## Overview
The Clinic Management System is a clinical IT platform providing patient records, scheduling, and billing. It utilizes a secure, sidecar-based audit architecture to ensure HIPAA/GDPR compliance and immutable record-keeping.

## Key Elements
*   **Audit Logging Sidecar:** Rust-based interceptor with Fluent Bit forwarder.
*   **WORM Storage:** Immutable destination for audit trails.
*   **Local Rule Engine:** Policy Enforcement Point (PEP) for operation classification.
*   **RocksDB:** Local buffer for transient network partition resilience.
*   **Hardware Security Module (HSM/Nitro Enclave):** Cryptographic signing provider.

## Relationships
*   **Parent Service to Sidecar:** gRPC with Unix Domain Sockets for low-latency request interception.
*   **Sidecar to WORM Storage:** TLS 1.3 with mTLS for secure, authenticated log streaming.
*   **Sidecar to Prometheus:** Metrics export for observability and alert triggering.
*   **Sidecar to SIEM:** Real-time alerts for "break-glass" emergency overrides.

## Technology Stack
*   **Rust:** Chosen for memory safety and minimal runtime overhead.
*   **Ed25519:** Cryptographic signing algorithm for non-repudiation.
*   **Fluent Bit:** Used for structured log transformation and PII masking.
*   **Kubernetes:** Orchestration using `postStart`/`preStop` hooks and cgroups for resource isolation.
*   **gRPC:** Protocol for strict schema enforcement and metadata propagation.

## Rationale
The architecture ensures compliance through immutable, cryptographically signed audit logs while maintaining clinical availability via a tiered "fail-closed/fail-open" policy. This design protects sensitive patient data without compromising the performance requirements of critical medical workflows.