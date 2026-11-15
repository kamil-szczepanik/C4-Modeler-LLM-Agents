## Overview
The Library Management System is a comprehensive solution for public and academic libraries designed to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and maintains a 99th-percentile search response time under 800 ms.

## Key Elements
* Library Patrons, Librarians / Circulation Staff, Library Administrators
* API Gateway (OAuth2/OIDC, JWT, Redis)
* Self-Service Portal Container (Kubernetes, Istio)
* Circulation Management Container (Kubernetes, Istio)
* Analytics/Reporting Container (Kubernetes, OpenTelemetry, Prometheus/Grafana)
* Catalogue Database, Message Broker (Kafka / RabbitMQ)

## Relationships
* Library Patrons -> API Gateway: Accesses self-service portals [HTTPS via OAuth2/OIDC with short-lived JWTs]
* Librarians -> API Gateway: Interacts with circulation management [HTTPS via OAuth2/OIDC with short-lived JWTs]
* Library Administrators -> API Gateway: Interacts with system administration and analytics [HTTPS via OAuth2/OIDC with short-lived JWTs]
* API Gateway -> Self-Service Portal Container: Routes requests [mTLS via Istio]
* API Gateway -> Circulation Management Container: Routes requests [mTLS via Istio]

## Technology Stack
* API Gateway: Entry point utilizing OAuth2/OIDC, JWT validation, Redis caching, and WAF for perimeter security.
* Kubernetes & Istio: Orchestration and service mesh providing mTLS, circuit breaking, and traffic shifting.
* OpenTelemetry & Prometheus/Grafana: Observability stack for real-time latency monitoring and HPA scaling.
* Anycast DNS: Geo-routing technology to enforce EU data residency and minimize TLS handshake latency.

## Rationale
This architecture ensures secure, isolated access for diverse user personas while meeting stringent performance requirements through edge routing and service mesh optimization. Furthermore, it guarantees compliance with EU-only data residency constraints and high availability via stateless scalability.