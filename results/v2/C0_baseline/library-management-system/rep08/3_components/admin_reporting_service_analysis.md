## Overview
[The Admin & Reporting Service provides administrative insights, compliance logging, and scheduled report generation for the Library Management System. It strictly enforces EU data residency and role-based access control.]

## Key Elements
- Admin & Reporting Service (Python / FastAPI)
- Audit Log Processor (Python / Celery)
- Reporting Engine (Python / ReportLab / Pandas)
- Admin API Controller (FastAPI)
- Query Caching Layer (Redis)
- PostgreSQL (EU-hosted)
- EU-hosted Object Storage (MinIO / AWS S3 EU-Central)

## Relationships
- API Gateway -> Admin API Controller: Routes admin requests [gRPC / mTLS]
- Admin API Controller -> Redis: Reads cached KPIs [Redis Protocol / TLS]
- Admin API Controller -> Celery Broker: Dispatches report tasks [AMQP / TLS]
- Reporting Engine -> PostgreSQL: Executes analytical queries [Database Protocol]
- Reporting Engine -> EU-hosted Object Storage: Stores exports [TLS]
- Audit Log Processor -> EU-hosted Log & Telemetry Aggregator: Ships logs [TLS]

## Technology Stack
- Python / FastAPI: High-performance asynchronous control plane for admin APIs
- Pandas / ReportLab: Efficient data aggregation and CSV/PDF report generation
- Celery / Redis: Asynchronous task queue and query caching to prevent database starvation
- PostgreSQL: Relational store with column-level PII encryption

## Rationale
[Component decomposition isolates heavy analytical workloads from the API control plane to maintain performance. Strict encryption, caching, and 24-hour storage lifecycles fulfill EU compliance and security constraints.]