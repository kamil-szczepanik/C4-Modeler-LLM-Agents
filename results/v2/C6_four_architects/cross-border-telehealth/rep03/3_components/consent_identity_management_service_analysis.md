## Overview
The system is a Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. Its core purpose is to deliver secure telemedicine while enforcing strict regional data residency, GDPR/HIPAA compliance, and robust consent management.

## Key Elements
* API Gateway / BFF (Go / Envoy)
* Consent & Identity Management Service (Java / Spring Security)
* Regional Tenant Router Component (Spring Cloud / Java)
* Identity & Federation Component (Spring Security / OAuth2)
* Consent Ledger Component (Spring Data JPA)
* OPA Policy Sidecar Component (Rego / Go)
* Local Credential Cache Component (Spring Cache / Redis)
* Compliance Token Verifier Component (Spring Security JWT)
* Emergency Break-Glass Component (Java / Spring Security)
* Consent Revocation Broadcaster Component (Spring Cloud Stream / Cloud Pub/Sub)
* Audit Interceptor Component (Spring AOP)
* Data Storage (Cloud SQL PostgreSQL, Cloud Storage, GCP Pub/Sub)

## Relationships
* API Gateway / BFF -> Regional Tenant Router Component: Routes identity and consent requests [gRPC over mTLS]
* Identity & Federation Component -> Compliance Token Verifier Component: Delegates token parsing and validation [In-process Java method call]
* Compliance Token Verifier Component -> Regional Tenant Router Component: Passes verified residency metadata [In-process Java method call]
* Regional Tenant Router Component -> Consent Ledger Component: Forwards localized database queries [PostgreSQL Wire Protocol]
* Consent Policy Engine -> OPA Policy Sidecar Component: Delegates access authorization [Local REST/UDS over mTLS]
* Identity & Federation Component -> Local Credential Cache Component: Manages user sessions [Redis protocol over mTLS]
* Consent Ledger Component -> Consent Revocation Broadcaster Component: Emits revocation notices [Spring ApplicationEvent]
* Consent Revocation Broadcaster Component -> Data Storage: Publishes revocation events [Pub/Sub over mTLS]
* Emergency Break-Glass Component -> Audit Interceptor Component: Logs override events [Spring ApplicationEvent]

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Enforces regional infrastructure and data residency constraints.
* Java / Spring Boot & Spring Security: Core framework providing robust RBAC/ABAC and HIPAA/GDPR alignment.
* OPA (Rego / Go) Sidecar: Delivers low-latency policy evaluation for cross-border access control.
* Spring Cache / Redis: Caches tokens and active consent for degraded network conditions.
* GCP Pub/Sub: Propagates real-time global consent revocations.

## Rationale
This architecture uses regional service decomposition, sidecar pattern authorization, and Redis caching to enforce strict data residency while ensuring high availability. It satisfies complex international compliance frameworks (GDPR, HIPAA, EU MDR) through isolated audit interceptors and immutable consent ledgers.