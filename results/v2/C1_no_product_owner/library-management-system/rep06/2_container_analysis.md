## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It is architected for strict EU data residency and high-performance search capabilities.

## Key Elements
- Library Patron and Librarian / Library Staff
- Payment Gateway and Digital Content Provider
- Web Application (SPA - React/TypeScript)
- API Gateway (NGINX / Spring Cloud Gateway)
- Core Domain Service (Spring Boot/Java)
- Search Service (Elasticsearch / OpenSearch)
- Async Event Bus (Managed Kafka)
- Database (PostgreSQL)

## Relationships
- Web Application -> API Gateway via HTTPS / TLS 1.3
- API Gateway -> Core Domain Service via gRPC/REST with mTLS
- Core Domain Service -> Database via JDBC (AES-256 encrypted)
- Core Domain Service -> Async Event Bus via Kafka protocol
- Search Service -> Async Event Bus via Kafka protocol

## Technology Stack
- React/TypeScript: Powers the single-page web application hosted on an EU CDN.
- Spring Boot & Java: Implements core cataloguing and circulation business logic.
- PostgreSQL & OpenSearch: Managed EU-hosted services providing transactional persistence and sub-800ms search performance (R-05).
- Managed Kafka: Decouples core transactions from search indexing asynchronously.
- TLS 1.3 & mTLS: Secures all external and internal container-to-container communication.

## Rationale
This architecture uses event-driven decoupling and dedicated managed storage services to meet the sub-800ms search performance SLA without degrading core transactions. Furthermore, all infrastructure and data flows are strictly constrained to EU boundaries to comply with data residency mandates.