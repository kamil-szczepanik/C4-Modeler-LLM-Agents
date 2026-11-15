## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It ensures high-performance discovery and strict EU data residency compliance.

## Key Elements
- **Users**: Library Patrons, Librarians, Library Administrators
- **Frontend Container**: React/TypeScript Single Page Application hosted on an EU CDN
- **API Gateway**: Nginx/Kong reverse proxy
- **Core Containers**: Catalog & Search Service (Node.js/Go, Elasticsearch), Circulation & Core Service (Java/Spring Boot, PostgreSQL), Notification Dispatcher (Python/FastAPI), Audit Logging Container (Node.js)
- **Infrastructure**: EU-hosted Kubernetes cluster (AWS EKS/Scaleway), Service Mesh (Istio/Linkerd), RabbitMQ/Kafka message broker
- **External Services**: Identity Provider, Payment Gateway, Notification Service, Observability Platform

## Relationships
- **Patrons/Librarians to Frontend**: HTTPS over TLS 1.3
- **Frontend to API Gateway**: HTTPS / REST APIs
- **API Gateway to Services**: gRPC over mTLS, rate-limited and JWT validated
- **Services to Databases**: PostgreSQL protocol and Elasticsearch REST API with AES-256 encryption over TLS
- **Notification Dispatcher to External Service**: Asynchronous messaging via TLS-secured AMQP/MQTT

## Technology Stack
- **Frontend**: React and TypeScript for responsive self-service and administrative UIs
- **Search & Storage**: Elasticsearch (EU-hosted) for <800ms search latency; PostgreSQL with read replicas for transactional integrity
- **Orchestration**: Kubernetes with Horizontal Pod Autoscalers (HPA) for scalable, automated deployments
- **Security**: HashiCorp Vault for key management; service mesh (Istio/Linkerd) for mTLS and zero-trust microsegmentation
- **Observability**: OpenTelemetry SDKs streaming metrics and traces to the External Observability Platform

## Rationale
This architecture isolates high-traffic search and patron-facing components from administrative modules, guaranteeing sub-800ms search performance and protecting sensitive workflows. Strict enforcement of EU-hosted infrastructure, mTLS, and AES-256 encryption ensures full compliance with data residency mandates.