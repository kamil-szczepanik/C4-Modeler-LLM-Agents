## Overview
- Library Management System for public and academic libraries to catalogue items, manage circulation, and provide self-service portals.
- Ensures EU-only data residency and sub-800ms search response times via a dedicated Elasticsearch search engine.

## Key Elements
- Library Patron and Library Staff (Users)
- External Identity Provider, Digital Content Providers, Third-Party Payment Processor, External Notification Gateway, EU-certified Cloud Provider Infrastructure
- Next.js / Node.js TypeScript (Web Application / API Gateway)
- Spring Boot Java (Catalog Service, Circulation Service)
- Python FastAPI (Notification Service)
- PostgreSQL (PostgreSQL)
- Elasticsearch (Elasticsearch container with internal components: Query Parsing & Routing Engine, Distributed Inverted Index, Cluster Coordinator, Faceted Aggregation Engine, Fuzzy Matcher)
- Apache Kafka / RabbitMQ (Event Bus)
- OpenTelemetry (Observability Backend)

## Relationships
- Catalog Service -> Elasticsearch: Queries index via REST/HTTPS with mTLS
- Elasticsearch Query Parsing & Routing Engine -> Distributed Inverted Index, Faceted Aggregation Engine, Fuzzy Matcher: Internal IPC
- Elasticsearch -> OpenTelemetry: Exports metrics via Prometheus exporters
- Elasticsearch -> External Identity Provider: Authenticates via OIDC/SAML

## Technology Stack
- Elasticsearch on Kubernetes via ECK Operator: Automates operations and ensures self-healing within EU cloud
- Lucene-based Distributed Inverted Index: Delivers sub-800ms P99 search latency (R-05)
- OpenTelemetry & Prometheus: Real-time heap, GC, and query-latency monitoring
- External Secrets Operator: Dynamic credential injection for security

## Rationale
- Meets the strict EU data residency constraint by deploying exclusively within EU-certified cloud infrastructure.
- Isolates routing, aggregation, and fuzzy-matching components to guarantee the R-05 sub-800ms P99 search latency SLA.