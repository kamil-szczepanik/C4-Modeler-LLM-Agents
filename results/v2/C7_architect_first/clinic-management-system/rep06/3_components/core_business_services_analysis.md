## Overview
The Clinic Management System is a hybrid cloud clinical IT platform providing patient admissions, scheduling, EMR, and billing for healthcare facilities. It ensures 99.99% availability, strict HIPAA/GDPR compliance, and sub-second P95 performance.

## Key Elements
- Patient Management Component
- Scheduling Engine Component
- EMR Core Component
- Billing Service Component
- CockroachDB
- Redis
- WORM Audit Store
- External KMS (HashiCorp Vault)
- API Gateway

## Relationships
- API Gateway -> Core Components: Routes requests via gRPC over mTLS (Istio)
- Scheduling Engine -> Redis: Acquires distributed locks via Redis RESP / TLS
- EMR Core & Patient Management -> CockroachDB: Executes ACID transactions via JDBC / TLS
- EMR Core -> WORM Audit Store: Writes guaranteed-delivery audit trails using the transactional outbox pattern
- Core Components -> HashiCorp Vault: Performs envelope encryption via TLS

## Technology Stack
- Java Spring Boot: Core component implementation framework for robust enterprise domain handling
- CockroachDB: Distributed SQL database providing active-active multi-region resiliency
- Redis: In-memory data store for high-performance appointment locking
- Istio: Service mesh handling mTLS, SPIFFE/SPIRE identity, and circuit breaking
- Protocol Buffers: Binary serialization format ensuring sub-second P95 gRPC performance
- HashiCorp Vault: External key management system for AES-256 column-level envelope encryption

## Rationale
This architecture combines active-active distributed databases with Istio service meshes to guarantee 99.99% availability across hybrid infrastructures. It balances stringent HIPAA/GDPR security, such as column-level encryption and outbox-pattern audit trails, with high-performance gRPC communication to meet strict sub-second clinical latency targets.