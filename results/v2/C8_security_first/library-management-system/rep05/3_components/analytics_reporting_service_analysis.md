## Overview
[Library Management System Analytics & Reporting Service: Handles operational reporting, dashboards, and GDPR-compliant data exports for public and academic libraries.]

## Key Elements
- Analytics & Reporting Service (Python / FastAPI / Pandas)
- API Router / Controller (FastAPI)
- Aggregation & Processing Engine (Pandas)
- Export Generator & Scheduler & Task Dispatcher
- Notification & Delivery Dispatcher & Data Access Repository
- PostgreSQL (Read-Replica) & Redis (Backing Celery/Locks)
- Object Storage & Notification Engine

## Relationships
- Staff Management Console -> API Router: Queries dashboards and requests reports [HTTPS / REST over TLS 1.3]
- API Router -> Data Access Repository: Executes queries with read-only roles [SQL over mTLS / TLS 1.3]
- Export Generator -> Object Storage: Uploads encrypted PDF/CSV reports [HTTPS / TLS 1.3]
- Notification & Delivery Dispatcher -> Notification Engine: Dispatches scheduled report alerts [AMQP over TLS]

## Technology Stack
- Python (FastAPI): High-performance asynchronous web framework for REST APIs
- Pandas: In-memory data processing and aggregation for complex analytics
- PostgreSQL: Relational database utilizing read-replicas to isolate analytics from transactions
- Redis: Backing store for Celery worker queues and distributed locking (Redlock)
- OAuth2/JWT: Role-Based Access Control for authorized branch scoping

## Rationale
[Isolating the analytics container with dedicated read-replicas and async workers prevents resource starvation and ensures 3-second dashboard rendering SLAs. Enforcing mTLS, column-level masking, and EU region-locked storage satisfies stringent GDPR data residency mandates.]