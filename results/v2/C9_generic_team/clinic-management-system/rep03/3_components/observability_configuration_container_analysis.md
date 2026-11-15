## Overview
The Clinic Management System is a clinical IT platform providing patient admissions, electronic medical records, scheduling, and billing. It features a decoupled, hybrid-cloud observability and configuration architecture designed for high availability and strict compliance.

## Key Elements
- **Domain Containers**: Microservices handling clinical workflows, running in Kubernetes.
- **Observability & Configuration Container**: Centralized system managing telemetry, logging, and configuration.
- **Secret Manager**: Dedicated sidecar/initialization plane decoupled from telemetry.
- **Prometheus & Fluentbit**: Edge telemetry, metric scraping, and log aggregation agents.
- **Local Disk Buffers (EmptyDir)**: Temporary storage for fault-tolerant telemetry backpressure.

## Relationships
- **Domain Containers to Configuration Agent**: Reads hot-reloaded configurations via secure local loopback or shared-memory volume mounts.
- **Fluentbit/Prometheus to Storage**: Exports scrubbed telemetry and audit logs over TLS to `eu-central-1` and `on-prem-k8s` backends.
- **Observability Agents to Domain Pods**: Scrapes metrics via HTTP and monitors health probes via standardized readiness/liveness endpoints.

## Technology Stack
- **Prometheus & OpenTelemetry**: Standardized metric scraping and distributed tracing headers.
- **Fluentbit**: Edge log aggregation featuring automated PII/PHI payload masking and disk-backed local buffering.
- **JSON Schema / Protocol Buffers**: Strict strongly typed contracts for configuration validation.
- **Cryptographic Hash & Version Tagging**: Ensures immutable, tamper-resistant configuration bundles across hybrid regions (`on-prem-k8s` and `eu-central-1`).

## Rationale
This architecture ensures 99.99% availability via circuit breakers, fallbacks, and local disk buffering during network partitions in hybrid deployments. It strictly satisfies HIPAA and GDPR compliance through isolated secret management, automated edge PII masking, and immutable audit logging.