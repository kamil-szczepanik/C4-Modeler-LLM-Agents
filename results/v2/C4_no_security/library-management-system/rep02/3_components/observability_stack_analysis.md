## Overview
The Library Management System provides cataloging, circulation, and self-service portals for libraries within an EU-only data residency constraint. The Observability Stack ensures technical resilience for SREs and compliance reporting for administrators while maintaining P99 search latency under 800 ms.

## Key Elements
- Platform SREs / Operations Engineers & Library Administrators
- OpenTelemetry Collector (OpenTelemetry)
- Metrics Storage & Query Engine (Prometheus + Thanos sidecar)
- Log Aggregator & Forwarder (Fluentbit / Promtail)
- Dashboard & Reporting Engine (Grafana)
- Synthetic Monitoring Agent (Grafana Synthetic Monitoring / Blackbox Exporter)
- EU-Resident Log & Audit Sink & EU-Region Object Storage

## Relationships
- Core Domain Services, API Gateway, Notification Dispatcher -> OpenTelemetry Collector [OTLP/gRPC]
- OpenTelemetry Collector -> Metrics Storage & Query Engine [Prometheus Remote Write]
- Metrics Storage & Query Engine -> Dashboard & Reporting Engine [PromQL/HTTP]
- Log Aggregator -> EU-Resident Log & Audit Sink [Encrypted Log Stream / HTTPS]
- Synthetic Monitoring Agent -> API Gateway [HTTPS/REST]
- Metrics Storage & Query Engine -> EU-Region Object Storage [S3 API / TLS]

## Technology Stack
- OpenTelemetry: Standardized protocol for gathering metrics, logs, and traces.
- Prometheus + Thanos: Scalable time-series storage and high availability with long-term object storage.
- Grafana: Unified visualization for SRE technical dashboards and Administrator SLA reports.
- Fluentbit / Promtail: Lightweight log forwarding enforcing EU compliance.
- Blackbox Exporter: Active probing to validate P99 search performance.

## Rationale
This component architecture separates technical observability pipelines from core application workloads to protect P99 search latency (<800ms). Furthermore, Thanos object storage integration and EU-bound log forwarding guarantee strict compliance with data residency mandates.