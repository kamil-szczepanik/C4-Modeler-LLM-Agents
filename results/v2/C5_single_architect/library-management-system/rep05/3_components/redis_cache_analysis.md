## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures EU-only data residency while delivering high-performance search responses.

## Key Elements
- **Library Patron & Librarian / Staff**: Primary system users
- **Web Application**: React, TypeScript, Nginx
- **API Gateway**: Spring Cloud Gateway / Kong
- **Core Domain Service**: Java, Spring Boot
- **Search Service**: Python, FastAPI, Elasticsearch
- **Background Worker Service**: Python/Celery or Java/Spring Batch
- **PostgreSQL Database**: PostgreSQL
- **Redis Cache**: Redis 7.x containing Session Store Module, Catalogue Query Cache Module, and Cache Eviction & Expiry Manager
- **External Systems**: Payment Gateway, Notification Service, DRM Provider

## Relationships
- **Core Domain Service -> Session Store Module**: Validates tokens and retrieves user state [RESP3/TCP]
- **Search Service -> Catalogue Query Cache Module**: Executes cache-aside pattern for frequent catalogue queries [RESP3/TCP]
- **Core Domain Service & Search Service -> Redis Cache**: Accesses cache for sessions and queries [TCP]

## Technology Stack
- **Redis 7.x**: Chosen for in-memory performance and low-latency data access
- **RESP3 Protocol**: Enables efficient, low-latency communication over TCP
- **volatile-lru policies & TTLs**: Enforces strict memory management for EU-only data residency

## Rationale
This architecture uses Redis 7.x with RESP3/TCP and targeted caching modules to accelerate frequent catalogue queries, ensuring the 99th-percentile search response stays below 800 ms. Strict TTLs and LRU eviction policies maintain compliance with EU-only data residency constraints.