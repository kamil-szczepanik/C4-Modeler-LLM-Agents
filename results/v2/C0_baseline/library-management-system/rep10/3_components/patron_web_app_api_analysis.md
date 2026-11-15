## Overview
The Patron Web App & API container provides secure, self-service cataloging, circulation, and account management for library patrons. It ensures frictionless user experiences while meeting strict EU data residency and high-performance constraints.

## Key Elements
- Patron UI Component (Next.js SSR/React)
- Patron API Controller (Node.js/Express)
- Patron Profile & Preferences Component (TypeScript/React Hook Form)
- Payment Client (TypeScript SDK/HTTPS)
- Notification Event Publisher (Node.js Kafka Client)
- Database Client (Prisma/TypeORM)
- API Gateway (Kong/Envoy)
- Search Engine (Managed OpenSearch/Elasticsearch, EU-hosted)
- Database (Managed PostgreSQL, EU-hosted, AES-256 encrypted)
- Integration/Messaging Container (Managed Apache Kafka / Amazon MQ, EU-hosted)
- External Payment Gateway
- External Identity Provider (IdP)

## Relationships
- API Gateway -> Patron Web App & API: Routes traffic via gRPC over mTLS
- Patron UI Component & Profile Component -> Patron API Controller: Internal HTTP/RPC
- Patron API Controller -> Payment Client -> External Payment Gateway: Processes payments via HTTPS/REST
- Patron API Controller -> Notification Event Publisher -> Integration/Messaging Container: Streams events via Kafka Protocol over TLS
- Patron API Controller -> Database Client -> Database: Reads/writes data via PostgreSQL Protocol over TLS 1.3
- Patron Web App & API -> Search Engine: Queries catalog via HTTPS/REST
- Patron Web App & API -> External Identity Provider (IdP): Authenticates via OIDC / OAuth 2.0

## Technology Stack
- Next.js / React: Powers SSR and frontend UI components for optimal performance
- Node.js / Express: Handles backend API logic and request validation
- Prisma / TypeORM: Manages secure database queries ensuring data residency compliance
- Managed PostgreSQL & Kafka: Provides encrypted, EU-resident persistence and messaging
- TypeScript: Ensures type safety across internal client modules and API controllers

## Rationale
This architecture decouples asynchronous tasks like notifications from real-time patron actions to guarantee the <800ms search performance requirement. Isolating payment and database clients ensures compliance with EU-only data residency and reduces the PCI-DSS security scope.