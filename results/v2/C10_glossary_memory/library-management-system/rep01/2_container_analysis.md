## Overview
The Library Management System is a cloud-native platform designed for public and academic libraries to catalogue items, manage circulation, and provide self-service portals with strict EU-only data residency. It delivers sub-800ms search performance and high availability through containerized microservices and decoupled asynchronous workers.

## Key Elements
- Library Member (Patron), Librarian / Staff, Library Administrator
- Anycast CDN / DDoS Protection Service (EU-PoPs)
- API Gateway / BFF (Nginx/Envoy)
- Patron Portal, Staff Circulation App, Admin Console (Web/Mobile Containers)
- Search & Catalog Service (Java/Spring Boot + Elasticsearch)
- Circulation & Core Engine (Go/Node.js)
- Primary Database (PostgreSQL, EU-hosted)
- Notification Worker, Digital Content Sync Worker
- EU Cloud Infrastructure (AWS/Azure EU Region), EU Identity Provider (IdP)
- Third-Party Digital Content Providers (OverDrive/Libby)

## Relationships
- Patron / Staff / Admin -> Anycast CDN / DDoS Protection Service (EU-PoPs) via TLS 1.3, HTTPS
- Patron Portal -> API Gateway / BFF via HTTPS/REST, WSS
- API Gateway / BFF -> Search & Catalog Service via gRPC
- Circulation & Core Engine -> Primary Database via Postgres Wire Protocol over mTLS
- Circulation & Core Engine -> Digital Content Sync Worker & Notification Worker via Async Message Queues (RabbitMQ/Redis)
- Digital Content Sync Worker -> Third-Party Digital Content Providers (OverDrive/Libby) via OAuth2, HTTPS/REST
- Notification Worker -> External Notification Service via SMTP/HTTPS API

## Technology Stack
- API Gateway: Nginx/Envoy for edge routing, TLS termination, and rate limiting
- Search Engine: Java/Spring Boot + Elasticsearch for sub-800ms catalog performance (R-05)
- Core Backend: Go/Node.js for Circulation & Core Engine
- Database: PostgreSQL with AES-256 encryption at rest (EU-hosted)
- Orchestration: Kubernetes (EKS/AKS) running immutable OCI images
- Authentication: OIDC/OAuth2 via EU Identity Provider (IdP) with JWT validation

## Rationale
Isolating user-facing UI containers from heavy backend catalog syncs prevents resource contention and preserves UI responsiveness. Decoupling asynchronous workers protects core circulation and sub-800ms search performance from third-party vendor latency while strictly enforcing EU data residency constraints.