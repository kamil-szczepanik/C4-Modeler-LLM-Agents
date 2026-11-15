## Overview
The Observability Collector Container ingests, processes, and exports system telemetry using OpenTelemetry and Prometheus. It enforces strict HIPAA, GDPR, and security mandates across hybrid Kubernetes and cloud environments.

## Key Elements
- OpenTelemetry Collector: Primary internal telemetry ingestion, processing, and export engine
- Receivers Layer: Ingests data via OTLP (gRPC/HTTP), Prometheus scraping, fluent-bit logs, and Apache Kafka StatefulSet
- Processing Layer: Includes batching, memory limiters, data scrubbing, Geo-Routing, Dynamic Sampling, Schema Validation, and Tenant Isolation Tagging
- Exporters Layer: Routes telemetry to Prometheus TSDB, Elasticsearch, ClickHouse, and remote SIEM backends
- Prometheus Alertmanager: Internal Alerting and Rule Evaluation Engine
- Persistent Queue (File Storage Extension): Guarantees data durability during network partitions
- mTLS Credential Manager: Manages automated certificate rotation for outbound gRPC exporters
- Configuration Hot-Reload Controller: Enables zero-downtime updates via Kubernetes ConfigMap

## Relationships
- Application Pods to Receivers Layer: Forwards logs and metrics via fluent-bit and OTLP (gRPC/HTTP)
- Apache Kafka StatefulSet to Kafka Consumer Receiver: Pulls raw telemetry events during peak loads
- Exporters Layer to Prometheus TSDB: Routes processed performance metrics locally via secure gRPC
- Exporters Layer to `eu-central-1` Backend: Forwards compliance audit traces via gRPC over the Hybrid VPN Gateway Container
- Prometheus Alertmanager to External SIEM System: Triggers immediate alerts via webhook over mTLS

## Technology Stack
- OpenTelemetry Collector: Chosen for robust, vendor-agnostic telemetry ingestion and routing
- Prometheus & Alertmanager: Selected for internal metric collection, TSDB storage, and alerting
- Apache Kafka: Used for zero-loss telemetry buffering during high-throughput loads
- File Storage Extension: Implemented for local persistent queueing during network partitions
- mTLS & W3C Trace Context: Enforced for secure transit encryption and distributed request tracing

## Rationale
This architecture guarantees 99.99% observability availability and strict regulatory compliance through automated PHI scrubbing and geo-routing. It ensures zero telemetry data loss during network partitions by utilizing persistent local queueing and Kafka buffering.