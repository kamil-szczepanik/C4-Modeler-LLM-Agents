## Overview
The EMR Microservice manages electronic medical records and clinical workflows within a hybrid cloud architecture. It ensures HIPAA/GDPR compliance, high availability, and sub-second performance for clinical operations.

## Key Elements
- EMR API Controller (Spring Boot / Express.js)
- Clinical Record Engine (Java / Node.js)
- FHIR Interoperability Adapter (Java HAPI FHIR / Node.js)
- Audit Logger Component
- KMS Crypto Interceptor
- Clinical Caching Layer (Redis)
- Telemetry & Circuit Breaker Sidecar (Istio)

## Relationships
- EMR API Controller -> Clinical Record Engine: In-process method calls [In-process]
- Clinical Record Engine -> FHIR Interoperability Adapter: Internal eventing [Kafka/AMQP]
- Audit Logger Component -> WORM Audit Log Store: Cryptographically signed writes [HTTPS/TLS 1.3]
- Clinical Record Engine -> KMS Crypto Interceptor: Cryptographic operations [Local KMS SDK]
- Clinical Record Engine -> Clinical Caching Layer: Record retrieval [Redis Protocol over mTLS]
- KMS Crypto Interceptor -> PostgreSQL Database: Persists ciphertexts [AES-256]

## Technology Stack
- Spring Boot / Express.js: Powers microservice components for efficient request handling
- Apache Kafka / AMQP: Enables reliable internal eventing and active-active replication
- Redis: Provides low-latency caching of encrypted clinical records
- Istio with SPIFFE/SPIRE: Enforces strict mTLS and service mesh security
- HSM-backed KMS: Manages encryption keys and supports cryptographic erasure

## Rationale
This architecture uses active-active replication and caching across hybrid boundaries to achieve 99.99% availability and sub-second P95 latency. Layered cryptographic controls and immutable audit logging ensure strict compliance with HIPAA and GDPR mandates.