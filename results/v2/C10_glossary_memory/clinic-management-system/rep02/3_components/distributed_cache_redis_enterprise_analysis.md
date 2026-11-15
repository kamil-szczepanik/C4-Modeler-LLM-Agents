## Overview
- Manages high-performance distributed session state, real-time messaging, and transient caching for the Clinic Management System.
- Ensures sub-second EMR screen loads and 99.99% availability while maintaining HIPAA and GDPR compliance across hybrid cloud deployments.

## Key Elements
- In-Memory Data Store (Redis Core / Redis Enterprise Active-Active CRDTs)
- Cluster Manager & Proxy (Envoy/Redis-Proxy)
- Pub/Sub & WebSocket Engine (Redis native Pub/Sub)
- Unified API Gateway
- EMR Microservice
- Scheduling Microservice
- Patient Portal / Mobile App
- HashiCorp Vault

## Relationships
- Unified API Gateway -> Distributed Cache (Redis Enterprise): RESP / mTLS 1.3 for session management and WebSocket pub/sub messaging
- EMR Microservice -> Distributed Cache (Redis Enterprise): RESP / mTLS 1.3 for transient data caching
- Scheduling Microservice -> Distributed Cache (Redis Enterprise): RESP / mTLS 1.3 for calendar lock states
- HashiCorp Vault -> Distributed Cache (Redis Enterprise): Automated TLS certificate and AUTH token rotation via API

## Technology Stack
- Redis Enterprise Software: Chosen for active-active CRDT multi-region synchronization supporting high availability and sub-millisecond retrieval.
- Envoy / Redis-Proxy: Selected for intelligent client routing, connection pooling, and TLS termination.
- Redis ACLs: Implemented for strict least-privilege microservice authorization per key namespace.
- AES-256 and Kubernetes Storage Encryption: Applied to AOF persistence volumes for data-at-rest protection.

## Rationale
- This architecture guarantees sub-second EMR performance and 99.99% uptime across hybrid on-prem and cloud regions.
- Enforced mTLS 1.3, Redis ACLs, and tokenized cache handles satisfy rigorous HIPAA and GDPR security constraints.