## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and low-latency clinical workflows.

## Key Elements
- **API Gateway / Edge Proxy:** NGINX / Envoy
- **Core Clinical & EMR Service:** Java / Spring Boot container
- **Internal Components:** Patient Record Manager, Authorization & Policy Engine, Audit Logging Interceptor, FHIR Interoperability Adapter, Crypto & Key Management Facade
- **Datastores & Logs:** PostgreSQL, Immutable Audit Log (AWS QLDB / Append-only Postgres), Local Durable Buffer
- **External Systems:** On-Premises Hardware Security Module (HSM), External Lab & Imaging Systems

## Relationships
- **API Gateway -> Authorization & Policy Engine:** Routes internal requests via gRPC
- **Authorization & Policy Engine -> Patient Record Manager:** Evaluates fine-grained access via In-process calls
- **Patient Record Manager -> PostgreSQL:** Reads and writes clinical data via JDBC/TLS with mTLS
- **Audit Logging Interceptor -> Immutable Audit Log:** Appends audit events via JDBC/TLS with local buffer fallback
- **Crypto & Key Management Facade -> On-Premises HSM:** Manages envelope encryption keys via Secure Hardware Interface
- **FHIR Interoperability Adapter -> External Lab & Imaging Systems:** Exchanges clinical data via HL7 FHIR over REST/TLS 1.3

## Technology Stack
- **Backend Services:** Java / Spring Boot for high-performance enterprise clinical operations
- **Inter-service Communication:** gRPC over Istio Service Mesh with strict mTLS for secure, low-latency microservice calls
- **Data Protection:** AES-256 encryption at rest utilizing an On-Premises HSM with short-lived memory-zeroized DEK caching
- **Resilience & Interoperability:** Resilience4j for circuit breaking and HAPI FHIR library for standardized healthcare data exchange

## Rationale
This architecture uses a hybrid deployment across on-premise Kubernetes and AWS eu-central-1 to achieve 99.99% active-active availability while retaining sensitive data locally. Decoupled security components and local caching strategies ensure sub-second P95 EMR load times without compromising stringent HIPAA audit and encryption mandates.