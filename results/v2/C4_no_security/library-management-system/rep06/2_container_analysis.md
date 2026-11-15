## Overview
The Library Management System is a solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. The architecture prioritizes strict EU data residency and high-performance search capabilities.

## Key Elements
* Library Patrons, Library Staff, Library Administrators
* External Systems: Payment Gateway, LDAP, Digital Content Providers, Notification Service, APM Tool
* Containers: API Gateway (Kong/NGINX), Self-Service Portal & Staff Dashboard (React/TypeScript), Core API Application (Spring Boot/Java), Search Engine (OpenSearch), Primary Database (Managed PostgreSQL), Message Broker (Kafka/RabbitMQ), Async Workers
* Infrastructure: Kubernetes cluster with Istio service mesh, EU-hosted private VPC

## Relationships
* Patrons and Staff interact with portals via HTTPS/JSON.
* Portals and external clients communicate via Kong/NGINX API Gateway using HTTPS/TLS.
* Core API communicates with Managed PostgreSQL and OpenSearch via private VPC network using gRPC/REST over TLS.
* Core API and Async Workers publish/consume events via Message Broker using AMQP/Kafka protocols.
* OpenTelemetry sidecars stream metrics to the APM Tool.

## Technology Stack
* Frontend: React/TypeScript Single Page Applications served via CDN for localization and accessibility.
* Gateway: Kong or NGINX for rate limiting and TLS termination.
* Backend & Workers: Spring Boot / Java for domain logic and background processing.
* Storage: Managed PostgreSQL (EU regions) for relational data and transactional integrity.
* Search: OpenSearch (EU region) to isolate heavy catalogue queries.
* Infrastructure: Kubernetes (EKS/AKS) with Istio mTLS service mesh and Horizontal Pod Autoscalers.

## Rationale
This architecture ensures strict compliance with EU-only data residency requirements through regional cloud deployments and isolates heavy catalogue queries into an OpenSearch container to consistently meet the sub-800ms search latency requirement. Kubernetes orchestration with HPA and dedicated node groups guarantees system stability during peak term-start traffic spikes.