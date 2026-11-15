## Overview
The EU E-Prescriptions Adapter processes and routes electronic prescriptions for patients in the EU, translating canonical models to meet diverse national standards. It operates securely within GCP region europe-west3, ensuring strict GDPR compliance and regional data residency.

## Key Elements
- Core Telehealth Backend
- Prescription Transformation Engine (Java / MapStruct)
- Gateway Resilience & Routing Module (Spring Cloud OpenFeign / Resilience4j)
- Security & Cryptography Interceptor (Spring Security / GCP Secret Manager)
- Audit & Compliance Logger (Spring AOP / SLF4J)
- National e-Prescription Gateways
- GCP Pub/Sub Dead-Letter Queue (DLQ) with Cloud KMS

## Relationships
- Core Telehealth Backend -> Prescription Transformation Engine: Submits canonical prescription DTOs [gRPC]
- Prescription Transformation Engine -> Gateway Resilience & Routing Module: Passes validated payloads [In-memory]
- Gateway Resilience & Routing Module -> National e-Prescription Gateways: Dispatches prescriptions [Egress-filtered HTTPS / mTLS]
- Gateway Resilience & Routing Module -> GCP Pub/Sub DLQ: Queues failed transmissions [Encrypted Pub/Sub Protocol]

## Technology Stack
- Java / Spring Boot: Core framework for enterprise service reliability and modularity
- Spring Cloud OpenFeign & Resilience4j: Handles dynamic routing and circuit breaking against unstable endpoints
- GCP Secret Manager & Cloud KMS: Provides dynamic mTLS certificate injection and at-rest CMEK encryption
- GCP Pub/Sub: Manages persistent asynchronous queuing for offline fallback processing

## Rationale
This architecture ensures strict regulatory compliance and high availability across fragmented international health systems. It isolates unreliable national infrastructures while enforcing end-to-end data security and residency standards required by the EU.