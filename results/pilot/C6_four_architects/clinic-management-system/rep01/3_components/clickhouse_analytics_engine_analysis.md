## Overview
The ClickHouse Analytics Engine provides high-throughput analytical reporting, billing insights, and clinical data aggregation for the Clinic Management System. It operates across hybrid environments while maintaining strict HIPAA, GDPR, and 10-year data retention compliance.

## Key Elements
* Columnar Storage Engine & MergeTree Table Family
* Vectorized Query Execution Engine
* ClickHouse Keeper Cluster
* Kafka Table Engine & Data Ingestion Coordinator
* Mutation Execution Controller & Schema Evolution Manager
* Native Disk Encryption Manager (LUKS / PKCS#11)
* Audit Logging Interceptor & Resource Governance Governor
* Prometheus Metrics Exporter (Port 9363)

## Relationships
* Consumes clinical and billing event streams from the Apache Kafka StatefulSet via Native Binary TCP protocol.
* Exports encrypted historical partitions and snapshots to the Compliance Archival Gateway and MinIO Object Storage via HTTPS.
* Forwards security events and query audits to the Audit & Compliance Sidecar Container via gRPC.
* Exposes analytical query endpoints to the API Gateway and reporting services over HTTP/TCP protocols.
* Scrapes telemetry metrics into the Observability Collector Container using Prometheus over HTTP.

## Technology Stack
* ClickHouse: Core columnar database chosen for high-throughput append performance and columnar compression.
* ClickHouse Keeper: Metadata coordination across hybrid Kubernetes nodes for active-active replication.
* Kafka Table Engine (`Engine = Kafka`): Real-time streaming ingestion from Apache Kafka.
* LUKS & PKCS#11/HSM: Encrypted block storage ensuring AES-256 compliance at rest.
* Prometheus: Telemetry and performance metric exposure.

## Rationale
This architecture guarantees sub-second analytical performance without impacting operational databases by offloading heavy reporting workloads to a distributed columnar store. Furthermore, integrated encryption, automated auditing, and retention controllers satisfy rigorous healthcare security and regulatory mandates.