## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide secure self-service patron portals.

## Key Elements
* Library Patrons, Library Staff/Cataloguers, and Library Administrators
* External Identity Provider (IdP), External Payment Gateway, and External Notification Service
* API Gateway / Ingress (Traefik or Envoy)
* Patron BFF Container (Node.js/Express or NestJS)
* Staff Workflow Container (Spring Boot or Python/Django)
* Catalogue & Search Service Container (Java / Elasticsearch)
* Circulation & Loan Service Container (Spring Boot)
* Notification Dispatcher Container (Go / Temporal)
* Data Tier: PostgreSQL and Redis
* Infrastructure: Kubernetes clusters with OPA Gatekeeper and OpenTelemetry

## Relationships
* Patrons access the Patron BFF via REST/JSON through the API Gateway with JWT validation.
* Internal containers communicate via gRPC over mTLS.
* Patron BFF and Staff Workflow query the Catalogue & Search Service using gRPC.
* Circulation Service queries PostgreSQL via JDBC.
* Notification Dispatcher integrates with the External Notification Service.

## Technology Stack
* API Gateway: Traefik or Envoy for routing and TLS termination.
* Backend Frameworks: Node.js/NestJS for Patron BFF; Spring Boot for Staff Workflow and Circulation.
* Search Engine: Java / Elasticsearch for sub-800ms search queries (R-05).
* Database & Caching: PostgreSQL for relational data; Redis for search caching.
* Orchestration & Security: Kubernetes with OPA Gatekeeper for EU data residency, HashiCorp Vault for secrets, and Cosign for image signing.

## Rationale
Isolating patron-facing services from staff workflows protects the 99th-percentile search response SLA (< 800 ms) under heavy load. Strict EU-only data residency and zero-trust mTLS controls ensure full regulatory compliance and robust data protection.