## Overview
The Audit Logging system provides tamper-proof, asynchronous event tracking for the Library Management System to ensure GDPR compliance, EU data residency, and high-performance search responses. It securely captures, processes, and stores audit trails for financial and administrative actions.

## Key Elements
* Library Administrators & Compliance Officers
* System Auditors & Security Analysts
* API Gateway (Kong/Envoy) & Backend Services
* Audit Agent (Fluentbit sidecar)
* Event Broker (Managed Apache Kafka / EU-hosted)
* Audit Consumer Worker (Go)
* Audit Storage (PostgreSQL with TimescaleDB WORM storage)
* Compliance Query Service (Go/REST)
* Compliance Reporting Dashboard (React)
* EU-hosted SIEM

## Relationships
* API Gateway & Backend Services -> Event Broker (gRPC/TCP, async event ingestion, mTLS)
* Event Broker -> Audit Consumer Worker (Kafka Protocol, mTLS)
* Audit Consumer Worker -> Audit Storage (SQL/TLS, AES-256 encryption at rest, EU KMS)
* Compliance Reporting Dashboard -> Compliance Query Service (HTTPS/REST, mTLS)
* Compliance Query Service -> Audit Storage (SQL/TLS, read-only restricted role, strict query guardrails)
* Audit Storage -> EU-hosted SIEM (Encrypted syslog/TLS)

## Technology Stack
* Fluentbit: Lightweight log shipping and payload sanitization/masking agent
* Managed Apache Kafka: Durable event broker with cross-AZ replication and disk-buffering
* Go: High-performance language for Audit Consumer Worker and Compliance Query Service
* TimescaleDB (WORM Storage): PostgreSQL-based immutable storage supporting automated retention, tiering, and cryptographic hash-chaining
* React: Lightweight UI for the Compliance Reporting Dashboard

## Rationale
An asynchronous event-driven architecture isolates heavy compliance logging from core operations, ensuring 99th-percentile search responses remain under 800ms. Utilizing managed EU-hosted infrastructure, WORM storage, and hash-chaining strictly satisfies EU data residency and GDPR non-repudiation mandates.