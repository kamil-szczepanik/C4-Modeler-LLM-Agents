## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and seamless interoperability.

## Key Elements
- **Users**: Patient, Clinician / Receptionist
- **External Systems**: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Notification Service, On-Premise K8s / AWS Infrastructure
- **Containers**: API Gateway (Kong/NGINX), Patient & Scheduling Service, EMR Service, Billing & Claims Service, Integration Service, Audit Service, Apache Kafka, PostgreSQL, Redis, Elasticsearch / WORM storage
- **Billing & Claims Service Components**: `BillingController`, `InvoiceManager`, `ClaimsProcessor`, `PaymentAdapter`, `BillingRepository`, `CircuitBreakerMiddleware`, `AuditInterceptor`

## Relationships
- **API Gateway -> Billing & Claims Service**: Routes requests via [gRPC]
- **Billing & Claims Service -> PaymentAdapter -> Clearinghouse**: Transmits claims via [HTTPS/REST, TLS 1.3]
- **BillingRepository -> PostgreSQL**: Persists data via [Encrypted TCP with AES-256]
- **Billing & Claims Service -> Apache Kafka**: Publishes events and audit logs via [mTLS]

## Technology Stack
- **Languages & Frameworks**: Spring Boot (Java), Node.js (TypeScript), Express
- **Databases & Storage**: PostgreSQL (AES-256 at rest), Redis, Elasticsearch / WORM storage
- **Messaging & Integration**: Apache Kafka, Apache Camel / Spring Integration, FHIR Adapter
- **Resilience & Security**: Opossum (Circuit Breaker), mTLS, TLS 1.3

## Rationale
The hybrid architecture utilizes Kubernetes and AWS to guarantee 99.99% active-active availability. AES-256 encryption, strict audit logging, and FHIR standards satisfy rigorous HIPAA, GDPR, and interoperability mandates.