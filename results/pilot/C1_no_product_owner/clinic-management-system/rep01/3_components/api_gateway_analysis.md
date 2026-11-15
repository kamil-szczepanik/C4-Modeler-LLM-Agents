## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMRs, appointments, and billing for healthcare facilities. It ensures HIPAA/GDPR compliance, high availability, and secure interoperability.

## Key Elements
*   Patients & Clinic Staff
*   API Gateway (NGINX/Kong with WAF, Rate Limiting, JWT/OAuth2 Filters, Routing Engine)
*   Identity Service (Keycloak)
*   Patient & EMR Service (Spring Boot)
*   Appointment Service (Spring Boot)
*   Billing Service (Spring Boot)
*   HL7 FHIR Integration Engine (Apache Camel)
*   Event Broker (Apache Kafka)
*   Primary Database & Storage (PostgreSQL & S3-compatible WORM)

## Relationships
*   Patients & Clinic Staff -> API Gateway: Accesses system features [HTTPS/TLS 1.3]
*   API Gateway -> Patient & EMR Service: Routes requests [HTTPS / mTLS (Istio)]
*   API Gateway -> Appointment Service: Routes requests [HTTPS / mTLS (Istio)]
*   API Gateway -> Billing Service: Routes requests [HTTPS / mTLS (Istio)]
*   API Gateway -> Identity Service: Validates tokens [gRPC / HTTPS]
*   Services -> Event Broker: Publishes audit/domain events [Apache Kafka / TLS]

## Technology Stack
*   NGINX/Kong: Edge routing, rate-limiting, and TLS termination for high performance.
*   Spring Boot: Microservices container framework for rapid business logic development.
*   Istio: Service mesh providing mTLS and secure service-to-service communication.
*   Keycloak: Identity and access management handling OAuth2/JWT authentication.
*   Apache Kafka: Asynchronous event broker ensuring decoupled audit logging.
*   PostgreSQL & S3: Storage layer meeting ACID compliance and 10-year data retention.

## Rationale
The hybrid architecture distributes workloads across on-premises Kubernetes and AWS eu-central-1 to achieve 99.99% active-active uptime. Strict zero-trust security controls, mTLS, and audit pipelines enforce HIPAA and GDPR mandates while maintaining low-latency EMR access.