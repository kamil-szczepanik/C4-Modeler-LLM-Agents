## Overview
Component-level architecture for the Clinic Management System's EMR Service container, built with Java and Spring Boot. It processes clinical notes, maintains immutable audit trails, and ensures secure interoperability.

## Key Elements
- **EMR API Controller** (Spring MVC): Exposes REST/gRPC endpoints and routes requests.
- **Clinical Record Manager** (Spring Service): Core business logic for clinical notes and treatments.
- **Audit Trail Logger** (Spring AOP / Aspect): Intercepts operations for tamper-evident logs.
- **Encryption Interceptor** (Hibernate / JPA Attribute Converter): Enforces AES-256 field-level encryption for PHI.
- **EMR Cache Manager** (Spring Data Redis) with **Cache Encryption Utility**: Manages and encrypts hot patient records in cache.
- **FHIR Transformer Component** (HAPI FHIR Library): Maps internal clinical models to HL7 FHIR standards.
- **Circuit Breaker & Fallback Manager** (Resilience4j): Provides fault tolerance for database and broker calls.
- **Async Event Publisher** (Spring Application Events / Kafka Template): Decouples domain actions from event dispatching.

## Relationships
- `EMR API Controller` -> `FHIR Transformer Component`: Converts inbound/outbound payloads [Java Method Call]
- `Clinical Record Manager` -> `Encryption Interceptor`: Secures PHI payload [JPA lifecycle hooks]
- `Clinical Record Manager` -> `EMR Cache Manager`: Reads/writes hot clinical records [Lettuce / TCP]
- `EMR Cache Manager` -> `Cache Encryption Utility`: Encrypts/decrypts cached PHI [Java Method Call]
- `Clinical Record Manager` -> `Circuit Breaker & Fallback Manager`: Invokes guarded persistence [Java Method Call]
- `Circuit Breaker & Fallback Manager` -> `Database Access Proxy`: Executes queries [JDBC over TCP]
- `Clinical Record Manager` -> `Async Event Publisher`: Dispatches domain events [Java Method Call]
- `Async Event Publisher` -> `Message Broker`: Publishes asynchronous events [SASL/SCRAM over TLS]

## Technology Stack
- **Java / Spring Boot**: Core container framework for robust enterprise services.
- **HAPI FHIR Library**: Standardized parsing for HL7 FHIR interoperability.
- **Resilience4j**: Ensures high availability and fault tolerance.
- **Redis Enterprise & Lettuce**: Delivers sub-second P95 read performance via caching.
- **Hibernate / JPA**: Manages transparent field-level encryption.

## Rationale
The component architecture enforces HIPAA and GDPR compliance through strict AES-256 encryption and immutable audit logging. It achieves high availability and sub-second performance via circuit breakers and secure distributed caching.