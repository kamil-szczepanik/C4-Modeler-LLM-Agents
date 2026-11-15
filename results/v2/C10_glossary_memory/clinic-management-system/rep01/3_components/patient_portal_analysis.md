## Overview
The Patient Portal container enables patients to manage appointments and view personal health records for the Clinic Management System (CMS). It ensures HIPAA and GDPR compliance while targeting 99.99% availability and high performance.

## Key Elements
* **Patients** [person, context]
* **Identity Provider (IdP)** [externalSystem, context]
* **API Gateway** [container, container]
* **Patient Portal** [container, container]
* **Portal API Controller** [component] (Node.js / Express)
* **Appointment Self-Service Module** [component] (TypeScript)
* **Record Viewer Service** [component] (TypeScript)
* **Patient Web Frontend** [component] (React / Next.js)
* **Patient Cache Manager** [component] (Redis)
* **Core Datastore** [container, container] (PostgreSQL with CQRS)
* **Hardware Security Module (HSM)** [container, container] (FIPS 140-2 Hardware)
* **WORM Audit Logging Service** [container, container] (Secure Storage)

## Relationships
* **Patients** -> **API Gateway**: HTTPS (TLS 1.3), OAuth 2.0 / OIDC, MFA
* **API Gateway** -> **Patient Portal** (**Portal API Controller**): gRPC over mTLS (Mutual TLS 1.3), SPIFFE/SPIRE X.509 certs
* **Portal API Controller** -> **Appointment Self-Service Module**: In-process gRPC / TypeScript function calls
* **Portal API Controller** -> **Record Viewer Service**: In-process gRPC / TypeScript function calls
* **Appointment Self-Service Module** -> **Core Datastore**: PostgreSQL queries via localized read replicas
* **Record Viewer Service** -> **Patient Cache Manager**: Read-through caching via TLS 1.3 over internal service mesh
* **Patient Cache Manager** -> **Core Datastore**: Localized read replicas
* **Patient Portal** -> **Hardware Security Module (HSM)**: FIPS 140-2 / AES-256 for field-level encryption
* **Patient Portal** -> **WORM Audit Logging Service**: Asynchronous secure logging of interactions and cache access

## Technology Stack
* **Kubernetes**: Container orchestration providing HPA, PodDisruptionBudgets, and active-active scaling for 99.99% uptime (R-06).
* **Node.js / Express**: Runtime and framework for the Portal API Controller handling asynchronous gRPC traffic.
* **React / Next.js**: Frontend framework delivering a mobile-responsive UI with Content Security Policies.
* **Redis**: In-memory cache manager with TLS 1.3 and strict memory eviction policies for sub-second P95 performance (R-07).
* **PostgreSQL (CQRS)**: Relational datastore optimized with localized read replicas.
* **AES-256 & FIPS 140-2 HSM**: Cryptographic algorithms and hardware modules for data-at-rest security (R-05).

## Rationale
This architecture decouples the patient-facing interface from internal clinical workflows using a secure Kubernetes-based container boundary. It balances strict HIPAA/GDPR data-isolation and encryption mandates with high-performance caching to meet sub-second response time goals.