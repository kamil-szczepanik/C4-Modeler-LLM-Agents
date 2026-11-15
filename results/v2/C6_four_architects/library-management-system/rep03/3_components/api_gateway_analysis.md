## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It uses an API Gateway container to securely route, authenticate, and translate client requests for downstream microservices.

## Key Elements
- **Clients:** Web Application (React, TypeScript), Self-Service Kiosk App (Electron, C# WPF)
- **API Gateway Components:** SSL Termination Module, Geo-Filtering & Compliance Module, IP Whitelisting & Threat Protection Plugin, Authentication & Authorization Filter, Routing Engine, Protocol Translation Module, Request Transformation Component, Rate Limiting & Throttling Component, Load Balancing & Upstream Circuit Breaker, API Versioning & Deprecation Filter, Metrics & Logging Exporter
- **Downstream Containers:** Core Domain Service (Java, Spring Boot), Search Service (Elasticsearch), Reporting & Analytics Service (Python, FastAPI)
- **External Dependencies:** Identity Provider, Distributed Cache (Redis)

## Relationships
- Web Application & Self-Service Kiosk App -> SSL Termination Module: Makes API requests [HTTPS (REST/JSON)]
- SSL Termination Module -> Geo-Filtering & Compliance Module: Passes decrypted traffic [Internal IPC]
- Geo-Filtering & Compliance Module -> IP Whitelisting & Threat Protection Plugin: Passes filtered traffic [Internal IPC]
- IP Whitelisting & Threat Protection Plugin -> Routing Engine: Passes validated traffic [Internal IPC]
- Routing Engine -> Protocol Translation Module: Forwards matched routes [Internal IPC]
- Protocol Translation Module -> Core Domain Service: Routes translated business payloads [gRPC over TLS]
- Protocol Translation Module -> Search Service: Routes search queries [gRPC over TLS]
- Rate Limiting Component -> Distributed Cache (Redis): Tracks rate-limit counters [RESP over TLS]
- Authentication & Authorization Filter -> Identity Provider: Validates tokens [OAuth2/OIDC]

## Technology Stack
- **Kong on Nginx:** Chosen as the API Gateway container technology for robust rate-limiting and declarative configuration.
- **Lua / Kong Router:** Powers the internal routing engine and custom filtering plugins.
- **gRPC over TLS:** Used for high-performance internal communication between the gateway and downstream microservices.
- **Redis:** Provides fast, distributed state storage for rate-limiting counters.
- **JWT / OAuth2:** Enforces stateless token-based authentication at the edge.

## Rationale
This architecture secures and optimizes ingress traffic at the perimeter while meeting strict EU-only data residency constraints. Protocol translation and circuit breaking ensure sub-800ms search responses and decoupled microservices.