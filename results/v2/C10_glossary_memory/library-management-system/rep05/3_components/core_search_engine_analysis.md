## Overview
The Library Management System provides a comprehensive solution for public and academic libraries to catalogue physical and digital items, manage circulation, and offer self-service portals. It ensures strict EU-only data residency and maintains a 99th-percentile search response time under 800 milliseconds.

## Key Elements
- Library Patrons & Staff [person]
- EU-edge Reverse Proxy [externalSystem]
- Third-Party Digital Content Providers [externalSystem]
- Payment Gateway [externalSystem]
- Notification Service [externalSystem]
- Self-Service Web App (React/Next.js SPA) [container]
- Admin/Staff Portal (React Admin SPA) [container]
- API Gateway (Nginx/Kong) [container]
- Circulation & Cataloguing Service (Node.js/TypeScript) [container]
- Core Search Engine (Elasticsearch 3-node cluster) [container]
- Database (PostgreSQL) [container]
- Query Processing Component, Indexing Component, Search Indices, Analysis Component, Cluster Coordination Component [components]

## Relationships
- Library Patrons & Staff -> EU-edge Reverse Proxy [HTTPS/TLS 1.3, OIDC/OAuth2]
- Self-Service Web App & Admin/Staff Portal -> API Gateway [HTTPS/REST with JWT]
- API Gateway -> Circulation & Cataloguing Service [gRPC/Internal, mTLS]
- Circulation & Cataloguing Service -> Core Search Engine [HTTP/REST over TCP, mTLS]
- Circulation & Cataloguing Service -> Database [PostgreSQL Wire Protocol]
- Circulation & Cataloguing Service -> Third-Party Digital Content Providers [REST/JSON over HTTPS]
- Circulation & Cataloguing Service -> Payment Gateway [HTTPS/REST]
- Circulation & Cataloguing Service -> Notification Service [Webhooks/SMTP with HMAC]

## Technology Stack
- Elasticsearch: Selected for the Core Search Engine to natively guarantee sub-800ms search latencies (R-05) via inverted index architecture.
- PostgreSQL: Utilized as the managed database with AES-256 encryption at rest to enforce EU-only data residency constraints.
- React/Next.js & React Admin: Deployed on EU-edge static hosting for patron and staff frontend applications.
- Nginx/Kong: Acts as the API Gateway for routing, rate limiting, and OAuth2/OIDC token validation.
- Node.js/TypeScript: Powers the Circulation & Cataloguing Service business logic.
- Transport Layer Security (TLS 1.3 with mTLS): Secures internal service-to-service communication.

## Rationale
This architecture uses a high-performance search engine and a managed database deployed across dedicated EU availability zones to meet strict data residency mandates and performance SLAs. Strict API gateways, mTLS, and RBAC secure internal components against denial-of-service vectors while supporting complex cataloguing and discovery features.