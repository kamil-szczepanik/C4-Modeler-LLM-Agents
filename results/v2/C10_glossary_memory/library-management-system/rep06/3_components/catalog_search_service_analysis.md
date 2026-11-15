## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital assets, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and maintains a sub-800ms search response SLA.

## Key Elements
- Library Patrons, Librarians, Library Administrators [Persons]
- Patron Web App (React, TypeScript), Staff Web App (Angular, TypeScript) [Containers]
- Core API Gateway (Envoy, Spring Cloud Gateway) [Container]
- Catalog & Search Service (Java, Spring Boot, Elasticsearch): Contains Search Controller, Search Engine Client, Catalog Manager, Metadata Indexer, and Digital Asset Synchronizer [Container & Components]
- Circulation Service (Java, Spring Boot) [Container]
- Notification Service (Node.js, TypeScript, RabbitMQ/Kafka) [Container]
- Analytics & Reporting Service (Python, FastAPI) [Container]
- Primary Database & Read Replica (PostgreSQL), Elasticsearch Cluster [Containers]
- EU Identity Provider (IdP), Payment Gateway, Digital Content Providers [External Systems]

## Relationships
- Library Patrons / Librarians -> Library Management System [HTTPS (TLS 1.3)]
- Patron Web App / Staff Web App -> Core API Gateway [HTTPS, TLS 1.3]
- Core API Gateway -> Catalog & Search Service [gRPC / HTTPS, mTLS]
- Search Controller -> Search Engine Client [In-Memory Java API]
- Search Engine Client -> Elasticsearch Cluster [Transport Client / REST over HTTPS, mTLS]
- Catalog Manager -> Primary Database & Read Replica [PostgreSQL Protocol, SCRAM-SHA-256, TLS]
- Catalog Manager -> Digital Content Providers [HTTPS (REST API), TLS 1.3, Certificate Pinning]
- Metadata Indexer -> Elasticsearch Cluster [REST over HTTPS, mTLS]

## Technology Stack
- Java & Spring Boot: Powers high-performance microservices like the Catalog & Search Service.
- Elasticsearch: Delivers high-performance faceted search to meet the sub-800ms SLA (R-05).
- PostgreSQL: Manages transactional data with strict EU-only data residency constraints.
- Kubernetes: Containerizes services with Horizontal Pod Autoscalers (HPA) and EU-centralized cloud deployment.
- Envoy & Spring Cloud Gateway: Manages secure ingress traffic and API routing.
- OpenTelemetry & Prometheus: Provides distributed tracing and latency metrics.

## Rationale
This architecture uses Elasticsearch to guarantee the sub-800ms search SLA while decoupling indexing and digital synchronization for high resilience. Strict EU-centralized deployments and mTLS encryption ensure compliance with EU data residency and security mandates.