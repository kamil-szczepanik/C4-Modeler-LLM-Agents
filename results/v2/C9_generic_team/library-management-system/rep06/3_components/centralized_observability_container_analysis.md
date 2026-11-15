## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. It uses a centralized observability architecture to guarantee high performance and maintain system reliability.

## Key Elements
- Patrons and Library Staff
- API Gateway Container (NGINX / Kong)
- Core Business Logic / Circulation API Container (Microservice / API Runtime)
- Search Engine Container (Elasticsearch / OpenSearch)
- Centralized Observability Container (Observability Platform)

## Relationships
- Upstream Containers to Centralized Observability Container: Ships metrics, logs, and traces asynchronously via OpenTelemetry (OTel) protocols.
- API Gateway Container to Core Business Logic Container: Routes requests using W3C trace context propagation.

## Technology Stack
- OpenTelemetry (OTel): Ensures vendor-neutral, low-overhead metric and trace ingestion.
- W3C Trace Context Headers: Enables automated log-to-trace correlation.
- Circuit-Breaker Pattern: Protects core library operations from observability pipeline failures.
- Infrastructure-as-Code (IaC): Manages dashboards and alert rules to prevent configuration drift.

## Rationale
This architecture ensures strict compliance with EU-only data residency via source PII scrubbing and sliding-window retention. It protects the 99th-percentile search response time (< 800 ms) by decoupling asynchronous telemetry ingestion from critical request paths.