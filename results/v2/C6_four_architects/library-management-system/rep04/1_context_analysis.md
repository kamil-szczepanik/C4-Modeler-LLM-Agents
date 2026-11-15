## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It strictly adheres to EU-only data residency and maintains a 99th-percentile search response under 800 ms.

## Key Elements
- **Patron & Staff (People):** End-users accessing web and mobile interfaces.
- **Library Management System (Software System):** Core system encompassing cataloging, circulation, and self-service portals.
- **Identity Provider (External System):** Keycloak or Auth0 hosted in the EU for OAuth2/OIDC authentication.
- **External Payment Gateway (External System):** Stripe or Adyen restricted to EU regions for fine collection.
- **National Library Registry (External System):** Used for ISBN and bibliographic metadata lookup.
- **Notification Service (External System):** Sendinblue/Brevo EU-hosted provider for circulation alerts.
- **Digital Content Delivery Provider (External System):** OverDrive or Adobe APIs for digital asset fulfillment.
- **Web Frontend (Container):** React/TypeScript Single Page Application served via CDN.
- **API Gateway (Container):** Kong or Nginx reverse proxy.
- **Core Services (Container):** Java/Spring Boot application handling circulation and business logic.
- **Search Engine (Container):** OpenSearch cluster for high-performance catalog queries.
- **Database & Cache (Containers):** PostgreSQL 15+ on AWS RDS Frankfurt and Redis/Valkey for in-memory caching.
- **Async Event Bus (Container):** Apache Kafka or RabbitMQ for decoupled messaging.

## Relationships
- *Patron & Staff* -> *Identity Provider*: HTTPS (OAuth2/OIDC redirect)
- *Patron & Staff* -> *Web Frontend*: HTTPS/TLS
- *Web Frontend* -> *API Gateway*: HTTPS
- *API Gateway* -> *Core Services* & *Search Engine*: gRPC over internal TLS
- *Core Services* -> *Database*, *Cache*, & *Async Event Bus*: Internal TLS / TCP
- *Library Management System* -> *External Payment Gateway*, *National Library Registry*, *Notification Service*, & *Digital Content Delivery Provider*: REST/SOAP over HTTPS (EU-hosted endpoints)

## Technology Stack
- **Frontend:** React/TypeScript, CDN (ensures fast client delivery)
- **API & Routing:** Kong/Nginx, gRPC (minimizes internal latency for <800ms search SLA)
- **Backend Services:** Java/Spring Boot (robust enterprise circulation logic)
- **Search & Caching:** OpenSearch and Redis/Valkey (meets strict <800 ms search performance requirement)
- **Primary Database:** PostgreSQL 15+ on AWS RDS Frankfurt (guarantees EU-only data residency)
- **Messaging:** Apache Kafka or RabbitMQ (decouples background tasks from user transactions)
- **Authentication & Security:** Keycloak/Auth0 via OAuth2/OIDC (offloads security overhead)

## Rationale
This architecture offloads identity and third-party integrations while utilizing high-performance search and caching containers to easily satisfy the <800 ms search latency requirement. Furthermore, selecting EU-native cloud regions and localized external endpoints ensures strict compliance with EU data residency constraints.