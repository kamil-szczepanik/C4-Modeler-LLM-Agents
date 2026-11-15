## Overview
[The Identity & Access Management (IAM) and Consent Service manages user authentication, authorization, and granular consent-driven access for the Cross-Border Telehealth Platform. It enforces regional data residency and regulatory compliance across EU and US deployments.]

## Key Elements
• Authentication Component (Spring Security / OIDC)
• Consent Engine (Spring Boot / Domain Model)
• Consent Ledger (Cloud SQL PostgreSQL per region)
• Policy Enforcement Interceptor (gRPC / Envoy Filter)
• Revocation Cache Component (Google Cloud Memorystore Redis)
• External Identity Providers (eIDAS, OAuth2/OIDC IdPs)
• Google Secret Manager

## Relationships
• API Gateway -> Policy Enforcement Interceptor: Validates requests [gRPC with mTLS via Istio/Anthos]
• Authentication Component -> External Identity Providers: Federates authentication [OAuth2 / OIDC / eIDAS]
• Policy Enforcement Interceptor -> Revocation Cache Component: Checks consent state [gRPC with mTLS]
• Consent Engine -> Consent Ledger: Persists immutable logs [PostgreSQL with CMEK]

## Technology Stack
• Spring Boot / Java: Core framework for IAM and Consent Engine services due to enterprise maturity
• Google Cloud SQL PostgreSQL: Regional database instances chosen to enforce strict data residency (R-05)
• Google Cloud Memorystore (Redis): Regional caching for low-latency revocation checks without cross-region leaks
• Google Secret Manager: Manages secure credentials and OIDC client secrets with automated rotation

## Rationale
[This architecture enforces strict regional data residency and regulatory compliance (GDPR/HIPAA) through isolated GCP deployments in Europe and the US. The combination of short-lived JWTs, regional Redis caching, and a gRPC policy interceptor ensures low-latency validation while protecting patient data.]