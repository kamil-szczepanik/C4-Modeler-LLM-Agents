## Overview
The Scheduling Microservice manages appointment workflows and real-time resource clash detection within a hybrid-cloud Clinic Management System. It delivers high-availability scheduling while strictly enforcing HIPAA and GDPR compliance mandates.

## Key Elements
* AppointmentController: Handles incoming gRPC routing from the API Gateway with OAuth2/OIDC.
* SchedulingEngine: Executes concurrent resource clash detection using an in-memory interval tree.
* SlotManager: Interfaces with Redis for low-latency availability state checks.
* AppointmentRepository: Manages ACID-compliant persistence and field-level PII cryptographic masking in PostgreSQL.
* AuditInterceptor: Intercepts state-changing requests to generate cryptographically-signed audit logs routed to Elasticsearch via Apache Kafka.

## Relationships
* API Gateway -> AppointmentController: Routes incoming requests via gRPC with mTLS.
* SchedulingEngine <-> SlotManager: Evaluates availability states via in-process memory calls.
* AppointmentRepository -> PostgreSQL Database: Persists appointment data using PostgreSQL protocol with AES-256 encryption.
* AppointmentRepository -> Apache Kafka: Publishes domain events and audit logs asynchronously via Messaging Backbone.

## Technology Stack
* Go: Chosen for the core scheduling engine to implement concurrent interval tree algorithms.
* gRPC with mTLS: Used for secure, high-performance inter-service communication.
* PostgreSQL: Selected for ACID-compliant structured data storage with AES-256 encryption at rest.
* Redis: Deployed for ultra-low latency caching of resource availability slots.
* Apache Kafka: Utilized as a messaging backbone for decoupled, reliable event distribution.
* Elasticsearch: Stores tamper-evident, cryptographically-signed audit logs.

## Rationale
The component architecture satisfies the 99.99% uptime and high-performance requirements through in-memory interval trees, Redis caching, and non-blocking Go routines. Strict security mandates are met via field-level PII masking and immutable, cryptographically-signed audit trails routed through Apache Kafka to Elasticsearch.