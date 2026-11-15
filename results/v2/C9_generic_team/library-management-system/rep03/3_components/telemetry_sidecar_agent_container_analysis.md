## Overview
Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. The architecture enforces strict EU-only data residency and maintains a 99th-percentile search response time under 800 ms.

## Key Elements
* Telemetry Sidecar/Agent Container
* EU-Hosted Observability Infrastructure
* Configuration and Secrets Management Container
* Core microservices and application containers

## Relationships
* Telemetry Sidecar/Agent Container -> EU-Hosted Observability Infrastructure: Exports sanitized operational metrics and logs [TLS Syslog/HTTPS with Gzip/Zstd compression]
* Telemetry Sidecar/Agent Container -> Configuration and Secrets Management Container: Reads runtime configuration and environment variables

## Technology Stack
* OpenTelemetry (OTel): Standardized semantic conventions and structured JSON logging
* Local Disk Buffering: Handles asynchronous batching to prevent data loss during network partitions
* Circuit Breaker & Adaptive Sampling: Protects against resource exhaustion and manages high-load log volumes
* Signal Handlers: Intercepts `SIGTERM` for graceful shutdowns and buffer flushing

## Rationale
Decoupling observability via a sidecar pattern ensures business logic remains lightweight and protects the 800 ms search latency target. Local buffering, PII sanitization, and strict resource quotas guarantee compliance with EU-only data residency rules without risking core application performance.