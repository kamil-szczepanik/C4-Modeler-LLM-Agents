## Overview
[A Library Management System providing cataloging, circulation management, and self-service portals for public and academic libraries.]
[Ensures high-performance search and EU-only data residency compliance.]

## Key Elements
• Library Patrons, Librarians / Circulation Staff, Library Administrators
• External Systems: Identity Provider (IdP), Payment Gateway, EU Cloud/CDN Provider
• Web Application (SPA)
• API Gateway (Nginx / Kong)
• Catalogue & Search Service (Spring Boot / Node.js with OpenSearch)
• Circulation Service (Spring Boot)
• Notification Service (Python/Celery with Sendinblue/Brevo EU)
• Analytics & Reporting Service
• Event Broker (Apache Kafka / AWS EventBridge EU)
• OpenTelemetry Collector & Audit Logging Service
• Managed Databases (PostgreSQL Multi-AZ, Read Replica / ClickHouse)

## Relationships
• Web Application (SPA) to API Gateway via HTTPS (TLS 1.3)
• API Gateway to Catalogue & Search, Circulation, and Analytics Services via gRPC and internal REST
• Circulation & Catalogue Services to Managed PostgreSQL and OpenSearch via private VPC
• Services to Event Broker for asynchronous workflows
• Notification Service to EU-compliant email/SMS relay

## Technology Stack
• React/TypeScript: Frontend single-page application
• Spring Boot / Node.js: Backend container services
• PostgreSQL & OpenSearch: Relational data and search, deployed via EU managed cloud services
• Apache Kafka / AWS EventBridge: Asynchronous messaging
• Nginx / Kong: API Gateway for routing, rate limiting, and JWT validation

## Rationale
• Utilizes managed EU-cloud infrastructure and strict VPC isolation to guarantee EU-only data residency and operational reliability.
• Employs read replicas, dedicated search clusters, and gRPC protocols to reliably achieve sub-800ms search performance (R-05).