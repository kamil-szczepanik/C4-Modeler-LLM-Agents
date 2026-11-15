## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue items, manage circulation, and provide self-service portals while maintaining EU-only data residency. The architecture utilizes a sidecar telemetry pattern to ensure high-performance, compliant log and metric collection.

## Key Elements
- Log/Metrics Collector Agent (OTel Collector / Fluentd)
- Monitoring and Telemetry Aggregator
- Centralized Configuration Store (Consul / Spring Cloud Config)
- Application Containers (Spring Boot)

## Relationships
- Log/Metrics Collector Agent -> Monitoring and Telemetry Aggregator: Forwards structured JSON logs and metrics via TLS
- Log/Metrics Collector Agent -> Centralized Configuration Store: Fetches externalized parsing and sanitization rules via API/RPC

## Technology Stack
- OTel Collector / Fluentd: Chosen for efficient log/metric routing and local disk-backed buffering.
- Consul / Spring Cloud Config: Utilized for externalizing pipeline configurations and PII sanitization rules.
- Cosign: Implemented for container image signing to ensure supply-chain integrity.
- TLS: Enforced for secure telemetry transmission to satisfy EU data residency constraints.

## Rationale
The architecture guarantees high-performance telemetry processing with sub-800ms search responses by isolating collection workloads into sidecar containers with local buffering. Strict PII sanitization at the source and centralized configuration management ensure continuous compliance with EU data residency requirements.