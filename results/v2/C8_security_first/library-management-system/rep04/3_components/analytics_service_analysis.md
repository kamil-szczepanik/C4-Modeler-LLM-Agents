## Overview
The Analytics Service is a container within the Library Management System that processes analytical circulation trends, ROI metrics, and executive reporting. It enables data-driven management for library staff and directors while enforcing strict GDPR compliance and EU data residency.

## Key Elements
* **Users:** Library Staff, Library Administrators / Directors
* **External Systems:** Message Broker (Kafka), EU Cloud Provider's HSM, EU Cloud Object Storage
* **Containers:** API Gateway, Analytics Service (Python / FastAPI, ClickHouse)
* **Components (Analytics Service):** Ingestion Worker (Python / Faust or Celery), Query API (Python / FastAPI), Aggregation Engine (ClickHouse Materialized Views), Report Generation Worker (Python / Celery)

## Relationships
* **API Gateway -> Query API:** Routes analytics queries via internal mTLS and gRPC
* **Message Broker -> Ingestion Worker:** Consumes event messages via Kafka Consumer API
* **Ingestion Worker -> ClickHouse Storage:** Bulk inserts events via ClickHouse Native Protocol
* **Query API -> ClickHouse Storage:** Executes read queries via ClickHouse SQL over HTTP/Native
* **Query API -> Report Generation Worker:** Delegates export tasks via Redis / Message Broker queue
* **Report Generation Worker -> ClickHouse Storage:** Queries historical aggregates via ClickHouse SQL over HTTP

## Technology Stack
* **Language & Framework:** Python / FastAPI for query handling, Python / Celery or Faust for background processing
* **Database & Storage:** ClickHouse with Materialized Views for high-performance aggregations and transparent data encryption (TDE)
* **Communication:** Apache Kafka for event streaming, gRPC and mTLS for internal service-to-service security
* **Security & Observability:** EU Cloud Provider's HSM for key management, OpenTelemetry for tracing, Fluentbit / Vector for log streaming

## Rationale
* The architecture separates real-time ingestion from heavy reporting workloads using dedicated workers, ensuring high-performance search and query responses. 
* Encrypted storage, PII sanitization at ingestion, and strict EU regional backups fully satisfy rigorous data residency and privacy mandates.