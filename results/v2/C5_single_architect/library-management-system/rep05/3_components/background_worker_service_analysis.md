## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It meets EU data residency constraints and delivers high-performance searches under 800 ms.

## Key Elements
- **Library Patron & Librarian / Staff**: Primary system users
- **Web Application**: React, TypeScript, Nginx
- **API Gateway**: Spring Cloud Gateway / Kong
- **Core Domain Service**: Java, Spring Boot
- **Search Service**: Python, FastAPI, Elasticsearch
- **Background Worker Service**: Python with Celery, Redis
- **PostgreSQL Database & Redis Cache**: Data storage layers
- **External Systems**: Payment Gateway, Notification Service, DRM Provider

## Relationships
- **Background Worker Service -> Notification Service**: Sends notifications [HTTPS/JSON]
- **Background Worker Service -> DRM Provider**: Provisions digital rights [HTTPS/JSON]
- **Maintenance Job Scheduler -> PostgreSQL Database**: Updates circulations [TCP/Postgres]
- **Task Dispatcher -> Redis**: Consumes messages [TCP]

## Technology Stack
- **Python with Celery**: Selected for distributed asynchronous task queues and I/O-bound integrations
- **Redis**: Reused as message broker and cache
- **PostgreSQL**: Primary transactional database ensuring EU data residency
- **Elasticsearch**: Powers high-performance search queries

## Rationale
This architecture ensures low-latency performance and reliable asynchronous processing for external integrations. The technology stack balances developer efficiency with strict data residency and response-time constraints.