## Overview
The Reporting & Analytics Service processes heavy workloads for library administrators while maintaining strict EU-only data residency and protecting core transactional performance. It utilizes a Python/FastAPI backend integrated with PostgreSQL read-replicas, Pandas, and gRPC communication protocols.

## Key Elements
* API Controller (FastAPI Router)
* Report Generation Engine (Pandas / NumPy)
* Data Access Repository (SQLAlchemy)
* Alert Evaluation Worker (Celery / Background Tasks)
* Administration Console
* Circulation & Loan Service
* Notification Dispatcher
* PostgreSQL Database (Read-Replicas)

## Relationships
* API Gateway -> API Controller: Routes HTTP/2 reverse proxy requests
* Circulation & Loan Service -> API Controller: Handles interservice communication via gRPC over TLS 1.3 / mTLS
* API Controller -> Report Generation Engine: Delegates tasks via internal Python function call / task queue
* Report Generation Engine -> Data Access Repository: Fetches pseudonymized data using SQLAlchemy ORM / SQL query
* Data Access Repository -> PostgreSQL Database: Queries analytics data using SQL / PostgreSQL protocol
* Alert Evaluation Worker -> Notification Dispatcher: Triggers threshold alerts via gRPC over TLS 1.3

## Technology Stack
* Python / FastAPI: Core framework for low-latency asynchronous API handling
* Pandas / NumPy: Processes heavy data frames for executive reports
* SQLAlchemy: Provides secure, parameterized ORM-based data access
* Celery: Manages asynchronous background worker tasks and queues
* PostgreSQL 15: Isolates analytical queries on read-replicas for performance

## Rationale
This architecture decouples heavy analytical workloads from core transactional services using dedicated data-science libraries and read-replicas. It ensures strict EU data compliance, robust security controls, and high-performance reporting without impacting staff circulation workflows.