## Overview
The Library Management System provides a scalable solution for public and academic libraries to catalogue items, manage circulation, and offer self-service portals. It ensures strict EU data residency compliance and meets sub-800ms search performance requirements.

## Key Elements
* **Users:** Library Patrons, Librarians/Catalogers, Library Administrators
* **Gateways:** API Gateway (Kong/Envoy), EU Payment Gateway, National Library Database
* **Frontends:** Patron Portal (Next.js), Librarian Dashboard (React)
* **Core Services:** Search & Catalogue Service (Elasticsearch/OpenSearch), Circulation Service, Notification Service, Integration Service
* **Data & Messaging:** PostgreSQL with Read Replicas, Message Broker (Kafka/RabbitMQ)
* **Security & Infrastructure:** Identity Provider (OAuth 2.0 / OIDC), HashiCorp Vault, Service Mesh

## Relationships
* **Patron Portal & Librarian Dashboard** -> **API Gateway** via HTTPS (REST/GraphQL) with OAuth 2.0 / OIDC tokens
* **API Gateway** -> **Search & Catalogue Service** via gRPC with mTLS
* **Circulation Service, Notification Service, & Integration Service** <-> **Message Broker** via AMQP
* **Integration Service** -> **EU Payment Gateway & National Library Database** via REST with circuit breakers
* **Services** -> **PostgreSQL & Elasticsearch** via TLS 1.3 and mTLS within EU availability zones

## Technology Stack
* **Frontend:** Next.js (Patron Portal) and React (Librarian Dashboard) for role-optimized UI bundles
* **Backend & API:** Node.js/Go (Circulation), Python/Go (Integration), Kong/Envoy (API Gateway)
* **Search & Database:** Elasticsearch/OpenSearch (Search & Catalogue), PostgreSQL with Read Replicas (Transactional storage)
* **Messaging & Security:** Kafka/RabbitMQ (Message Broker), HashiCorp Vault (Secrets), OAuth 2.0 / OIDC (AuthN/AuthZ)
* **Infrastructure:** Terraform, OpenTelemetry, TLS 1.3, and AES-256 for EU-only compliance

## Rationale
This microservices-based C4 architecture isolates resource-heavy components like the Search & Catalogue Service to consistently achieve the <800ms performance SLA. Furthermore, it strictly enforces EU data residency through region-locked infrastructure and secures sensitive patron data using container isolation, mTLS, and GDPR-compliant PII masking.