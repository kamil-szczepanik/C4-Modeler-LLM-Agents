## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and high-performance search requirements.

## Key Elements
- Patrons / Library Members and Librarians / Staff (Users)
- External Payment Gateway, Digital Content Providers, Notification Service, External Enterprise Search Service (External Systems)
- Web Application (React, TypeScript), API Gateway (Kong / Nginx)
- Core Business Service (Java, Spring Boot), Search Service (Elasticsearch), Notification Worker (Node.js)
- Database (PostgreSQL) and Redis Cache (Redis)
- Database Components: Relational Storage Engine (PostgreSQL 15), Connection Pooler (PgBouncer), Audit Logging Extension (`pgAudit`), Full-Text Search Index (PostgreSQL GIN Indexes)

## Relationships
- Core Business Service -> Connection Pooler (PgBouncer): Database queries and transactions [TCP/SQL via JDBC, port 6432]
- Connection Pooler -> Relational Storage Engine: Proxied client connections [TCP, local socket]
- Relational Storage Engine -> Audit Logging Extension (`pgAudit`): Writes security and data access event logs [Internal PostgreSQL Hook]
- Core Business Service -> Database: Reads and writes persistent data [TCP]

## Technology Stack
- PostgreSQL 15: Core relational engine for ACID-compliant storage of patrons, items, and transactions within EU infrastructure
- PgBouncer: Connection pooler to manage concurrent connections and meet performance NFRs
- `pgAudit`: Extension for strict database-level activity logging to satisfy EU compliance
- PostgreSQL GIN Indexes: Native full-text search index for fast metadata filtering

## Rationale
This architecture ensures strict EU data residency compliance while supporting high-performance search and scalable circulation workflows. Component-level isolation via connection pooling and auditing guarantees reliability under load.