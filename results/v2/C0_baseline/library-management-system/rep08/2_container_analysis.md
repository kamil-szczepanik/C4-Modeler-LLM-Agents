## Overview
The Library Management System is a comprehensive platform for public and academic libraries designed to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and maintains a sub-800ms search response time.

## Key Elements
- **Users:** Library Member (Patron), Librarian/Staff, Library Administrator
- **External Systems:** EU Identity Provider, EU Payment Gateway, EU-hosted Log & Telemetry Aggregator
- **Containers:** API Gateway, Patron Web App, Catalog & Search Service, Circulation & Payments Service, Admin & Reporting Service
- **Data Stores:** Elasticsearch, PostgreSQL (EU-hosted)

## Relationships
- **External Access:** Patrons, Librarians, and Administrators access the API Gateway via HTTPS (TLS 1.3).
- **Frontend to Backend:** Patron Web App communicates with internal microservices via gRPC over a private network.
- **Service Communication:** Microservices enforce mutual TLS (mTLS) via Istio service mesh.
- **External Integrations:** Circulation & Payments Service connects to the EU Payment Gateway via HTTPS/REST.
- **Observability:** Containers ship Prometheus metrics and sanitized JSON logs to the EU-hosted Log & Telemetry Aggregator.

## Technology Stack
- **API Gateway:** NGINX / Envoy for edge routing and TLS termination.
- **Frontend:** React / TypeScript Single Page App served via NGINX.
- **Backend Services:** Kotlin / Spring Boot (Catalog & Search), Java 17 / Spring Boot (Circulation & Payments), Python / FastAPI (Admin & Reporting).
- **Databases & Search:** PostgreSQL for transactional data, Elasticsearch for search indexing.
- **Orchestration & Security:** Kubernetes (StatefulSets, HPA), Istio (Service Mesh, mTLS, OPA AuthorizationPolicy).

## Rationale
This architecture decouples heavy search and reporting workloads from core circulation to strictly guarantee the <800ms search SLA and ensure independent service scaling. Furthermore, it enforces EU-only data residency, strict PII encryption, and mTLS security to meet stringent regulatory and compliance requirements.