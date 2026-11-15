## Overview
The EMR & Audit Service is a core Java Spring Boot component of the Clinic Management System designed to handle clinical data and compliance. It ensures high availability, strict HIPAA/GDPR adherence, and rapid <1s P95 response times.

## Key Elements
- EMR Management Controller / Service (Java Spring Boot)
- HL7 FHIR Interoperability Adapter (HAPI FHIR library)
- Audit Trail Interceptor (Spring AOP)
- WORM Storage Exporter (Async Java worker)
- EMR Cache Layer (Redis)

## Relationships
- API Gateway -> EMR Management Controller: Routes EMR requests [Internal gRPC/REST over TLS 1.3]
- EMR Management Controller -> EMR Cache Layer: Reads patient records [Redis Protocol over TLS]
- EMR Management Controller -> PostgreSQL Primary DB: Reads/writes clinical data [JDBC / TLS 1.3]
- Audit Trail Interceptor -> Async Message Broker: Publishes audit events [Apache Kafka]
- HL7 FHIR Interoperability Adapter -> External Lab & Imaging Systems: Exchanges test results [HL7 FHIR APIs]
- WORM Storage Exporter -> WORM-compliant storage: Archives immutable logs [HTTPS / S3 Object Lock API]

## Technology Stack
- Java Spring Boot: Robust framework for enterprise microservices and dependency injection
- HAPI FHIR Library: Standardized tooling for healthcare data interoperability
- Spring AOP: Aspect-oriented programming for transparent, non-invasive audit logging
- Redis: In-memory distributed cache to achieve <1s P95 read performance
- Apache Kafka: Reliable event streaming for asynchronous audit processing
- PostgreSQL & S3 Object Lock: Persistent transactional storage with AES-256 and immutable 10-year retention

## Rationale
This component architecture uses specialized caching and AOP logging to meet strict sub-second performance and HIPAA compliance goals simultaneously. Standardized FHIR adapters and WORM storage ensure seamless external integration and robust long-term regulatory compliance.