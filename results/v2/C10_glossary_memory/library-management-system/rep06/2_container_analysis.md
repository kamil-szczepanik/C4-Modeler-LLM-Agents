## Overview
The Library Management System provides cataloging, circulation, and self-service portals while enforcing strict EU-only data residency and high-performance search SLAs. It serves patrons, librarians, and administrators through a secure, scalable containerized architecture.

## Key Elements
- Library Patrons, Librarians, Library Administrators
- EU Identity Provider (IdP), Payment Gateway, Digital Content Providers
- Patron Web App (React, TypeScript)
- Staff Web App (Angular, TypeScript)
- Core API Gateway (Envoy/Spring Cloud Gateway)
- Catalog & Search Service (Java, Spring Boot, Elasticsearch)
- Circulation Service (Java, Spring Boot)
- Notification Service (Node.js, TypeScript, RabbitMQ/Kafka)
- Analytics & Reporting Service (Python, FastAPI)
- Primary Database & Read Replica (PostgreSQL)

## Relationships
- Library Patrons / Librarians / Library Administrators -> Patron Web App / Staff Web App (HTTPS, TLS 1.3)
- Patron Web App / Staff Web App -> Core API Gateway (HTTPS, TLS 1.3)
- Core API Gateway -> Catalog & Search Service, Circulation Service, Notification Service, Analytics & Reporting Service (gRPC / HTTPS, mTLS)
- Library Management System -> EU Identity Provider (IdP) (OIDC over HTTPS)
- Circulation Service -> Payment Gateway (REST/JSON, mTLS over HTTPS)
- Library Management System -> Digital Content Providers (API over HTTPS)

## Technology Stack
- React & TypeScript: Powers the responsive Patron Web App for fast client-side rendering.
- Angular & TypeScript: Structures the robust Staff Web App for administrative workflows.
- Java (Spring Boot) & Elasticsearch: Implements high-performance microservices and meets the sub-800ms search SLA (R-05).
- PostgreSQL: Manages transactional data with strict EU-only data residency constraints.
- Kubernetes (EKS/AKS): Orchestrates EU-region container deployments with automated health probes and rolling updates.

## Rationale
The containerized microservices architecture isolates heavy search and analytics workloads to protect transactional performance and maintain the sub-800ms search SLA. Strict EU-hosted databases, message brokers, and OIDC token validation guarantee compliance with data residency and security constraints.