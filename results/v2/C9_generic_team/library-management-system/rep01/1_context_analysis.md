## Overview
The Library Management System provides item cataloguing, circulation management, and self-service portals for public and academic libraries. It ensures strict EU data residency compliance and high-performance search capabilities.

## Key Elements
- Library Patrons and Staff (Users)
- Self-Service Portals and Kiosks
- API Gateway
- Core Domain Services
- Dedicated Search Tier
- Primary Transactional Datastore
- EU-certified Secrets Management Vault

## Relationships
- Users access Self-Service Portals via HTTPS.
- Self-Service Portals communicate with the API Gateway using OpenAPI-defined REST contracts.
- API Gateway routes traffic to Core Domain Services with enforced geo-routing.
- Core Domain Services query the Dedicated Search Tier for catalogue searches (R-01) achieving < 800ms p99 latency (R-05).
- Services persist transactional data in the Primary Transactional Datastore located strictly within the EU.

## Technology Stack
- OpenAPI/AsyncAPI: Contract-first design and API documentation.
- JSON Schema / Protocol Buffers: Defensive data validation at service edges.
- EU-certified Secrets Vault: Secure storage and rotation of credentials, API keys, and certificates.
- Dedicated Search Tier: Meets the < 800ms 99th-percentile search performance requirement (R-05).

## Rationale
This architecture guarantees strict EU data residency compliance through isolated regional boundaries, secure secrets management, and geo-routed ingress. Simultaneously, it meets the strict 99th-percentile search latency requirement (< 800ms) by utilizing a dedicated search tier and decoupled core domain services.