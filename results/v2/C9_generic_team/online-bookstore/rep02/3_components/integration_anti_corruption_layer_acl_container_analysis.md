## Overview
The Online Bookstore system is a scalable e-commerce platform for purchasing books, providing user reviews, and delivering personalized recommendations. It utilizes an AWS-hosted microservices architecture to ensure high availability, performance, and GDPR/CCPA compliance.

## Key Elements
* **Users:** Customers
* **External Systems:** Third-party Payment Gateway, Shipping Providers, Foreign Exchange (FX) Rate Provider, Tax Calculation Service, Anti-Fraud Service, Book Distributors, Notification Services, Identity/Compliance Services, Observability Provider, CI/CD Pipeline
* **Containers:** API Gateway (AWS API Gateway), Frontend (SPA/SSR via CDN), Core Domain Microservices, Integration / Anti-Corruption Layer (ACL) Container, Event Broker (CloudEvents), Caching/Session (Redis), Background Job Scheduler, Observability Sidecar & Config Agents (AWS Systems Manager / Secrets Manager)

## Relationships
* **Customers -> Frontend Container:** Browses catalogue, manages cart, and checks out [HTTPS]
* **Frontend Container -> API Gateway Container:** Routes client requests [HTTPS]
* **API Gateway Container -> Core Domain Containers:** Forwards validated traffic [Internal REST / gRPC]
* **Core Domain Containers -> Integration / Anti-Corruption Layer (ACL) Container:** Requests third-party integrations [Internal REST]
* **Integration / Anti-Corruption Layer (ACL) Container -> Shipping Providers, FX Provider, Tax Service:** Manages fulfillment, exchange rates, and tax calculations [HTTPS APIs with Resilience4j circuit breakers, bulkhead isolation, and token-bucket rate limiting]
* **Core Domain Containers -> Caching/Session Container:** Manages session state and caches FX rates [Redis Protocol]
* **Core Domain Containers -> Async Worker / Event Broker Container:** Publishes asynchronous events [CloudEvents]

## Technology Stack
* **Cloud Platform:** AWS (us-east-1, eu-west-1, ap-southeast-1) for global multi-region scalability.
* **API & Communication:** REST and gRPC for internal microservices; AWS API Gateway for edge routing.
* **Resilience & Fault Tolerance:** Resilience4j for circuit breakers, bulkheads, and timeout policies within the ACL.
* **Caching & State:** Redis for high-performance session management and FX rate caching.
* **Testing & Quality:** Pact for consumer-driven contract testing to prevent schema drift.

## Rationale
This architecture utilizes an Anti-Corruption Layer (ACL) with circuit breakers, bulkheads, and idempotency keys to isolate volatile third-party services, guaranteeing 99.95% uptime and sub-2-second page loads. Strict PII scrubbing and caching mechanisms ensure full GDPR/CCPA compliance while effortlessly scaling to support 1 million monthly active users.