## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It guarantees EU-only data residency and sub-800ms search responses.

## Key Elements
*   **Users:** Library Patrons, Library Staff
*   **Frontends:** Patron Portal (React/TypeScript SPA), Staff Dashboard (React/TypeScript SPA)
*   **Gateway & Services:** API Gateway (Nginx/Envoy), Core Business Service (Java/Spring Boot), Search Service (Elasticsearch/OpenSearch), Integration Service (Node.js/TypeScript), Notification & Audit Service (Python/FastAPI)
*   **Storage & Messaging:** Relational DB (PostgreSQL), Message Broker (Kafka/RabbitMQ), Secrets Manager (HashiCorp Vault)
*   **External Systems:** Third-Party Identity Provider, Digital Content Providers, Interlibrary Loan Network, Payment Gateway, Notification Service, Centralized Observability & SIEM Platform, Backup & Disaster Recovery Storage

## Relationships
*   **Frontend to Gateway:** Patron Portal and Staff Dashboard connect to API Gateway via HTTPS (TLS 1.3).
*   **Gateway to Core:** API Gateway routes traffic to Core Business Service using gRPC/REST over mTLS (Istio service mesh).
*   **Search & Events:** Core Business Service syncs data to Search Service asynchronously via AMQP/Kafka.
*   **Integration & Notifications:** Integration Service and Notification & Audit Service consume domain events via Kafka/RabbitMQ.
*   **External Outbound:** Integration Service connects to Payment Gateways and Digital Content Providers via TLS 1.3.

## Technology Stack
*   **Frontend:** React and TypeScript for responsive SPAs.
*   **Platform & Mesh:** Kubernetes (EKS/AKS) with Istio service mesh for mTLS and circuit breaking.
*   **Backend & APIs:** Java/Spring Boot (Core), Node.js/TypeScript (Integration), Python/FastAPI (Notification & Audit).
*   **Data & Search:** PostgreSQL and OpenSearch hosted exclusively in EU regions.
*   **Security:** OAuth2/OIDC with JWTs via Third-Party Identity Provider; HashiCorp Vault for secrets management.

## Rationale
This architecture uses dedicated search and integration containers backed by asynchronous messaging to easily achieve the sub-800ms search NFR without database bottlenecks. Furthermore, managed EU-cloud infrastructure, strict mTLS, and isolated integration services satisfy rigorous data residency and zero-trust security constraints.