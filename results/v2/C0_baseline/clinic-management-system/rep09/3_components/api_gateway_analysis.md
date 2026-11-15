## Overview
• Manages patient admissions, EMR, scheduling, and billing for clinics using a hybrid cloud architecture.
• Ensures HIPAA/GDPR compliance, active-active 99.99% availability, and 10-year data retention.

## Key Elements
• API Gateway (Kong / Envoy)
• Authentication & Token Validation Filter
• Rate Limiting & Throttling Engine
• Circuit Breaker & Routing Proxy
• Consent & Audit Logging Interceptor
• Enterprise Identity Provider (IdP)
• Redis Distributed Token-Bucket Store
• Audit Sidecar Container

## Relationships
• Authentication Filter -> Enterprise IdP: Validates tokens [HTTPS / OIDC via TLS]
• Rate Limiting Engine -> Redis: Reads/writes rate counters [RESP over TLS]
• API Gateway -> Core Clinical & EMR Container: Routes service requests [gRPC over mTLS]
• Audit Interceptor -> Audit Sidecar Container: Streams asynchronous audit logs [gRPC]

## Technology Stack
• Kong Enterprise / Envoy Proxy: Chosen for high-performance edge routing and security enforcement.
• Redis: Selected for distributed, low-latency rate limiting and token-bucket management.
• Envoy WASM / OpenTelemetry: Used for high-speed, asynchronous audit logging without impacting performance.
• mTLS / Istio: Implemented for zero-trust internal service-to-service communication.

## Rationale
• The distributed edge architecture and asynchronous audit interceptors protect core EMR performance to maintain <1s P95 latency.
• Active-active multi-region design across on-premise Kubernetes and AWS eu-central-1 guarantees 99.99% availability and strict compliance.