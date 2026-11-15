## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals for public and academic libraries. The architecture enforces strict EU-only data residency and meets high-performance search latency requirements.

## Key Elements
- **API Gateway Container**: Kong Gateway handling edge routing, security, and telemetry.
- **Web Application Container**: React/TypeScript frontend served via Nginx.
- **Core Services Container**: Java/Spring Boot application managing business logic.
- **Search Service Container**: Elasticsearch/OpenSearch for catalog discovery.
- **Database & Cache Containers**: PostgreSQL (EU region) and Redis.
- **Internal API Gateway Components**: Routing & Proxy Engine, Auth Plugin, Rate Limiting Plugin, Request Transformation Plugin, Telemetry & Tracing Component, IP Geolocation & Geo-Fencing Plugin.

## Relationships
- **Web Application Container -> API Gateway Container**: Routes frontend traffic [HTTPS/REST and WebSockets].
- **API Gateway Container -> Core Services Container**: Forwards validated requests [gRPC].
- **API Gateway Container -> Search Service Container**: Routes catalogue search queries directly [gRPC/HTTP].
- **API Gateway Container -> Redis Cache Container**: Performs rate-limiting and JWT checks [Redis RESP protocol].
- **API Gateway Container -> EU Identity Provider**: Validates OAuth2/OIDC tokens [HTTPS/OIDC].

## Technology Stack
- **Kong Gateway**: Selected for rich ecosystem of plugins (JWT, Rate Limiting, Geo-IP, OpenTelemetry).
- **OpenTelemetry (OTel)**: Used for distributed tracing to monitor P99 search latency (< 800 ms SLA).
- **Redis**: Provides fast distributed rate-limiting and JWT revocation checks within the EU cluster.
- **Elasticsearch/OpenSearch**: Delivers high-performance catalogue search bypassing core services.

## Rationale
This architecture uses an API Gateway pattern with direct search routing and edge-level security plugins to meet strict P99 latency SLAs (< 800 ms). Deploying all components within EU-hosted infrastructure strictly enforces regional data residency constraints.