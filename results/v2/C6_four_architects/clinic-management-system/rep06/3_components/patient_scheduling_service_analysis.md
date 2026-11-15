## Overview
The Patient & Scheduling Service is a core Java/Spring Boot container within the Clinic Management System responsible for handling patient admissions, scheduling, and interoperability. It ensures high availability, strict HIPAA/GDPR compliance, and robust resource clash prevention for medium-sized healthcare facilities.

## Key Elements
* Patient Management Controller (Spring MVC)
* Scheduling Engine Component (Spring Service)
* FHIR Mapping Adapter Component (Apache Camel / Spring Integration)
* Audit Interceptor Component (Spring AOP)
* Notification Trigger Component (Spring Event Listener)
* Domain Event Publisher Component (Spring AMQP / Kafka Client)
* Data Access Repository Layer (Spring Data JPA)

## Relationships
* API Gateway -> Patient Management Controller: Routes demographic and scheduling requests [gRPC]
* Scheduling Engine Component -> Distributed Cache: Acquires atomic resource locks [Redis Protocol over TLS]
* Scheduling Engine Component -> Patient DB: Reads/writes appointment data [TLS-encrypted SQL]
* Domain Event Publisher Component -> Async Message Broker: Emits domain events [AMQP/Kafka]
* Notification Trigger Component -> Hospital Notification/SMS Gateway: Dispatches appointment alerts [REST/HTTPS]

## Technology Stack
* Java / Spring Boot: Provides a modular monolith framework for rapid domain isolation and high availability.
* Redis: Used for distributed caching and atomic resource locking to prevent appointment clashes in active-active setups.
* Spring AOP: Captures audit logs transparently without business logic pollution for HIPAA/GDPR compliance.
* Apache Camel / Spring Integration: Translates internal models to HL7 FHIR standards for external interoperability.

## Rationale
This architecture utilizes a modular Spring Boot container combined with Redis-backed locking to ensure sub-second performance and zero double-booking under high concurrency. Cross-cutting audit and integration adapters guarantee strict regulatory compliance without compromising core transaction throughput.