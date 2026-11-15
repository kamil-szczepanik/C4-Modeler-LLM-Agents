## Overview
The Library Management System provides public and academic libraries with digital/physical cataloging, circulation management, and self-service portals. It is architected as a distributed microservices platform enforcing EU-only data residency and sub-800ms search performance.

## Key Elements
- Library Patron and Librarian / Staff (Users)
- Payment Gateway, Notification Service, Digital Content Provider (External Systems)
- Web Application (React, Nginx)
- API Gateway (Envoy)
- Core Domain Microservice (Java 17, Spring Boot)
- Search Microservice (Elasticsearch)
- Database (PostgreSQL)
- Async Worker (Python, Celery)
- Message Broker (RabbitMQ)
- Observability Stack (Prometheus, Grafana, OpenTelemetry Collector)
- Secure Vault (HashiCorp Vault)

## Relationships
- Users to Web Application via HTTPS
- Web Application to API Gateway via HTTPS
- API Gateway to Core Domain and Search Microservices via mTLS, REST/JSON, and RBAC
- Core Domain to PostgreSQL via JDBC
- Core Domain to RabbitMQ via AMQPS for asynchronous catalog indexing events
- Async Worker to RabbitMQ via AMQPS for background payment and notification jobs
- Observability Stack scrapes metrics via Prometheus/OpenTelemetry

## Technology Stack
- React & Nginx: Powers self-service portals for low latency
- Envoy: Handles high-performance routing, mTLS termination, and tracing
- Java 17 & Spring Boot: Delivers reliable core domain circulation logic
- Elasticsearch: Satisfies R-05 (<800ms P99 search) via dedicated indexing
- PostgreSQL: Stores relational data with enforced EU data residency
- Python & Celery with RabbitMQ: Manages asynchronous workloads and event-driven updates
- Prometheus, Grafana, OpenTelemetry: Centralizes tracing and metrics
- HashiCorp Vault: Securely injects dynamic runtime secrets and TLS certificates

## Rationale
Decoupling search via asynchronous RabbitMQ events protects P99 search latencies under 800ms against database lock contention. Strict cryptographic controls (mTLS, AES-256 storage, and AMQPS) guarantee compliance with EU-only data residency and rigorous security mandates.