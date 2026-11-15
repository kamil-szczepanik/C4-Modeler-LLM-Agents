## Overview
• The Analytics & Reporting Service processes heavy reporting and analytics workloads for the Library Management System.
• It provides secure, asynchronous generation of circulation and engagement reports while enforcing strict EU-only data residency and role-based access control.

## Key Elements
• Analytics & Reporting Service [Container, Container] (Python, FastAPI)
• Circulation Analytics Component [Component] (Python, Pandas)
• Usage & Engagement Reporting Component [Component] (Python, Pandas)
• Report Generation & Export Component [Component] (Python, ReportLab/Openpyxl)
• Report Export Job Queue [Component] (Celery, Redis/RabbitMQ)
• EU-Pinned Object Storage [Component] (S3-compatible storage)
• Primary Database & Read Replica [Container, Container] (PostgreSQL)
• Core API Gateway [Container, Container] (Envoy, Spring Cloud Gateway)

## Relationships
• Core API Gateway -> Analytics & Reporting Service: Initiates async report jobs [gRPC, mTLS]
• Circulation Analytics Component -> Primary Database & Read Replica: Queries analytical data [PostgreSQL Protocol, Read Replica]
• Usage & Engagement Reporting Component -> Primary Database & Read Replica: Queries engagement data [PostgreSQL Protocol, Read Replica]
• Report Generation & Export Component -> Report Export Job Queue: Queues export tasks [AMQP / Redis Protocol]
• Report Generation & Export Component -> EU-Pinned Object Storage: Stores export artifacts [HTTPS, TLS 1.3]

## Technology Stack
• Python, FastAPI: Powers lightweight, high-performance REST and gRPC endpoints for reporting APIs.
• Python, Pandas: Enables efficient in-memory aggregation of large dataset metrics for circulation and usage trends.
• Celery, Redis/RabbitMQ: Manages asynchronous task queues to prevent synchronous HTTP timeouts during heavy report compilation.
• EU-Pinned S3-Compatible Object Storage: Secures exported PDF and CSV artifacts at rest using AES-256 within compliant geographic boundaries.
• PostgreSQL Read Replica: Isolates heavy analytical queries from primary transactional database operations.

## Rationale
• Asynchronous job queuing and dedicated worker pools isolate memory-intensive Pandas and PDF generation tasks from real-time API threads.
• Read-replica routing, strict least-privilege database roles, and EU-pinned object storage protect sensitive patron data while ensuring compliance with EU residency mandates.