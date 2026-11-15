## Overview
The Library Management System provides a digital solution for public and academic libraries to catalogue items and manage circulation. The Self-Service Portal Container specifically delivers patron-facing discovery and autonomous account workflows.

## Key Elements
* Library Patrons (Primary Users)
* Self-Service Portal Container (Kubernetes, Istio)
* API Gateway (OAuth2/OIDC, JWT)
* Catalogue Database and Read-Replica Data Store
* Distributed Cache (Redis)
* Content Delivery Network (CDN)

## Relationships
* API Gateway -> Self-Service Portal Container: Routes requests [mTLS via Istio]
* Self-Service Portal Container -> Distributed Cache (Redis): Offloads frequent catalogue queries [In-cluster]
* Self-Service Portal Container -> Read-Replica Data Store: Queries catalogue data [TLS 1.3]
* Self-Service Portal Container -> CDN: Delivers localized static assets [HTTPS]

## Technology Stack
* Kubernetes & Istio: Container orchestration and service mesh for zero-downtime canary deployments and mTLS.
* Redis: Distributed caching layer to guarantee 99th-percentile search response times under 800 ms.
* OpenTelemetry: End-to-end tracing with PII scrubbing for EU GDPR compliance.
* Kubernetes Horizontal Pod Autoscaler (HPA): Dynamic scaling based on CPU and request latency.

## Rationale
This architecture ensures strict EU-only data residency and meets sub-800ms search performance SLAs through targeted caching and auto-scaling. Robust security controls, including short-lived JWTs and input validation, protect patron privacy.