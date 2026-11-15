## Overview
The Reporting/Analytics Container delivers operational dashboards and strategic executive reports for library administrators and compliance officers. It processes event streams to provide business intelligence while maintaining strict EU data residency and privacy compliance.

## Key Elements
* Library Administrators & Compliance Officers (Primary Users)
* Reporting/Analytics Container (Analytics Service)
* Audit & Event Tracking Container
* Apache Kafka / Redpanda (Event Streaming)
* ClickHouse / OLAP Database & EU Object Storage (Analytical Datastore & Cold Storage)
* Redis / Kafka (Background Worker Queue)

## Relationships
* Apache Kafka / Redpanda -> Reporting/Analytics Container: Populates analytics data via event streams [Internal API]
* Reporting/Analytics Container -> Audit & Event Tracking Container: Streams report generation and data export events [Internal API]
* Reporting/Analytics Container -> ClickHouse / OLAP Database: Queries aggregated metrics [TCP/SQL]
* Reporting/Analytics Container -> EU Object Storage: Archives raw event logs via automated data tiering [HTTPS/TLS 1.3]

## Technology Stack
* ClickHouse / OLAP Database: Provides read-side isolation and fast analytical query performance
* KEDA: Drives metric-based autoscaling for analytics workers during heavy reporting periods
* Redis / Kafka: Backs asynchronous worker queues for heavy PDF/CSV report generation
* AES-256 & TLS 1.3: Secures data-at-rest and in-transit within the EU boundary
* S3-compatible EU Object Storage: Handles cold storage and data lifecycle management (DLM)

## Rationale
This architecture isolates heavy reporting workloads from transactional databases to meet high-performance search requirements. It enforces strict EU-only data residency and cryptographic erasure protocols to satisfy GDPR compliance.