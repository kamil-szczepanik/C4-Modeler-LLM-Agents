## Overview
The Library Management System provides self-service portals, circulation management, and cataloguing for public and academic libraries with EU-only data residency and strict search SLAs. It utilizes an Nginx/Kong API Gateway to ensure secure, low-latency routing and token validation.

## Key Elements
* Library Patrons & Staff
* EU-edge Reverse Proxy
* API Gateway (Nginx/Kong) with internal components: Routing & Upstream Proxy, Auth & Token Validation Filter, Rate Limiting & Throttling Engine, Telemetry & Logging Exporter, and Request Transformation & Validation Engine
* Circulation & Cataloguing Service (Node.js/TypeScript)
* Core Search Engine (Elasticsearch)
* Database (PostgreSQL)
* Third-Party Digital Content Providers
* Payment Gateway
* Notification Service

## Relationships
* Library Patrons & Staff -> EU-edge Reverse Proxy [HTTPS/TLS 1.3, OIDC/OAuth2]
* EU-edge Reverse Proxy -> Self-Service Web App & Admin/Staff Portal [HTTPS]
* Self-Service Web App & Admin/Staff Portal -> API Gateway [HTTPS/REST with JWT]
* API Gateway -> Circulation & Cataloguing Service [gRPC/Internal, mTLS]
* Circulation & Cataloguing Service -> Core Search Engine [TCP]
* Circulation & Cataloguing Service -> Database [PostgreSQL Wire Protocol]

## Technology Stack
* Nginx/Kong: Powers the API Gateway for routing, rate limiting, and OAuth2/OIDC token validation.
* Redis: High-availability clustered data store for distributed rate-limiting counters.
* Node.js/TypeScript: Implements the Circulation & Cataloguing Service.
* Elasticsearch: Core Search Engine hosted in EU regions to meet the R-05 search SLA (<800ms).
* PostgreSQL: Managed database with AES-256 encryption at rest to enforce EU-only data residency.
* OpenTelemetry: Emits structured access logs, metrics, and distributed traces via OTLP/gRPC.

## Rationale
This architecture enforces strict EU data residency and robust security controls at the API Gateway before requests reach internal microservices. Distributed rate limiting, schema validation, and optimized Elasticsearch integration guarantee high performance and low-latency search SLAs under peak load.