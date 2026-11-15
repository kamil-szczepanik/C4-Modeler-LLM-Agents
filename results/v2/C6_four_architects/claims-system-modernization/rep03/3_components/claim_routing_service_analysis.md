## Overview
[The Claim Routing Service manages high-throughput claim traffic distribution between the modern Azure cloud platform and the legacy on-premises mainframe. It ensures strict consistency, seamless fallbacks, and rapid claim-type rollbacks during the hybrid migration.]

## Key Elements
- Routing Engine Component
- State & Circuit Breaker Component
- Audit & Reconciliation Logger Component
- Mainframe Fallback Adapter Component
- Idempotency & Deduplication Guard Component
- Dynamic Routing Rule Synchronizer Component
- Distributed Tracing & Correlation Component
- Fallback Cache-Aside Guard Component
- Claim Schema Validator Component
- Secret & Endpoint Resolver Component

## Relationships
- Claims Management App -> Routing Engine [gRPC]
- Routing Engine -> Idempotency Guard [In-process]
- Idempotency Guard -> Claim Schema Validator [In-process]
- Routing Engine -> State & Circuit Breaker [In-process / Redis TCP]
- State & Circuit Breaker -> Azure Redis Cache [TCP/Redis Protocol]
- State & Circuit Breaker -> Fallback Cache-Aside Guard [In-process]
- Routing Engine -> Mainframe Fallback Adapter [gRPC]
- Mainframe Fallback Adapter -> Legacy Mainframe [MQ / HTTPS]
- Mainframe Fallback Adapter -> Secret & Endpoint Resolver [In-process / HTTPS]
- Routing Engine -> Audit Logger [Azure Service Bus / AMQP]
- Integration & Sync Service -> Dynamic Routing Rule Synchronizer [Azure Service Bus / AMQP]
- Dynamic Routing Rule Synchronizer -> State & Circuit Breaker [In-process / Redis]
- Routing Engine & Mainframe Fallback Adapter -> Distributed Tracing Component [In-process]
- Distributed Tracing Component -> Observability & Audit Container [OpenTelemetry / HTTPS]

## Technology Stack
- Java 17 / Spring Boot: Stateless enterprise runtime chosen for team familiarity given cloud inexperience.
- Resilience4j + Azure Redis Cache: Circuit breaker and distributed cache for dynamic failovers and rollbacks.
- Apache Camel: Enterprise integration patterns for legacy mainframe payload transformation.
- Spring Data Redis & Caffeine Cache: Idempotency enforcement and high-availability in-memory caching.
- Micrometer Tracing & OpenTelemetry: Unified end-to-end telemetry across hybrid boundary.
- Azure Key Vault: Secure credential and mTLS certificate management.

## Rationale
[This component architecture guarantees zero data loss and sub-second routing decisions while bridging modern cloud services with the legacy mainframe. It provides isolated rollback capabilities per claim type to satisfy strict migration constraints.]