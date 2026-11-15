## Overview
The Analytics & Reporting Container provides high-performance operational dashboards and compliance reports for Hospital Administrators and Compliance Officers. It operates within a hybrid cloud infrastructure, ensuring HIPAA and GDPR compliance while maintaining 99.99% availability.

## Key Elements
- CDC Ingestion Worker (Python / Go)
- Query & Aggregation Service (Node.js / Express or Java Spring Boot)
- Report Generation Engine (Node.js)
- Reporting API / BFF
- Scheduler & Notification Dispatcher (Node.js / BullMQ)
- Analytics Database (ClickHouse / Apache Pinot)
- Object Storage (S3-compatible)

## Relationships
- CDC Ingestion Worker -> Apache Kafka: Consumes streaming data [Kafka Protocol]
- Query & Aggregation Service -> ClickHouse / Apache Pinot: Executes analytical queries [Native TCP / HTTP]
- Report Generation Engine -> S3-compatible Object Storage: Persists temporary export payloads [HTTPS / TLS]
- Scheduler & Notification Dispatcher -> Report Generation Engine: Triggers asynchronous generation [BullMQ Redis]
- Scheduler & Notification Dispatcher -> Email Gateway: Dispatches alerts and notifications [HTTPS / TLS]
- Reporting API -> API Gateway: Exposes endpoints [REST / gRPC]

## Technology Stack
- ClickHouse / Apache Pinot: Columnar store chosen for sub-second analytical queries and 10-year data retention
- Python / Go: High-throughput ingestion of Debezium CDC streams
- Node.js: Asynchronous processing for report generation, scheduling, and API routing
- BullMQ / Redis: Robust queue management for time-zone-aware scheduled report dispatch
- S3-compatible Storage: Secure, ephemeral staging for generated CSV and PDF reports

## Rationale
This architecture balances heavy analytical workloads with strict HIPAA and GDPR security mandates. Isolated internal components, columnar storage, and strict access controls ensure sub-second performance without impacting primary clinical workflows.