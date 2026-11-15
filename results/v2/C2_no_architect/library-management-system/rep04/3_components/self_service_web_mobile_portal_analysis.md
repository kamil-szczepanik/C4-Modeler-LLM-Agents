## Overview
The Library Management System provides a solution for public and academic libraries to catalogue items and manage circulation. The Self-Service Web/Mobile Portal serves patrons and librarians with secure access, robust accessibility, and strict EU data residency.

## Key Elements
* Library Patrons (Members)
* Librarians / Library Staff
* Self-Service Web/Mobile Portal (Web/Mobile)
* API Gateway (Kubernetes, OAuth2/OIDC, mTLS)
* Read-optimized Search Index (Elasticsearch, EU-hosted)
* External Services (Payment Gateways, Notification Services, ILL Partners)

## Relationships
* Library Patrons -> Self-Service Web/Mobile Portal [HTTPS (TLS 1.3)]
* Librarians -> Self-Service Web/Mobile Portal [HTTPS (TLS 1.3)]
* Self-Service Web/Mobile Portal -> API Gateway [HTTPS (TLS 1.3), OAuth2/OIDC, PKCE]
* API Gateway -> Read-optimized Search Index [gRPC/REST, mTLS]

## Technology Stack
* Frontend Assets: EU-hosted CDN with strict geo-pinning for EU data residency
* Authentication: OAuth2/OIDC with PKCE, HTTP-only Secure SameSite=Strict cookies
* Security: Subresource Integrity (SRI), Content Security Policy (CSP), platform-native secure enclaves (Keychain/Keystore)
* Observability: Real User Monitoring (RUM) for latency tracking (<800ms NFR)

## Rationale
The architecture ensures strict GDPR compliance and EU data residency via localized CDN deployment and zero-PII client caching. It guarantees high performance (<800ms search latency) through optimized search indexes and comprehensive RUM tracking.