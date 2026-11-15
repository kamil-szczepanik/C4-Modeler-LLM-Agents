## Overview
- Observability Backend system designed to monitor performance, guarantee Service Level Objectives (SLOs), and ensure strict EU-only data residency compliance for the Library Management System.
- Empowers DevOps/SREs to proactively maintain 99.9% uptime and track non-functional search latency requirements.

## Key Elements
- OpenTelemetry Collector (Go)
- Time-Series Metrics Database (VictoriaMetrics / Prometheus - C++)
- Distributed Trace Store (Grafana Tempo - Go)
- Visualization UI & Alerting Engine (Grafana - TypeScript/Go)

## Relationships
- Web Application / API Gateway -> OpenTelemetry Collector: Exports traces/metrics [OTLP/gRPC with mTLS]
- OpenTelemetry Collector -> Time-Series Metrics Database: Writes metrics [Prometheus Remote Write]
- OpenTelemetry Collector -> Distributed Trace Store: Writes spans [OTLP/gRPC]
- Visualization UI -> Time-Series Metrics & Trace Stores: Queries data [PromQL / TraceQL with OIDC RBAC]
- Alerting Engine -> External Notification Gateway: Dispatches incident alerts [HTTPS/REST with HMAC]

## Technology Stack
- OpenTelemetry (Go): Chosen for standardized, polyglot telemetry collection and built-in edge PII scrubbing.
- VictoriaMetrics (C++): Selected for efficient, high-cardinality metrics storage supporting R-05 search latency tracking.
- Grafana Tempo (Go): Utilized for cost-effective, object-storage-backed distributed trace analysis.
- Grafana (TypeScript/Go): Deployed for unified visualization, RBAC dashboarding, and threshold-based alerting.

## Rationale
- Architecture meets EU data residency constraints through local PII scrubbing at the collector edge and AES-256 encryption at rest.
- Dedicated metrics and tracing components directly support tracking and safeguarding the 99th-percentile search response time under 800ms (R-05).