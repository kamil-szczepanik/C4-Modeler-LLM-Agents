## Overview
[The system is a Library Management System designed to catalogue items, manage circulation, and provide self-service portals. Its core purpose is to deliver fast catalogue discovery and secure search capabilities for patrons and staff while enforcing strict EU data residency.]

## Key Elements
- Library Patrons
- Librarians / Circulation Staff
- Library Administrator
- API Gateway (Nginx/Kong)
- Search Service (Elasticsearch)
- RabbitMQ
- Search API Controller
- Indexing Consumer
- Query Processor
- Search Index

## Relationships
- API Gateway -> Search Service: Routes search queries via gRPC [Protocol Buffers over TLS 1.3]
- Indexing Consumer -> RabbitMQ: Consumes domain events via AMQPS with mTLS
- Search API Controller -> Query Processor: Validates JWTs and maps requests to Search Profiles
- Query Processor -> Search Index: Executes parameterized Elasticsearch Query DSL with Field-Level Security

## Technology Stack
- Elasticsearch: Selected for high-performance catalogue discovery meeting sub-800ms search latency (R-05)
- RabbitMQ: Used as the event broker for near real-time item synchronization
- gRPC / Protocol Buffers: Provides low-latency transport over TLS 1.3 for search queries
- JSON Web Tokens (JWT): Enforces role-based access control (RBAC) at the API layer

## Rationale
[This architecture uses Elasticsearch and optimized search profiles to meet strict performance requirements under 800ms. It enforces EU data residency and security controls through encrypted transport, mTLS, and query-level access restrictions.]