## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It guarantees strict EU-only data residency and sub-800ms search latency.

## Key Elements
- **Patron Web/Mobile App:** React / React Native UI prioritizing WCAG 2.1 AA accessibility.
- **Staff Dashboard:** Angular UI for administrative cataloging and branch operations.
- **Self-Service Check-In/Out Kiosk:** Electron / React lightweight container supporting offline fallback.
- **API Gateway:** Kong / Nginx single entry point enforcing TLS, mTLS, and OAuth2.
- **Core Domain Services:** Java / Spring Boot microservices handling circulation and cataloging.
- **Search Engine:** Elasticsearch container guaranteeing <800ms response times (R-05).
- **Data Storage:** PostgreSQL transactional database hosted exclusively in the EU.
- **Async Message Broker:** Apache Kafka for decoupling batch tasks and event distribution.
- **Notification Dispatcher:** Python / FastAPI service with rate-limiting and DLQ integration.
- **Observability Stack:** OpenTelemetry collector, Prometheus, and Grafana routed to an EU-Resident Log & Audit Sink.

## Relationships
- **Patrons & Staff** access the **Patron App**, **Staff Dashboard**, and **Kiosks** via HTTPS and mTLS.
- **API Gateway** routes traffic to **Core Domain Services** and **Search Engine** using gRPC and HTTPS.
- **Core Domain Services** persist transactions to **PostgreSQL** and publish events to **Apache Kafka**.
- **Notification Dispatcher** consumes events from **Kafka** and integrates with the external **EU Notification Service**.
- **Observability Stack** ingests metrics and traces from all microservices and edge kiosks.

## Technology Stack
- **Frontend/Clients:** React, React Native, Angular, Electron for diverse cross-platform and web interfaces.
- **Backend Services:** Java Spring Boot, Python FastAPI for robust microservice architecture.
- **Routing & Security:** Kong / Nginx, OAuth2, TLS, mTLS for secure perimeter control.
- **Data & Search:** PostgreSQL, Elasticsearch for ACID compliance and high-performance catalog search.
- **Messaging:** Apache Kafka for resilient asynchronous event-driven decoupling.
- **Operations:** OpenTelemetry, Prometheus, Grafana for centralized EU-compliant observability.

## Rationale
This architecture decouples high-traffic patron portals from resource-intensive staff workflows to consistently achieve sub-800ms search latency SLAs (R-05). Deploying all active containers and data stores exclusively within EU cloud availability zones strictly enforces EU data residency constraints.