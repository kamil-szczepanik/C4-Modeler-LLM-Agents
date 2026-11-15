## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The architecture utilizes an API Gateway/BFF pattern to handle client requests, secure traffic, and meet strict EU data residency constraints.

## Key Elements
- Users: Patrons, Staff, Librarians, and System Administrators
- Edge Security: Edge / WAF
- Gateway: API Gateway / BFF Container
- Core Services: Web App Container, Core Transactional Service Container, Search Service Container
- Infrastructure: Distributed Cache Container (Redis), Message Broker Container (Kafka/RabbitMQ)

## Relationships
- Patrons/Staff/Librarians/Administrators -> API Gateway / BFF Container: HTTPS [HTTPS]
- Edge / WAF -> API Gateway / BFF Container: Inspects and filters traffic [HTTPS]
- API Gateway / BFF Container -> Core Transactional Service Container: Routes requests [Internal REST/gRPC]
- API Gateway / BFF Container -> Search Service Container: Routes search queries [Internal REST/gRPC]
- API Gateway / BFF Container -> Distributed Cache Container (Redis): Offloads session state and caching [TCP]

## Technology Stack
- API Gateway / BFF: Custom routing engine with declarative configuration for maintainability
- Authentication: OAuth2/OIDC integrated via gateway
- Caching/Session State: Redis for horizontal scalability and session offloading
- Search: Elasticsearch / OpenSearch for sub-800ms catalogue retrieval
- Contracts: OpenAPI/Swagger for API schema definition and automated testing

## Rationale
This architecture ensures horizontal scalability and sub-800ms search performance through distributed caching and request optimization at the gateway. Strict data residency and security constraints are met via edge filtering, PII log sanitization, and OAuth2 validation.