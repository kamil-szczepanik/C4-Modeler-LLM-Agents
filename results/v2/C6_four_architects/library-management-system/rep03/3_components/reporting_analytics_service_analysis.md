## Overview
The Reporting & Analytics Service is a Python/FastAPI container within the Library Management System responsible for handling complex analytical workloads and report generation. It ensures performance and EU-only data residency without impacting operational databases.

## Key Elements
- Report Orchestration Engine (Python, Celery)
- Analytics Query Processor (Python, Pandas/SQLAlchemy)
- Export Formatter (Python, ReportLab/Openpyxl)
- Data Ingestion Component (Python, Faust/Kafka-Python)
- API Gateway (Nginx, Kong)
- Notification & Event Bus (Apache Kafka)
- Database (PostgreSQL)
- Distributed Cache (Redis)
- Object Storage (MinIO, S3-compatible)

## Relationships
- API Gateway -> Report Orchestration Engine: Forwards generation requests [gRPC over TLS]
- Report Orchestration Engine -> Notification & Event Bus: Consumes domain events [Kafka Protocol]
- Report Orchestration Engine -> Async Worker: Delegates tasks [Redis Broker Protocol]
- Report Orchestration Engine -> Export Formatter: Renders exports [Direct Function Call]
- Report Orchestration Engine -> Analytics Query Processor: Invokes queries [Python Asyncio]
- Analytics Query Processor -> Database: Queries analytical views [SQL over TLS / psycopg2]
- Analytics Query Processor -> Distributed Cache: Caches aggregates [RESP over TLS]
- Data Ingestion Component -> Notification & Event Bus: Consumes raw events [Kafka Protocol]
- Data Ingestion Component -> Database: Persists metrics [SQL over TLS]
- Data Ingestion Component -> Analytics Query Processor: Invalidates cache [RESP over TLS]
- Export Formatter -> Object Storage: Stores large reports [HTTPS / AWS S3 API]

## Technology Stack
- Python with FastAPI: High-performance asynchronous API framework
- Celery: Asynchronous task queue for heavy report orchestration workloads
- Pandas and SQLAlchemy: Data processing and analytical querying
- ReportLab and Openpyxl: PDF and spreadsheet export rendering
- Apache Kafka: High-throughput event ingestion bus
- PostgreSQL: Read-optimized data store for compliance with EU-only data residency
- Redis: Distributed caching and broker protocol implementation
- MinIO: S3-compatible local object storage ensuring regional data residency compliance

## Rationale
This architecture decouples heavy analytical workloads and real-time event ingestion from synchronous API traffic, protecting the FastAPI event loop. Utilizing local S3 storage, EU-hosted PostgreSQL, and encrypted protocols strictly enforces regional data residency constraints while meeting high-performance targets.