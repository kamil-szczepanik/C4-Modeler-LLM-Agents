## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It ensures EU-only data residency and sub-second search responses.

## Key Elements
* API Gateway (Kong / NGINX)
* Search & Catalog Service (Java / Spring Boot + Elasticsearch)
* Core Circulation Service (Node.js / Go + PostgreSQL)
* Analytics Service (Python / FastAPI + ClickHouse)
* Notification Worker (Python / Celery or Go)
* Message Broker (Apache Kafka / RabbitMQ)
* Audit Logging Sidecar (Fluentbit / Vector)
* EU Kubernetes Cluster and EU Cloud Provider's HSM

## Relationships
* Users to API Gateway via HTTPS / TLS 1.3
* API Gateway to Core Services via internal mTLS and gRPC
* Core Circulation Service to Message Broker via AMQP / gRPC
* Message Broker to Notification Worker and Analytics Service via Kafka topics
* Audit Logging Sidecar to external Audit Log Stream via TLS

## Technology Stack
* Kong / NGINX for edge routing and OAuth 2.0 / OIDC authentication
* Elasticsearch for catalog search to satisfy the <800ms performance SLA
* PostgreSQL for relational core circulation data storage
* ClickHouse for analytical processing of circulation trends
* Apache Kafka / RabbitMQ for event-driven asynchronous messaging
* Kubernetes with OpenTelemetry and Fluentbit for orchestration, tracing, and logging

## Rationale
This containerised, event-driven architecture isolates resource-intensive search and analytics workloads to guarantee sub-second performance. Strict security controls, container hardening, and localized data stores ensure full compliance with EU-only data residency mandates.