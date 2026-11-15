## Overview
• The Library Management System provides public and academic libraries with catalogue management, circulation control, and self-service portals.
• The system enforces strict EU-only data residency and high-performance search requirements.

## Key Elements
• Library Patrons
• Circulation Staff and Library Administrators
• Web Portal (React/TypeScript on Nginx)
• API Gateway (Envoy/Kong)
• Core Services API (Java/Spring Boot)
• Search & Catalogue Service (Elasticsearch/OpenSearch)
• Database (PostgreSQL with EU hosting)
• Identity Provider / SSO
• Digital Content Providers
• Notification Gateway

## Relationships
• Library Patrons -> Web Portal (HTTPS/TLS 1.3)
• Circulation Staff and Library Administrators -> Web Portal (HTTPS/TLS 1.3)
• Web Portal -> API Gateway (HTTPS / JSON over TLS 1.3)
• API Gateway -> Core Services API (gRPC over mTLS)
• API Gateway -> Search & Catalogue Service (gRPC over mTLS)
• Core Services API -> Database (PostgreSQL Wire Protocol over TLS 1.3)
• API Gateway -> Identity Provider / SSO (OIDC/SAML over HTTPS)

## Technology Stack
• React/TypeScript on Nginx: Provides UI components and client-side routing within an EU-restricted container deployment.
• Envoy/Kong API Gateway: Manages edge security, OIDC validation, and HttpOnly session cookies.
• Java/Spring Boot Core Services API: Processes business logic and server-side authorization.
• Elasticsearch/OpenSearch: Delivers high-performance catalogue search queries meeting R-05 SLAs.
• PostgreSQL: Stores persistent relational data compliant with EU-only residency mandates.

## Rationale
• The multi-tier architecture separates UI presentation from transactional services to guarantee high-performance search responses under 800 ms.
• Strict adherence to EU-only data residency and secure token management protects sensitive patron data against regulatory breaches.