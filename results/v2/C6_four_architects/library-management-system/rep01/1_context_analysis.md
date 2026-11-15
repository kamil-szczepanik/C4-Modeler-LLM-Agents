## Overview
The Library Management System is an enterprise solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It guarantees strict EU-only data residency and high-performance search capabilities.

## Key Elements
*   **Users:** Patron (Public/Academic) and Librarian/Staff
*   **System Boundary:** Library Management System (LMS)
*   **Containers:** React/TypeScript Single-Page Application (SPA), Kong/Nginx API Gateway, Java/Spring Boot or Node.js Core Services, PostgreSQL Primary Database, and OpenSearch Caching/Search Layer
*   **External Systems:** EU-Tenant Identity Provider (IdP), EU-Hosted Payment Gateway, Notification Service (Email/SMS), and Digital Content Repository / DRM Provider

## Relationships
*   *Patron/Librarian* -> *SPA*: HTTPS (TLS 1.3)
*   *SPA* -> *API Gateway*: HTTPS (TLS 1.3) via JSON/REST and WebSockets
*   *API Gateway* -> *Core Services*: Internal gRPC
*   *Core Services* -> *PostgreSQL / OpenSearch*: TLS-encrypted JDBC/TCP within private VPC
*   *LMS* -> *IdP, Payment Gateway, Notification Service, Digital Content Repository*: REST/HTTPS (TLS 1.3) restricted to EU endpoints

## Technology Stack
*   **Frontend:** React/TypeScript served via EU CDN for user portals
*   **Gateway:** Kong or Nginx for reverse proxy and TLS termination
*   **Backend:** Java/Spring Boot or Node.js for core business logic
*   **Database:** PostgreSQL on EU-region managed cloud infrastructure for ACID-compliant circulation records
*   **Search Engine:** OpenSearch to meet the R-05 99th-percentile search response < 800 ms requirement
*   **Transport Security:** TLS 1.3 enforced for all internal and external network traffic

## Rationale
This architecture uses localized container orchestration within EU-region cloud infrastructure to strictly enforce the EU-only data residency constraint. Furthermore, the integration of OpenSearch and gRPC guarantees high-performance search and low-latency inter-service communication to meet non-functional requirements.