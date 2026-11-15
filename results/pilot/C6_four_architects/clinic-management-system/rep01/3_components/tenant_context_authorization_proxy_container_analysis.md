## Overview
The Tenant Context & Authorization Proxy Container enforces fine-grained authorization, tenant isolation, and regulatory compliance for the Clinic Management System. It evaluates security policies with low latency to protect electronic medical records while supporting high availability.

## Key Elements
- Open Policy Agent (OPA)
- Go-based Custom Policy Enforcement Daemon
- In-Memory Policy Cache Component
- Tenant Context Resolver Component
- Dynamic Role Mapping Component
- Embedded SQLite Database
- Context Propagation & Header Sanitization Component
- Metrics & Telemetry Emitter Component
- Policy Bundle Synchronizer Component
- Rate Limiting & Token Bucket Component
- Denial-of-Wallet & Threat Mitigation Component
- Tenant Metadata Lookup Component

## Relationships
- Intercepts inbound traffic from API Gateway via gRPC (`/authz.v1.Authorizer/Check`)
- Communicates with downstream microservices via Envoy-managed mTLS over HTTP/2
- Queries Redis Container tier for session caches, tenant context, and rate-limiting sliding windows
- Interacts with Audit & Compliance Sidecar Container via Unix domain socket and asynchronous logs
- Connects to Data Encryption & Key Management Container (PKCS#11, HSM) for token verification and bundle signatures
- Polls OCI-compliant secure registry over HTTPS via Policy Bundle Synchronizer

## Technology Stack
- Open Policy Agent (OPA) / Rego: Chosen for sub-millisecond, attribute-based policy evaluation
- Go: Powers the custom policy enforcement daemon for high performance and low memory overhead
- Redis Enterprise: Provides distributed session caching and rate-limiting sliding windows
- OpenTelemetry: Enables real-time tracing and metrics collection
- SQLite: Used for localized offline fallback role-cache storage during network partitions

## Rationale
This architecture ensures strict HIPAA and GDPR compliance through robust tenant isolation and cryptographically verified access controls. The distributed caching and Go-based proxy design satisfy the sub-millisecond latency and 99.99% uptime availability constraints.