## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The Observability & Logging Container ensures secure, high-performance telemetry processing, log aggregation, and compliance monitoring.

## Key Elements
- Observability & Logging Container: Centralized metrics, tracing, log aggregation, schema validation, and archival
- Application Sidecars: Fluentd or Vector agents for asynchronous buffering and local disk spooling
- Core Domain Services & API Gateway: Upstream producers of metrics, traces, and structured JSON logs
- Storage Tier: Active telemetry storage, cold storage for archival, and centralized schema registry

## Relationships
- Core Domain Services emit structured JSON logs and OpenTelemetry traces to Application Sidecars via local I/O
- Application Sidecars forward telemetry to the Observability & Logging Container over TLS 1.3 with asynchronous buffering
- Operators query observability dashboards protected by query timeout and resource throttling mechanisms

## Technology Stack
- OpenTelemetry: Unified semantic conventions for distributed tracing, metrics, and logs
- Fluentd / Vector: Sidecar agents providing fail-safe local disk spooling and non-blocking log emission
- JSON: Standardized structured logging format for reliable parsing and schema validation
- TLS 1.3: Protocol ensuring strict encryption-in-transit across all container boundaries

## Rationale
This architecture decouples log emission from primary transactional workflows to protect the 99th-percentile search response time constraint (< 800 ms). It enforces strict EU data residency and minimization through PII masking, automated archival, and dynamic sampling.