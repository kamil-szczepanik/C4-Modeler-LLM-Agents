## Overview
- The Billing & Claims Container manages financial transactions, claim validation, and insurance submissions within the Clinic Management System.
- It ensures high-availability billing operations, HIPAA/GDPR compliance, and seamless integration with external insurance networks.

## Key Elements
- Billing API Controller (Spring Boot / Java 17)
- Claim Validation Engine
- Claim Processing Service
- Patient Invoice Generator
- Billing Data Access Layer (PostgreSQL)
- Audit Sidecar Container (HashiCorp Vault / OpenTelemetry)
- Insurance Claim Gateways

## Relationships
- API Gateway -> Billing API Controller: Routes billing requests via [gRPC over mTLS (Istio/Linkerd)]
- Claim Processing Service -> Insurance Claim Gateways: Submits claims via [mTLS with certificate pinning, OAuth2, and JWE envelope encryption]
- Billing Processing Service -> Audit Sidecar Container: Emits immutable logs and retrieves secrets via [gRPC]
- Billing Data Access Layer -> PostgreSQL: Persists billing data using [JDBC / TLS with AES-256 column-level encryption]

## Technology Stack
- Spring Boot / Java 17: Selected for robust enterprise validation frameworks and service stability.
- PostgreSQL: Provides secure, persistent relational storage for financial records.
- HashiCorp Vault: Manages dynamic secret injection and eliminates static configurations.
- Resilience4j: Implements circuit breaking to handle third-party gateway outages gracefully.
- OpenTelemetry: Enables distributed tracing and observability across hybrid Kubernetes clusters.

## Rationale
- This architecture guarantees 99.99% uptime and zero data loss through active-active Kubernetes deployments and resilient dead-letter queues.
- Strict tokenization, envelope encryption, and mTLS satisfy stringent HIPAA and GDPR security mandates.