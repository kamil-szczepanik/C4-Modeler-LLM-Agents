## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within an EU-only data residency constraint. It utilizes a containerized microservices architecture to ensure high performance, meeting 99th-percentile search response times under 800 ms.

## Key Elements
- Web App Container (Web Application Framework)
- API Gateway / BFF Container (API Gateway / BFF)
- Search Service Container (Elasticsearch / OpenSearch)
- Distributed Cache Container (Redis)
- Enterprise Logging and Monitoring Service

## Relationships
- API Gateway / BFF Container -> Web App Container: Routes requests [Internal REST/gRPC]
- Web App Container -> Search Service Container: Serves search queries [HTTP]
- Web App Container -> Distributed Cache Container: Manages sessions and caches catalogue queries [Redis Protocol]
- Web App Container -> Enterprise Logging and Monitoring Service: Sends structured JSON logs and metrics [HTTPS]

## Technology Stack
- Server-Side Rendering (SSR) with Hydration: Balances SEO for catalogues with UI interactivity
- Redis: Externalizes session state for stateless container scalability
- Structured JSON Logging: Streamlines ingestion into enterprise monitoring

## Rationale
The architecture ensures strict EU data compliance while maintaining horizontal scalability and low latency. Stateless containers combined with distributed caching and optimized rendering directly support the required high-performance search targets.