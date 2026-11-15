## Overview
The Library Management System is a comprehensive solution designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It guarantees strict EU-only data residency and maintains a 99th-percentile search response time under 800ms.

## Key Elements
* Web Application (SPA): Frontend single-page application served via CDN
* API Gateway: Entry point with TLS termination and IAM token validation
* Core Business Services: Decoupled microservices architecture
* Search Engine Container: Elasticsearch/OpenSearch
* Database Container: PostgreSQL
* Async Event Broker Container: Apache Kafka or RabbitMQ
* Shared Caching Container: Redis
* File Storage Container: S3/HTTPS Compatible Storage

## Relationships
* Self-Service Patrons -> Web Application (SPA): Interacts for searching and self-service portals [HTTPS/TLS]
* Library Staff -> Web Application (SPA): Interacts for administrative catalogue management and circulation [HTTPS/TLS]
* Web Application (SPA) -> API Gateway: Sends user requests and retrieves data [HTTPS/TLS]

## Technology Stack
* Frontend Framework: React with React Query / RTK Query for client-side state management and search caching
* CDN Provider: Configured with restricted EU-only edge caching and origin routing for data residency compliance
* Security: Content Security Policy (CSP), automated dependency vulnerability scanning, and cache-busting hashing
* Monitoring & Testing: Real-User Monitoring (RUM) for Core Web Vitals, automated E2E smoke tests, and WCAG 2.1 AA accessibility testing

## Rationale
The modular SPA architecture with client-side caching and strict CDN edge constraints ensures compliance with EU data residency while achieving the sub-800ms search performance requirement. Comprehensive CI/CD quality gates, including bundle size budgets and automated testing, guarantee high availability, maintainability, and accessibility for patrons and staff.