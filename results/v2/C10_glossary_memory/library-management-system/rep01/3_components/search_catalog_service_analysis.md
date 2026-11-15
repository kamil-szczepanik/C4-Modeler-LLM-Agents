## Overview
[A cloud-native Library Management System providing cataloging, circulation, and self-service portals with strict EU-only data residency.]

## Key Elements
- Library Member (Patron), Librarian / Staff, Library Administrator
- Anycast CDN / DDoS Protection Service (EU-PoPs), EU Cloud Infrastructure (AWS/Azure EU Region), EU Identity Provider (IdP)
- API Gateway / BFF (Nginx/Envoy), Patron Portal, Staff Circulation App, Admin Console
- Search & Catalog Service (Java/Spring Boot + Elasticsearch), Circulation & Core Engine (Go/Node.js)
- Primary Database (PostgreSQL, EU-hosted), Notification Worker, Digital Content Sync Worker

## Relationships
- Library Member (Patron) -> Anycast CDN / DDoS Protection Service (EU-PoPs) [TLS 1.3, HTTPS]
- Anycast CDN / DDoS Protection Service (EU-PoPs) -> API Gateway / BFF [TLS 1.3, HTTPS]
- Patron Portal -> API Gateway / BFF [HTTPS/REST, WSS]
- API Gateway / BFF -> Search & Catalog Service [gRPC]
- API Gateway / BFF -> Circulation & Core Engine [gRPC / HTTPS]
- Circulation & Core Engine -> Primary Database [Postgres Wire Protocol over mTLS]

## Technology Stack
- Java/Spring Boot + Elasticsearch: Powers the Search & Catalog Service for sub-800ms search performance
- Go/Node.js: Implements the core business logic engine for circulation workflows
- PostgreSQL (EU-hosted): Persists application data with AES-256 encryption at rest
- Nginx/Envoy: Manages edge routing, TLS termination, and rate limiting at the API Gateway

## Rationale
[Decomposing services with asynchronous workers and Elasticsearch ensures sub-800ms search performance under heavy academic loads. Strict adherence to EU-hosted infrastructure and TLS/mTLS protocols guarantees complete regional data residency compliance.]