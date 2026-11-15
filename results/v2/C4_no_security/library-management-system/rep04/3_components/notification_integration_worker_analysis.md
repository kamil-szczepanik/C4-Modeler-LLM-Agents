## Overview
The Library Management System is a EU-compliant solution for public and academic libraries to catalogue items and manage circulation. The Notification & Integration Worker handles asynchronous notifications and system integrations.

## Key Elements
* Library Patrons, Librarians and Circulation Staff, Library Administrators
* Patron Web App & Staff Portal (TypeScript/React SPAs)
* API Gateway (Nginx / Spring Cloud Gateway)
* Catalog & Search Service (Java/Spring Boot + Elasticsearch)
* Circulation Service (Java/Spring Boot + PostgreSQL)
* Notification & Integration Worker (Node.js/Python)
* Internal Event Bus (Apache Kafka / RabbitMQ)
* Event Consumer Component (KafkaJS / Kafka-python)
* Routing & Template Engine (Nunjucks / Jinja2)
* Dispatch & Retry Manager (Axios / HTTPX, Redis, Kafka DLQ)
* Audit Logger & Publisher (OpenTelemetry SDK)
* External Systems: Identity Provider, Payment Gateway, Notification Service, Digital Content Providers, EU-hosted Log & Metrics Aggregator
* Managed Kubernetes Cluster (EKS/AKS in EU-central)

## Relationships
* Internal Event Bus -> Event Consumer Component: Consumes domain events via TLS [Apache Kafka]
* Routing & Template Engine -> Dispatch & Retry Manager: Compiles localized messages [Nunjucks / Jinja2]
* Dispatch & Retry Manager -> Notification Service: Sends outbound alerts [HTTPS/REST]
* Dispatch & Retry Manager -> Internal Event Bus: Publishes delivery status events [Apache Kafka]
* Audit Logger & Publisher -> EU-hosted Log & Metrics Aggregator: Forwards structured logs and metrics [OpenTelemetry / TLS]

## Technology Stack
* Node.js / Python: Core runtime for the Notification & Integration Worker
* Apache Kafka: Internal Event Bus for event-driven messaging and native DLQ
* Nunjucks / Jinja2: Templating engines for localized message compilation
* Axios / HTTPX: HTTP clients implementing exponential backoff for REST calls
* Redis: Local queue supporting the Dispatch & Retry Manager
* OpenTelemetry SDK: Instrumentation for end-to-end tracing and auditing
* Managed Kubernetes (EKS/AKS): EU-central deployment with Horizontal Pod Autoscaling based on consumer lag

## Rationale
This architecture uses an event-driven microservices pattern with containerized workers to ensure 99th-percentile search response times under 800 ms. Isolating the Notification & Integration Worker with Kubernetes autoscaling and localized Redis/Kafka retry mechanisms guarantees robust asynchronous delivery while strictly enforcing EU data residency constraints.