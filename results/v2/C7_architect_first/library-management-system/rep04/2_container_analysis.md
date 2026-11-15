## Overview
The Library Management System provides physical and digital item cataloguing, circulation management, and self-service patron portals. It enforces strict EU-only data residency and maintains a 99th-percentile search response time under 800 ms.

## Key Elements
* Web App (SPA): React hosted on Nginx
* API Gateway: Spring Cloud Gateway with OAuth2/OIDC
* Core Services Container: Spring Boot microservices
* Search Container: Elasticsearch cluster
* Worker Container: Python/Celery with RabbitMQ/Redis broker
* Telemetry Container: Prometheus, Grafana, and Fluentbit
* Database: PostgreSQL with AES-256 encryption

## Relationships
* SPA to API Gateway: HTTPS with TLS 1.3
* Gateway to Core Services: gRPC / internal REST with mTLS
* Core Services to PostgreSQL & Elasticsearch: Restricted private EU subnet
* Core Services to Search: Asynchronous change data capture (CDC) sync

## Technology Stack
* React & Nginx: Frontend delivery for patrons and staff
* Spring Boot & Spring Cloud Gateway: Microservice orchestration and API routing
* PostgreSQL: Transactional relational data storage
* Elasticsearch: High-performance catalogue searching (R-05 compliance)
* Kubernetes (Terraform): Infrastructure deployment pinned to EU cloud regions

## Rationale
Separating the Elasticsearch container via asynchronous CDC prevents heavy queries from locking transactional PostgreSQL tables to meet the <800ms search requirement. Deploying on EU-pinned Kubernetes clusters with strict network isolation and mTLS satisfies data residency constraints and enterprise security mandates.