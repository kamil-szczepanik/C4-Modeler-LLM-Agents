## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. The API Gateway manages secure, high-performance edge routing and security enforcement.

## Key Elements
- **Web Application**: React app served via Nginx
- **API Gateway (Envoy)**: Kubernetes Ingress Controller with TLS Termination, WAF, Token Exchange, Routing Engine, Rate Limiting, and Telemetry filters
- **Core Domain Microservice**: Java 17, Spring Boot service handling business logic
- **Search Microservice**: Elasticsearch handling catalog queries
- **Secure Vault**: HashiCorp Vault providing dynamic secrets and JWT keys

## Relationships
- **Web Application -> API Gateway**: Forwards client requests [HTTPS, TLS 1.3]
- **API Gateway -> Core Domain Microservice**: Routes enriched requests with injected claims [mTLS, REST/JSON]
- **API Gateway -> Search Microservice**: Routes search queries with circuit breaking [mTLS, REST/JSON]
- **API Gateway -> Secure Vault**: Fetches mTLS certificates and JWT validation keys [TLS, API]

## Technology Stack
- **Envoy**: High-performance C++ proxy chosen for low latency and rich filter ecosystem
- **HashiCorp Vault**: Secures dynamic secrets and automated mTLS certificate rotation
- **Kubernetes**: Orchestration platform with multi-zone replica sets pinned to EU-region nodes
- **OpenTelemetry**: Standardized telemetry collection and propagation

## Rationale
Envoy and Kubernetes ensure sub-800ms search performance while enforcing strict EU data residency. Vault-backed mTLS and edge token exchange establish a zero-trust architecture.