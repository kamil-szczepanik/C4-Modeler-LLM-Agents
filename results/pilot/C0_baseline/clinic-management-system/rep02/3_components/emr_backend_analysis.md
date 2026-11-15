## Overview
• The EMR Backend is a core clinical Java Spring Boot service managing electronic medical records, clinical logic, and regulatory audit trails.
• It provides high-performance, compliant data access for medical staff to ensure rapid, secure patient care across hybrid hospital environments.

## Key Elements
• EMR Orchestrator (Spring WebFlux)
• Clinical Data Access Layer (Spring Data JPA)
• FHIR Interoperability Adapter
• Audit Log Interceptor
• In-Memory Clinical Cache (Hazelcast)
• FHIR Event Consumer
• PostgreSQL & WORM Storage
• Apache Kafka Event Broker

## Relationships
• Physician EMR Frontend -> EMR Orchestrator: Requests clinical data [gRPC with mTLS]
• EMR Orchestrator -> Clinical Data Access Layer: Queries and persists patient records [Encrypted TCP (AES-256)]
• FHIR Interoperability Adapter -> External Systems: Exchanges medical data [REST/HTTPS via HL7 FHIR]
• FHIR Event Consumer -> Apache Kafka: Ingests clinical events [TLS and SCRAM-SHA-512]
• EMR Backend -> WORM Storage: Writes immutable audit logs [Cryptographic verification]
• EMR Backend nodes -> EMR Backend nodes: Clusters cache replication [TLS 1.3 mTLS]

## Technology Stack
• Java Spring Boot: High-throughput enterprise backend framework
• Spring WebFlux: Reactive, non-blocking request handling for low latency
• Hazelcast: In-memory distributed caching for emergency room offline resilience
• Apache Kafka: Asynchronous event streaming for decoupled lab ingestion
• PostgreSQL & WORM Storage: Dual persistence model for transactional data and tamper-evident audit logs
• HikariCP: High-performance database connection pooling

## Rationale
• Reactive components, distributed caching, and non-blocking I/O satisfy the sub-second P95 performance constraint (R-07) and 99.99% availability (R-06).
• Integrated cryptographic controls, TLS 1.3, AES-256 encryption, and WORM storage ensure strict HIPAA and GDPR compliance.