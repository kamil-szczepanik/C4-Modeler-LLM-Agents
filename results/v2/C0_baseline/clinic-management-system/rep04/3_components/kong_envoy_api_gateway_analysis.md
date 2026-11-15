## Overview
[The Clinic Management System is a hybrid-cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures high availability, strict HIPAA and GDPR compliance, and seamless integration with external clinical systems.]

## Key Elements
* Kong/Envoy API Gateway (Control Plane & Data Planes)
* Routing & Upstream Matcher (Envoy Router with Coraza/ModSecurity WAF)
* Authentication & Authorization Filter (Kong Auth Plugin / Envoy WASM/Lua)
* Rate Limiting & Throttling Engine (Kong Rate Limiting)
* Audit & Telemetry Logger (Kong Logging / Envoy Access Log Service)
* Identity Provider (IdP)
* Redis Enterprise Caching Layer
* Apache Kafka Event Stream
* Core Services & Billing Service (Istio Service Mesh)
* HashiCorp Vault

## Relationships
* Client to Kong/Envoy API Gateway: HTTPS/TLS 1.3
* Authentication & Authorization Filter to Identity Provider: HTTPS / OIDC
* Rate Limiting & Throttling Engine to Redis Enterprise: RESP over TLS / TCP
* Routing & Upstream Matcher to Core Services & Billing Service: gRPC/REST over mTLS (Istio)
* Audit & Telemetry Logger to Apache Kafka: Kafka Protocol over TLS
* Data Planes to HashiCorp Vault: TLS / gRPC for short-lived certificate rotation

## Technology Stack
* Kong/Envoy: Edge proxy and API gateway for routing, security, and telemetry.
* Coraza / ModSecurity: Web Application Firewall (WAF) plugin for OWASP Top 10 mitigation.
* Redis Enterprise: Distributed active-active cache for tenant-aware rate limiting.
* Apache Kafka: Event stream for asynchronous, HMAC-signed audit logs and OpenTelemetry spans.
* Istio Service Mesh: Manages mTLS and traffic between gateway data planes and backend services.
* HashiCorp Vault: Dynamic secret management and automated certificate rotation (≤ 30 days).

## Rationale
[This architecture utilizes a distributed Kong/Envoy data-plane model combined with Redis Enterprise active-active caching to guarantee 99.99% uptime and low-latency EMR access across hybrid regions. Robust edge security, mTLS enforcement, and HMAC-signed audit logging satisfy rigorous HIPAA and GDPR compliance requirements.]