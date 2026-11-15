## Overview
The Library Management System provides cataloging, circulation, and self-service portals for academic and public libraries. The Observability Stack container centralizes system telemetry while ensuring strict EU data residency compliance.

## Key Elements
- **OpenTelemetry Collector**: Ingests, filters, and forwards traces and metrics.
- **Prometheus**: Scrapes and stores time-series metrics.
- **Grafana Loki**: Aggregates structured logs.
- **Grafana**: Visualizes metrics, traces, and logs.
- **HashiCorp Vault**: Manages encryption keys for data at rest.

## Relationships
- Core Domain Microservice -> OpenTelemetry Collector: Pushes traces/metrics via OTLP/gRPC (mTLS).
- OpenTelemetry Collector -> Grafana Loki: Forwards structured logs via OTLP/HTTP.
- Prometheus -> Core Domain Microservice: Scrapes metrics via HTTP/Prometheus (mTLS).
- Grafana -> Prometheus: Queries metrics via PromQL/TLS 1.3.
- Grafana -> Grafana Loki: Queries logs via LogQL/TLS 1.3.

## Technology Stack
- **OpenTelemetry Collector**: Chosen for robust telemetry pipelining and rate-limiting.
- **Prometheus TSDB**: Selected for high-performance time-series metrics storage.
- **Grafana Loki**: Adopted for scalable, cost-effective log aggregation.
- **Grafana**: Used for operator visualization and OIDC-backed RBAC.
- **HashiCorp Vault**: Utilized for secure, centralized key management.

## Rationale
This architecture integrates metrics, logs, and traces to meet high-performance search requirements while enforcing strict EU data residency and security constraints.