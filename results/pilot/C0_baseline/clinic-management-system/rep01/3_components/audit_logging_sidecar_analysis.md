## Overview
The Audit Logging Sidecar provides secure, immutable WORM audit trails for the Clinic Management System to ensure strict HIPAA and GDPR compliance. It captures, buffers, and cryptographically signs operational events across hybrid cloud deployments without impacting clinical performance.

## Key Elements
* Compliance Officers, Hospital Legal Counsel, External Regulatory Auditors (Users)
* Audit Logging Sidecar (Container - Sidecar Proxy)
* HTTP Log Interceptor (Component - Go / Envoy Filter)
* Asynchronous Buffer Queue (Component - Golang channel-based ring buffer)
* WORM Storage Exporter (Component - Go)
* Indexer and Query Agent (Component - Go with embedded SQLite/Bleve search index)
* Immutable S3 Bucket with Object Lock (External Storage)

## Relationships
* Core API Service and EMR Engine to HTTP Log Interceptor via local loopback using gRPC/HTTP over shared memory and mTLS/Unix domain sockets
* Audit Logging Sidecar to Immutable S3 Bucket via HTTPS (TLS 1.3) with Object Lock
* Compliance Officers to Indexer and Query Agent via secure gRPC management API with token-based auth and RBAC

## Technology Stack
* Go / Envoy Filter: Chosen for high-throughput, low-latency log interception and resource efficiency in a Kubernetes sidecar pattern
* Golang channel-based ring buffer with local disk caching: Ensures zero data loss and fault tolerance during network partitions or cloud outages
* AES-256 and HMAC-SHA256 chained hashes: Enforces cryptographic verification and data protection for PHI at rest and in transit

## Rationale
This architecture decouples compliance logging from clinical operations to maintain the required 99.99% availability and sub-second P95 performance SLA. Furthermore, it guarantees forensic integrity and a 10-year data retention mandate via immutable S3 storage and cryptographic block signatures.