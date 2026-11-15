## Overview
The Library Management System analytics subsystem collects, processes, and stores telemetry and usage data for public and academic libraries. It ensures compliance with EU-only data residency and GDPR mandates while powering administrative reporting.

## Key Elements
- Ingestion Proxy / Collector (Fluentd)
- Stream Buffer (Apache Kafka)
- Analytics Datastore Engine (ClickHouse)
- ETL / Aggregation Worker (Python)
- Dead-Letter Queue (DLQ)

## Relationships
- API Gateway -> Ingestion Proxy: Forwards raw events [HTTP/2 / TLS 1.3 with mTLS]
- Ingestion Proxy -> Stream Buffer: Publishes pseudonymized events [TCP / Kafka Wire Protocol with SASL/SCRAM and TLS 1.3]
- Stream Buffer -> Analytics Datastore Engine: Consumes and flushes events to disk [TCP]
- Analytics Datastore Engine -> Core Services API: Serves OLAP queries and BI exports [HTTP/gRPC]
- ETL / Aggregation Worker -> Analytics Datastore Engine: Computes materialized views and executes scheduled TTL rollups [Internal TCP]

## Technology Stack
- Fluentd: Ingestion proxy chosen for high-throughput buffering, pipeline filtering, and PII masking.
- Apache Kafka: Stream buffer selected to decouple ingestion from persistence, absorb traffic spikes, and route poison pills to a DLQ.
- ClickHouse: Columnar database chosen for fast OLAP queries, massive write throughput, and automated partition TTL policies supporting EU data residency.
- Python: ETL and aggregation worker language chosen for scheduled metrics computation and materialization.
- Prometheus: Monitoring framework chosen for tracking consumer lag, disk saturation, and ingestion error rates.

## Rationale
This decoupled event-driven architecture handles high-throughput telemetry with minimal latency while enforcing strict EU data residency and PII minimization. Immutable pseudonymized schemas and automated TTL policies ensure full GDPR compliance without sacrificing OLAP query performance.