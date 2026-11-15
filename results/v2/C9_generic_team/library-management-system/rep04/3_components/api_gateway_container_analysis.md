## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries while enforcing EU-only data residency. It utilizes an API Gateway container to securely route, validate, and optimize client traffic to core microservices.

## Key Elements
- Web Frontend (React, HTML, JavaScript)
- Mobile App (Native / Cross-Platform)
- API Gateway Container (OCI-compliant, Envoy / NGINX)
- Core Microservices: Catalog Management, Circulation, User Portals (Spring Boot)
- Infrastructure: Redis Distributed Cache, RabbitMQ / Kafka, Elasticsearch / OpenSearch

## Relationships
- Web Frontend -> API Gateway Container [HTTPS/REST]
- Mobile App -> API Gateway Container [HTTPS/REST]
- API Gateway Container -> Catalog Management [gRPC/REST]
- API Gateway Container -> Circulation [gRPC/REST]
- API Gateway Container -> User Portals [gRPC/REST]
- API Gateway Container -> Redis Distributed Cache [RESP/TCP]

## Technology Stack
- API Gateway: Envoy or NGINX (OCI-compliant) for high-performance proxying and traffic management
- Caching/Rate Limiting: Redis Distributed Cache for token bucket algorithms and distributed state
- Observability: W3C Trace Context and OTel Collector for distributed tracing and telemetry
- Validation/Errors: OpenAPI / JSON Schema and RFC 7807 Problem Details for standardized payloads
- Security: TLS termination, IP whitelisting, and strict request size/payload limits

## Rationale
This architecture ensures strict EU data residency while maintaining high availability and low latency (<800 ms search response). Edge-level security, rate limiting, and circuit breaking protect backend services from cascading failures and traffic spikes.