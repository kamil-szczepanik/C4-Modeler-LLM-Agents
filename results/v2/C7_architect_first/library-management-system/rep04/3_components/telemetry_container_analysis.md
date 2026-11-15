## Overview
The Library Management System provides cataloging, circulation, and self-service portals for libraries, with EU-only data residency and sub-800ms search performance requirements. The Telemetry Container manages operational monitoring, logging, and metrics aggregation.

## Key Elements
- Prometheus: Metrics Scraper, TSDB, Rule Evaluator, and secondary replication for long-term storage
- Fluentbit: Log Forwarder with disk-backed queues, rate limiting, and PII sanitization
- Grafana: Visualization and Alerting UI with RBAC and immutable audit logging
- Blackbox Exporter: Synthetic probing for search SLA verification (< 800ms)
- Library Administrator: Business-value dashboard consumer

## Relationships
- Core Services, Search, API Gateway -> Prometheus (Pulls metrics via HTTP/TCP)
- All Containers -> Fluentbit (Writes logs via local socket/file mounts)
- Prometheus Scraper -> Prometheus Rule Evaluator (Internal evaluation loop)
- Library Administrator -> Grafana (HTTPS, via API Gateway OIDC integration)
- Grafana -> External Alert Sink (Webhooks via PagerDuty/EU-hosted incident tool)

## Technology Stack
- Prometheus & Prometheus Rule Evaluator: Metrics collection and pre-aggregation for PromQL queries
- Grafana: Operational and business dashboard visualization with strict RBAC
- Fluentbit: Log collection, scrubbing, and rate-limited log forwarding
- Region-locked Block Storage: Encrypted storage ensuring EU-only data residency compliance
- Blackbox Exporter: Synthetic performance probing for R-05 SLA tracking

## Rationale
This architecture guarantees strict EU-only data residency through region-locked encrypted storage and secure log forwarding. It ensures sub-800ms search performance visibility via dedicated synthetic probing and pre-aggregated business metrics.