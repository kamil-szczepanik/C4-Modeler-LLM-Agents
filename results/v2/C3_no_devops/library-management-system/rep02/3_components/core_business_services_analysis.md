## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and sub-second search performance.

## Key Elements
- **Core Business Services Container**: Java / Spring Boot container executing core business logic.
- **Search Orchestrator Component**: Java / Spring WebFlux reactive component for non-blocking search aggregation.
- **Circulation Engine Component**: Java / Spring Boot with Spring Data JPA for transactional safety.
- **Fulfillment & Reservation Component**: Java / Spring Boot component managing waitlists and hold expirations.
- **Integration Component**: Spring Integration handling asynchronous event streams.
- **External Systems**: Payment Gateway, Digital Content Providers, Notification System, Analytics Worker, and PostgreSQL managed database.

## Relationships
- **API Gateway -> Core Business Services**: Forwards internal requests via gRPC / REST with mTLS.
- **Core Business Services -> PostgreSQL Database**: Reads and writes business data via secure PostgreSQL protocol with AES-256 encryption.
- **Core Business Services -> Apache Kafka**: Streams business events and analytics via mTLS with PII redaction.
- **Core Business Services -> Payment Gateway**: Processes fees using HTTPS/REST with tokenization.
- **Core Business Services -> Notification System**: Sends automated alerts via Apache Kafka and HTTPS/REST with mTLS.

## Technology Stack
- **Java 17 / Spring Boot & Spring WebFlux**: Chosen for transactional safety and reactive non-blocking I/O to meet <800ms search latency.
- **Spring Data JPA**: Ensures consistent state management for loans, fines, and reservations.
- **Apache Kafka / Spring Integration**: Facilitates non-blocking event-driven messaging and analytics streaming.
- **HashiCorp Vault**: Manages secure secrets injection via ephemeral IAM roles.
- **TLS 1.3 & AES-256**: Enforces strict data-in-transit and data-at-rest encryption for EU compliance.

## Rationale
This architecture uses reactive programming and internal component decomposition to achieve high-performance search (<800ms) while maintaining strict transactional integrity for circulation and reservations. It adheres to EU data residency and security mandates through robust encryption, RBAC, and isolated trust boundaries.