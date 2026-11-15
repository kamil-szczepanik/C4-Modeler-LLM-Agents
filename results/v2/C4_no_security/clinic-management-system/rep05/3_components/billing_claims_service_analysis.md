## Overview
The Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing capabilities for clinics. It ensures HIPAA and GDPR compliance, 99.99% availability, and a 10-year data retention policy.

## Key Elements
- SPA Frontend (React, TypeScript, Nginx)
- Billing & Claims Service (Spring Boot, Java)
- Claim Generation & Scrubbing Engine (Spring Integration / Drools)
- Insurance Clearinghouse Adapter (Spring Cloud OpenFeign / Resilience4j)
- Payment Gateway Module (Spring WebFlux)
- Payer Rule Management Component (Spring Data JPA / Redis)
- Billing Controller (Spring MVC / WebFlux)
- External Insurance Clearinghouses
- Apache Kafka & PostgreSQL

## Relationships
- SPA Frontend -> Billing Controller: Requests billing data and operations [HTTPS / WSS]
- Billing Controller -> Payment Gateway Module: Triggers payment processing [Synchronous REST / HTTPS]
- Claim Generation & Scrubbing Engine -> Payer Rule Management Component: Fetches active rules [In-memory cache read / Redis]
- Claim Generation & Scrubbing Engine -> Insurance Clearinghouse Adapter: Internal handoff [In-memory / Java Method]
- Insurance Clearinghouse Adapter -> Insurance Clearinghouses: Submits claims [HTTPS / REST over TLS 1.3]
- Billing & Claims Service -> Apache Kafka: Streams billing events [TCP event streaming]
- Billing & Claims Service -> PostgreSQL: Reads and writes billing data [TCP with AES-256 encryption at rest]

## Technology Stack
- Java 17 & Spring Boot: Core framework for microservices
- Spring Integration / Drools: Powers the claim scrubbing engine
- Spring Cloud OpenFeign & Resilience4j: Handles resilient external communication
- Spring WebFlux & Spring MVC: Manages asynchronous and synchronous endpoints
- Redis Cache: Ensures low-latency rule evaluation
- Apache Kafka: Event streaming and cache invalidation messaging
- PostgreSQL with Patroni: Primary-replica relational data storage with AES-256 encryption at rest

## Rationale
This architecture uses modular Spring Boot components with aggressive failure isolation to guarantee high availability and resilient external integration. Furthermore, Redis caching and secure database encryption satisfy strict performance thresholds and HIPAA/GDPR compliance mandates.