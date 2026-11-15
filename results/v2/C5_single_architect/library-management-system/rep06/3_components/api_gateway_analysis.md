## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures EU-only data residency and meets high-performance search requirements.

## Key Elements
- **Patron & Librarian / Staff**: System users
- **Web Application (SPA)**: Built with React, TypeScript, and Nginx
- **API Gateway**: Built with Spring Cloud Gateway (Java), containing Routing Engine, Auth & Token Relay Filter, Rate Limiter/Throttler, and Request Transformation & Logging Filter
- **Core Domain Service**: Built with Java and Spring Boot
- **Search Service**: Built with Python, FastAPI, and Elasticsearch
- **Async Event Broker & Database**: Apache Kafka, PostgreSQL, and Redis
- **External Systems**: Payment Gateway, Notification Provider, Identity Provider, Digital Content Provider

## Relationships
- Web Application (SPA) -> API Gateway: Terminates TLS, forwards authenticated requests [HTTPS/REST]
- API Gateway -> Core Domain Service / Search Service: Forwards sanitized requests [gRPC]
- Auth & Token Relay Filter -> Identity Provider: Introspects/Validates JWTs [HTTPS/OIDC]
- Rate Limiter / Throttler -> Redis Database: Checks request quotas [RESP/TCP]

## Technology Stack
- **Spring Cloud Gateway (Java)**: Standardized to reduce operational overhead and maintain ecosystem alignment
- **Redis**: Backs the rate limiter/throttler for quota checks
- **Elasticsearch**: Powers search performance to meet the < 800 ms requirement
- **PostgreSQL**: Primary data store constrained to EU infrastructure

## Rationale
Standardizing on Spring Cloud Gateway and a unified Java stack minimizes operational complexity while delivering high-performance, secure routing. This architecture directly supports strict EU data residency constraints and sub-800ms search performance goals.