## Overview
The Go EMR Service is a core backend component of the Clinic Management System, managing electronic medical records and clinical workflows. It ensures sub-second retrieval, high availability, and strict HIPAA and GDPR compliance across a hybrid infrastructure.

## Key Elements
- `EMR Query Handler`: Manages read-optimized queries with Redis caching
- `Clinical Command Processor`: Executes write operations with Go routines and attribute-based access control (ABAC)
- `Audit Log Interceptor`: Generates immutable, cryptographically signed audit trails
- `FHIR Adapter`: Translates internal models to HL7 FHIR resources
- `Data Masking Engine`: Dynamically redacts and tokenizes Protected Health Information (PHI)
- `Async Event Publisher`: Streams domain mutation events asynchronously

## Relationships
- API Gateway -> Go EMR Service: Routes requests using gRPC and REST over mTLS
- Go EMR Service -> PostgreSQL Cluster: Persists transactional data with AES-256 storage encryption
- Go EMR Service -> Redis Cluster: Caches read-optimized data using TLS
- Go EMR Service -> Apache Kafka Event Bus: Streams asynchronous events using payload-level encryption (JWE)

## Technology Stack
- Go: Chosen for high-throughput, low-latency inter-service execution via gRPC and Go routines
- PostgreSQL Cluster: Provides ACID compliance with AES-256 encryption at rest
- Redis Cluster: Enables sub-second P95 caching performance with Redis Sentinel
- Apache Kafka: Handles reliable, decoupled asynchronous event publishing with dead-letter queues

## Rationale
This architecture uses Go-based concurrency and read-optimized caching to consistently achieve sub-second P95 response times for clinicians. It combines cryptographic auditing, JWE encryption, and strict isolation layers to fulfill 99.99% availability and rigorous healthcare compliance standards.