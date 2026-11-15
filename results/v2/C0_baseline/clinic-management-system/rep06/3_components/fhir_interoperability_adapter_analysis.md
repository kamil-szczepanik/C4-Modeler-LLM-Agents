## Overview
- The system is a Clinic Management System designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing.
- It ensures HIPAA/GDPR compliance, 99.99% availability, and secure interoperability via a hybrid cloud infrastructure.

## Key Elements
- External Lab & Imaging Systems
- Identity Provider (IdP)
- FHIR Interoperability Adapter (HAPI FHIR container)
- FHIR REST Facade
- Security & Auth Enforcer
- Transformation Engine
- Outbound Dispatcher
- Audit Logger Interceptor
- Message Broker (Kafka)
- Core Clinical & EMR Service
- Audit & Compliance Service

## Relationships
- External Lab & Imaging Systems -> FHIR REST Facade: Exchanges lab/imaging data [HL7 FHIR API over mTLS]
- FHIR REST Facade -> Security & Auth Enforcer: Validates credentials [In-process Java]
- Security & Auth Enforcer -> Identity Provider (IdP): Token introspection & JWT verification [OAuth 2.0 / OIDC]
- FHIR REST Facade -> Transformation Engine: Direct method calls [Java]
- Transformation Engine -> Message Broker (Kafka): Publishes clinical events asynchronously [Kafka Protocol]
- Message Broker (Kafka) -> Core Clinical & EMR Service: Consumes events [gRPC/Protobuf]
- FHIR Interoperability Adapter -> Audit & Compliance Service: Emits audit trails [gRPC over mTLS]

## Technology Stack
- HAPI FHIR: Chosen for standards-compliant HL7 FHIR US Core / European profile support.
- Apache Kafka: Used for asynchronous buffering between the adapter and core EMR to prevent cascading failures.
- Java Spring Boot: Underlying framework for high-performance microservice components.
- AES-256: Utilized for data encryption at rest, including DLQ exception storage.
- Mutual TLS (mTLS): Enforces zero-trust hybrid perimeter security.

## Rationale
- The hybrid active-active architecture with Kafka buffering guarantees 99.99% availability and resilience against network partitions.
- Strict perimeter schema validation, mTLS, and SMART-on-FHIR scopes satisfy HIPAA/GDPR security mandates.