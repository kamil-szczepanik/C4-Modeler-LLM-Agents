## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It ensures strict EU data residency while maintaining high-performance search capabilities.

## Key Elements
* Library Patron and Librarian / Staff (Users)
* Web Application (React/TypeScript, Nginx)
* API Gateway (Spring Cloud Gateway / Kong)
* Core Domain Service (Java/Spring Boot)
* Search Service (Python/FastAPI, Elasticsearch)
* Background Worker Service (Python/Celery or Java/Spring Batch)
* PostgreSQL Database
* Redis Cache
* Payment Gateway, Notification Service, and DRM Provider (External Systems)

## Relationships
* Web Application calls API Gateway via HTTPS/JSON
* API Gateway routes search queries to Search Service via gRPC
* Core Domain Service and Search Service access Redis Cache via TCP
* Core Domain Service persists data in PostgreSQL (EU-hosted)
* Background Worker Service communicates with Notification Service and DRM Provider via HTTPS/JSON

## Technology Stack
* React/TypeScript with Nginx: Powers the responsive single-page Web Application
* Spring Cloud Gateway/Kong: Manages secure API entry routing
* Java/Spring Boot: Implements robust Core Domain business logic
* Python/FastAPI with Elasticsearch: Delivers high-performance search to meet <800ms response targets
* PostgreSQL: Guarantees compliance with EU-only data residency constraints
* Redis: Accelerates frequent catalogue queries and session management

## Rationale
This container architecture isolates high-performance search queries to dedicated components to meet strict response time requirements. Furthermore, it utilizes regionally restricted databases to enforce data residency mandates.