## Overview
[Component-level architecture for the Audit Logging Service of the Library Management System, providing immutable, compliant audit trails for EU-region operations.]

## Key Elements
* Ingest API Handler (Go with Fiber or Gin)
* Event Normalizer & Enricher (Go)
* Log Integrity Verifier (Go)
* WORM Storage Adapter (Go)
* Query & Export API (Go)

## Relationships
* Message Broker to Ingest API Handler via AMQP/JSON with mTLS
* Ingest API Handler to Event Normalizer & Enricher via Go channels/interfaces
* Event Normalizer & Enricher to WORM Storage Adapter via AWS S3 Object Lock API
* Log Integrity Verifier to WORM Storage Adapter via Go interfaces
* Compliance Officers to Query & Export API via HTTPS with RBAC/MFA

## Technology Stack
* Go: Chosen for high-throughput concurrency and performance
* AWS S3 Object Lock & SSE-KMS: Enforces WORM immutability, encryption-at-rest, and EU-only data residency
* SHA-256 Merkle Trees: Enables efficient, tamper-evident log batch verification
* TLS 1.3: Secures all data-in-transit

## Rationale
[This component architecture enforces strict EU data residency, GDPR compliance, and cryptographic immutability using Go and AWS S3 Object Lock. It satisfies performance, security, and audit readiness requirements through decoupled ingestion, sanitization, and verification components.]