## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures EU-only data residency while maintaining a 99th-percentile search response under 800ms.

## Key Elements
* Patrons / Library Members and Librarians / Staff (Users)
* Web Application (React, TypeScript)
* API Gateway (Kong / Nginx)
* Core Business Service (Java, Spring Boot)
* Search Service (Elasticsearch)
* Database (PostgreSQL)
* Redis Cache (Redis)
  * Cache Data Store (Redis In-Memory Engine)
  * Eviction & TTL Manager
  * Connection & Command Router (Redis Cluster / Sentinel Interface)
* Notification Worker (Node.js)
* External Payment Gateway, Digital Content Providers / e-Book Vendors, Notification Service, External Enterprise Search Service (External Systems)

## Relationships
* Core Business Service -> Connection & Command Router: Routes read/write and TTL configuration commands via TCP/RESP (Pooled)
* Connection & Command Router -> Cache Data Store: Manages internal Redis memory operations
* Core Business Service -> Database: Queries persistent data via PostgreSQL protocol

## Technology Stack
* React & TypeScript: Powers the Web Application for responsive self-service portals
* Java & Spring Boot: Implements the Core Business Service for robust domain logic
* PostgreSQL: Provides reliable relational storage respecting EU-only data residency
* Elasticsearch: Delivers high-performance search to meet the <800ms NFR
* Redis: Accelerates access and reduces database load via in-memory caching

## Rationale
This architecture uses an in-memory caching layer with connection pooling to satisfy high-concurrency performance requirements. It strictly maintains data residency constraints by keeping sensitive processing and volatile session data within compliant boundaries.