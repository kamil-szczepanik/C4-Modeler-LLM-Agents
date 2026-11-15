## Overview
- System: Library Management System (LMS) core domain service container for cataloging and circulation management.
- Purpose: Delivers secure, high-performance cataloging and circulation workflows while strictly enforcing EU data residency.

## Key Elements
- Catalog Management Component (Spring `@Service`, Java)
- Circulation Workflow Component (Spring `@Service`, Java)
- Domain Event Publisher (Spring Event / Kafka Template, Java)
- Patron Account & Policy Engine Component (Spring `@Service`, Java)
- Search Integration Facade (Spring `@Component`, Java)
- Data Governance & Audit Interceptor (Spring `@Aspect`, Java)
- Domain Health & Metrics Actuator (Spring Boot Actuator, Java)

## Relationships
- API Gateway -> Catalog & Circulation Components: REST/TLS (JSON payloads)
- Catalog & Circulation -> Database: JDBC over SSL via HikariCP connection pooling
- Catalog Management Component -> Search Integration Facade: Synchronous Spring ApplicationEvent (in-memory)
- Circulation Workflow Component -> Patron Account & Policy Engine: In-memory Java method call
- Catalog & Circulation Components -> Data Governance & Audit Interceptor: In-memory AOP method invocation
- Domain Event Publisher & Search Integration Facade -> Message Broker: Apache Kafka (TCP, TLS-encrypted)
- Kubernetes Platform Monitor -> Domain Health & Metrics Actuator: Prometheus scraping / HTTP (TLS)

## Technology Stack
- Spring Boot (Java): Provides the modular monolith framework for core domain logic
- Spring Data JPA: Manages physical and digital item persistence
- Apache Kafka: Handles asynchronous event emission for search indexing and downstream workers
- Spring AOP: Intercepts persistence and events for GDPR compliance and data residency
- Spring Boot Actuator: Exposes internal health probes and Prometheus metrics

## Rationale
- Modular Spring `@Service` boundaries enforce strict separation of concerns while keeping internal calls in-memory for zero overhead.
- Transactional outbox patterns and AOP-based data governance safeguard low-latency performance targets and strict EU data residency constraints.