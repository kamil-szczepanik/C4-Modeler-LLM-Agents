## Overview
The Currency Localization Container manages real-time currency conversion, geo-IP fallback, and multi-currency pricing (USD, EUR, GBP) for the global online bookstore. It ensures high availability and financial accuracy across multiple AWS regions while mitigating systemic checkout failures.

## Key Elements
- **Global Shopper:** End-user browsing catalogue and executing secure checkouts.
- **Site Administrator:** Manages exchange-rate overrides and operational configurations.
- **Currency Localization Container:** Core microservice handling currency conversion logic.
- **Redis Cache:** Low-latency store for cached exchange rates and geo-IP mapping data.
- **Third-Party Financial APIs:** External providers supplying daily exchange rates.
- **AWS KMS:** Encryption service for securing data at rest.

## Relationships
- API Gateway -> Currency Localization Container: Routes internal requests via mTLS [Istio service mesh].
- Currency Localization Container -> Redis Cache: Retrieves and caches exchange rates [TCP].
- Currency Localization Container -> Third-Party Financial APIs: Fetches daily exchange rates [TLS 1.3 with egress filtering].
- Site Administrator -> Currency Localization Container: Executes administrative overrides via secure portal [HTTPS/JWT].

## Technology Stack
- **Amazon EKS:** Container orchestration platform ensuring scalable, multi-region deployments.
- **Redis:** In-memory cache for fallback exchange rates and geo-IP data.
- **AWS X-Ray / OpenTelemetry:** Distributed tracing for monitoring request latency and failures.
- **AWS KMS:** Encryption at rest for cached financial and geo-IP data.
- **Argo Rollouts:** Progressive canary deployments for safe release management.

## Rationale
This architecture guarantees 99.95% uptime and sub-2-second performance through regional isolation, Redis caching, and circuit breaking. It ensures GDPR compliance, robust security, and uninterrupted checkout flows even during third-party financial API outages.