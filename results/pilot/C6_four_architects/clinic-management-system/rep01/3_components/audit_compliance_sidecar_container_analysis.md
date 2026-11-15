## Overview
The Clinic Management System is a clinical IT platform providing patient administration, electronic medical records, scheduling, and billing. It features a distributed, hybrid-cloud architecture enforcing strict HIPAA/GDPR compliance, 99.99% availability, and long-term data retention.

## Key Elements
- Log Interceptor Component (FluentBit/Vector, Unix Domain Sockets, `mmap`)
- Policy Validation Component (Go, WebAssembly, Rego rules)
- Cryptographic Signer & Formatter Component (Go, Canonical JSON RFC 8785, HMAC-SHA256)
- HSM Key Provider Component (PKCS#11, Hardware Security Module)
- Resilient Forwarder Component (RocksDB persistent buffering, token-bucket rate limiter)
- Compliance Archival Gateway & WORM Object Storage
- Elasticsearch Containers cluster
- RabbitMQ Container cluster (AMQP 0.9.1)
- Observability Collector Container (OpenTelemetry, Prometheus)
- Tenant Context & Authorization Proxy Container

## Relationships
- Log Interceptor Component -> Primary Container: Consumes stdout/stderr logs via `AF_UNIX` and shared emptyDir volumes [Shared Memory]
- Policy Validation Component -> Tenant Context & Authorization Proxy Container: Fetches context-aware masking policies and compiled Rego rules [gRPC/Wasm]
- Cryptographic Signer & Formatter Component -> HSM Key Provider Component: Performs hardware-backed digital signatures and key rotations [PKCS#11]
- Resilient Forwarder Component -> Compliance Archival Gateway & WORM Object Storage: Streams encrypted audit logs [mTLS 1.3, gRPC]
- Resilient Forwarder Component -> Elasticsearch Containers: Dispatches log batches for real-time analytics [TLS]
- Resilient Forwarder Component -> RabbitMQ Container cluster: Publishes security alerts and tamper notifications [AMQP 0.9.1, TLS 1.3]
- Resilient Forwarder Component -> Observability Collector Container: Emits operational metrics [HTTP, OpenTelemetry]

## Technology Stack
- Go: Chosen for high-performance compliance processing, cryptographic signing, and policy validation components.
- FluentBit/Vector & RocksDB: Selected for low-latency asynchronous log interception and resilient disk-backed persistent buffering.
- WebAssembly (Wasm) & Rego: Utilized for sub-millisecond local evaluation of data sanitization policies without inter-process overhead.
- PKCS#11 & HSM: Implemented for secure, hardware-backed cryptographic key generation and tamper-evident log signing.
- gRPC with mTLS 1.3 & Protocol Buffers: Deployed for secure, efficient cross-container telemetry transmission and archival streaming.

## Rationale
This architecture ensures immutable, tamper-evident compliance tracking that satisfies rigorous 10-year data retention and HIPAA/GDPR privacy mandates. Asynchronous local buffering and decoupled sidecar components guarantee high availability and sub-second performance without impacting primary clinical transaction processing.