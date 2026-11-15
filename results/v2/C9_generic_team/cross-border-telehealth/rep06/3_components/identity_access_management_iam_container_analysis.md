## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Its architecture enforces regional data residency while ensuring secure, compliant identity and access management.]

## Key Elements
- Identity & Access Management (IAM) Container
- API Gateway / Edge Proxy Container (GCP Cloud Load Balancing / Envoy)
- State & Session Management Container (Redis / GCP Memorystore)
- Audit & Traceability Logging Container (GCP Pub/Sub / Cloud Logging)
- Secrets & Certificate Management Container (GCP Secret Manager)
- Data Persistence Container (Cloud SQL / Spanner (GCP))

## Relationships
- API Gateway -> IAM Container: Authenticates and authorizes requests [gRPC over mTLS, JWT]
- IAM Container -> GCP Secret Manager: Retrieves signing keys and environment variables [HTTPS]
- IAM Container -> GCP Pub/Sub: Emits asynchronous security audit events [gRPC]
- IAM Container -> Data Persistence Container: Queries regional consent and user states [PostgreSQL Protocol / SQL]

## Technology Stack
- OAuth2 / OpenID Connect / JWTs: Standardized authentication protocols with short-lived (15-minute) tokens to balance security and scalability
- RFC 8414 / RFC 7807: Standardized OIDC discovery endpoints and problem details for secure error handling
- GCP Cloud Run: Serverless container execution with explicit resource pinning and zero-downtime scaling
- GCP Secret Manager: Secure storage for rotating asymmetric JWT signing keys and configuration parameters

## Rationale
[This architecture strictly enforces GDPR and HIPAA data residency requirements by decoupling dynamic consent from JWT payloads while enabling high availability in degraded network conditions. Asymmetric key rotation and automated auditing guarantee traceability for medical device compliance and secure cross-border operations.]