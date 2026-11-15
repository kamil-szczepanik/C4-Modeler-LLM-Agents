## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries in the EU. It utilizes a high-performance API Gateway architecture to meet strict latency and data residency requirements.

## Key Elements
- **API Gateway (Kong, Node.js):** Reverse proxy handling edge routing, security, and traffic policies.
- **Routing Engine (Kong Core):** Path-based gRPC routing to downstream services.
- **Authentication & Authorization Filter (Lua/Kong Plugin):** Stateless cryptographic JWT validation via cached JWKS.
- **Rate Limiting & Throttling Module (Redis-backed Kong Plugin):** Multi-AZ Redis instance enforcing traffic thresholds in AWS Frankfurt.
- **Observability & Tracing Agent (Kong OTel Plugin):** Injects W3C Trace Context headers.
- **External Security & Infrastructure:** AWS CloudFront Frankfurt, AWS WAF, AWS Secrets Manager, AWS MSK, and PostgreSQL.

## Relationships
- Web Application -> API Gateway: Sends API requests [HTTPS / REST]
- API Gateway -> Catalogue & Search Service: Routes search queries [gRPC with mTLS]
- API Gateway -> Circulation & User Service: Routes user requests [gRPC with mTLS]
- API Gateway -> Apache Kafka (AWS MSK): Publishes audit logs and access metrics [TCP / SASL_SSL]
- API Gateway -> AWS CloudWatch / OpenTelemetry Collector: Exports traces and metrics [OTLP / gRPC]

## Technology Stack
- **Kong & Node.js:** Chosen for high-performance edge routing and custom plugin extensibility.
- **Redis:** Deployed multi-AZ in AWS Frankfurt to back rate limiting without cross-region latency.
- **OpenTelemetry & W3C Trace Context:** Ensures end-to-end distributed tracing across gRPC boundaries.
- **decK & ArgoCD:** Implements GitOps workflow for version-controlled Kong declarative configurations.
- **AWS WAF & Secrets Manager:** Enforces geo-blocking, DDoS protection, and secure credential injection.

## Rationale
This architecture uses stateless JWT validation and localized multi-AZ caching in AWS Frankfurt to guarantee the <800ms search response NFR. Strict TLS 1.3, mTLS, and EU-only service placement fully satisfy the data residency constraint.