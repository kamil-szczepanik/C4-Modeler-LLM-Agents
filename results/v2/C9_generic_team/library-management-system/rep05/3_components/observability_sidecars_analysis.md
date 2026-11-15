## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue items, manage circulation, and provide self-service portals while strictly enforcing EU data residency. The architecture integrates robust Observability Sidecars to ensure high performance and strict telemetry governance.

## Key Elements
- Observability Sidecars (OpenTelemetry Collector agents)
- Primary application containers (API Gateway / BFF, Web App, Core Transactional, Search, Workers)
- Enterprise Logging and Monitoring Service (External sink)
- Local encrypted quarantine volume (Dead-letter queue)

## Relationships
- Primary containers to Observability Sidecars: Telemetry data transmission via local `localhost` loops using W3C Trace Context headers
- Observability Sidecars to Enterprise Logging and Monitoring Service: Scrubbed telemetry payload forwarding across network boundaries
- Observability Sidecars to Local Quarantine Volume: Secure routing of invalid payloads via a dead-letter queue (DLQ) strategy
- Prometheus Scrapers to Observability Sidecars: Internal metrics monitoring via Prometheus-compatible endpoints

## Technology Stack
- OpenTelemetry Collector: Standard sidecar pattern for local telemetry buffering and dynamic pipeline reloading
- Prometheus: Endpoint compatibility for internal metrics monitoring (drop counters, queue depth, export latency)
- W3C Trace Context: Standardized protocol for distributed trace-context propagation
- Bounded local disk storage: Spooling mechanism for backpressure management during downstream outages

## Rationale
This architecture uses local sidecars with strict resource caps and circuit breaking to protect the 99th-percentile search response time (<800 ms). Furthermore, local data scrubbing and a fail-open/fail-closed governance matrix ensure strict adherence to EU data residency mandates without compromising system availability.