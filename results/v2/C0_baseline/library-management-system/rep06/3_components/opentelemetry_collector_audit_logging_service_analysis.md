## Overview
- OpenTelemetry Collector & Audit Logging Service for the Library Management System.
- Collects telemetry, processes security logs, and ensures EU data residency compliance.

## Key Elements
- OTel Collector Core (`otelcol-contrib`)
- Audit Log Processor Component
- Audit Log Exporter
- Audit Query API Component
- Managed Databases (PostgreSQL Multi-AZ, Read Replica)

## Relationships
- Microservices to OTel Collector via gRPC (Port 4317) with mTLS
- OTel Collector to PostgreSQL via PostgreSQL wire protocol over TLS
- API Gateway to Audit Query API via TLS 1.3
- Audit Query API to PostgreSQL Read Replicas via TLS

## Technology Stack
- OpenTelemetry (`otelcol-contrib`): Low-overhead telemetry ingestion and PII scrubbing
- Go: Custom audit log processor implementation
- PostgreSQL Multi-AZ & Read Replicas: EU-compliant immutable audit storage and query offloading
- TLS 1.3 & mTLS: End-to-end transport encryption and authentication

## Rationale
- Enforces strict EU data residency and GDPR audit requirements via isolated storage and PII scrubbing.
- Protects system performance using aggressive memory limiters and read-replica offloading for queries.