## Overview
The Library Management System provides a cloud-native platform for cataloging physical and digital items, managing circulation, and offering self-service portals. It enforces strict EU-only data residency and high-performance requirements.

## Key Elements
- Library Management System [softwareSystem, context]
- Library Member (Patron), Librarian / Staff, Library Administrator [person, context]
- Anycast CDN / DDoS Protection Service (EU-PoPs), EU Cloud Infrastructure (AWS/Azure EU Region), EU Identity Provider (IdP), EU Compliance & Audit Logging Service, EU Monitoring & APM Provider, Third-Party Digital Content Providers (OverDrive/Libby), External Notification Service, EU Secondary Region Backup Target [externalSystem, context]
- API Gateway / BFF (Nginx/Envoy), Patron Portal, Staff Circulation App, Admin Console, Search & Catalog Service (Java/Spring Boot + Elasticsearch), Circulation & Core Engine (Go/Node.js), Primary Database (PostgreSQL, EU-hosted), Notification Worker, Digital Content Sync Worker [container]
- Connection Pooler Component (PgBouncer), Relational Storage Engine Component (PostgreSQL Core), Encryption & Key Management Component, Replication & Failover Component [component]

## Relationships
- Library Member (Patron) -> Anycast CDN / DDoS Protection Service (EU-PoPs) [TLS 1.3, HTTPS]
- Anycast CDN / DDoS Protection Service (EU-PoPs) -> API Gateway / BFF [TLS 1.3, HTTPS]
- Patron Portal, Staff Circulation App, Admin Console -> API Gateway / BFF [HTTPS/REST, WSS]
- API Gateway / BFF -> Search & Catalog Service [gRPC]
- API Gateway / BFF -> Circulation & Core Engine [gRPC / HTTPS]
- Circulation & Core Engine -> Primary Database [Postgres Wire Protocol over mTLS]
- Circulation & Core Engine -> Connection Pooler Component [Postgres Wire Protocol over mTLS]
- Primary Database -> EU Monitoring & APM Provider [OTLP/HTTPS]

## Technology Stack
- PostgreSQL: Provides ACID transactional integrity and EU-hosted relational storage.
- PgBouncer: Manages database connections to prevent thread exhaustion during peak academic loads.
- Elasticsearch / Java Spring Boot: Delivers sub-800ms search performance for catalog items.
- AES-256 and pgcrypto: Secures application data at rest and column-level PII.
- SCRAM-SHA-256 over mTLS: Enforces least-privilege database authentication and transport security.

## Rationale
The architecture utilizes PostgreSQL with connection pooling and automated replication to handle high peak-load circulation transactions reliably. Strict encryption, audit logging, and isolated EU hosting ensure full compliance with EU data residency and GDPR mandates.