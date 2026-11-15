## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics, ensuring HIPAA and GDPR compliance. It provides high availability, secure data storage, and interoperability through standardized healthcare protocols.

## Key Elements
- Clinic Management System [softwareSystem, context]
- Patient [person, context]
- Clinician [person, context]
- Billing/Admin Staff [person, context]
- Compliance Officer [person, context]
- Lab & Imaging Systems [externalSystem, context]
- Insurance Clearinghouse / External Billing Provider [externalSystem, context]
- Patient Portal SPA/Mobile [container] (React/TypeScript)
- Clinician/Admin Workspace SPA [container] (React/TypeScript)
- API Gateway / BFF [container] (Envoy/Kong)
- Core Services Container [container] (Java/Spring Boot)
- Billing Service Container [container] (Node.js/TypeScript)
- Integration Service Container [container] (Apache Camel / Spring Integration)
- Audit & Compliance Logging Container [container] (WORM-compliant storage / Spring Integration)
- PostgreSQL & HL7 FHIR Compliant Data Stores [container] (PostgreSQL with AES-256 at rest)
- Message Broker [container] (RabbitMQ/Kafka)

## Relationships
- Patient -> Clinic Management System [HTTPS (TLS 1.3, OAuth2/OIDC, MFA)]
- Clinician -> Clinic Management System [HTTPS (TLS 1.3, OAuth2/OIDC, MFA)]
- Billing/Admin Staff -> Clinic Management System [HTTPS (TLS 1.3, OAuth2/OIDC, MFA)]
- Compliance Officer -> Clinic Management System [HTTPS (TLS 1.3, OAuth2/OIDC, MFA)]
- Clinic Management System -> Lab & Imaging Systems [HL7 FHIR over REST/JSON (TLS 1.3)]
- Clinic Management System -> Insurance Clearinghouse / External Billing Provider [HTTPS / EDI X12]
- API Gateway / BFF -> Core Services Container [gRPC over mTLS]
- API Gateway / BFF -> Billing Service Container [gRPC over mTLS]
- Core Services Container -> PostgreSQL & HL7 FHIR Compliant Data Stores [JDBC (AES-256 at rest)]
- Billing Service Container -> Message Broker [AMQP]
- Integration Service Container -> Lab & Imaging Systems [HL7 FHIR over REST/JSON (TLS 1.3)]
- Billing Service Container -> Insurance Clearinghouse / External Billing Provider [HTTPS / EDI X12]

## Technology Stack
- Java/Spring Boot: Chosen for the Core Services Container to deliver robust clinical domain logic and meet the <1s P95 EMR performance requirement.
- React/TypeScript: Selected for user interfaces to provide high-performance, responsive frontends for patients, clinicians, and administrative staff.
- PostgreSQL with AES-256: Utilized for data stores to ensure relational integrity, HL7 FHIR compliance, and strict cryptographic data protection at rest.
- Apache Camel / Spring Integration: Deployed in the Integration Service Container to enable seamless HL7 FHIR translation and interoperability.
- Envoy/Kong: Implemented as the API Gateway / BFF for secure reverse proxying, token exchange, and routing.
- RabbitMQ/Kafka: Used as the Message Broker for decoupled, asynchronous domain events and insurance claim submissions.

## Rationale
This hybrid cloud architecture guarantees 99.99% active-active availability across on-premise Kubernetes and AWS eu-central-1 regions while adhering strictly to HIPAA and GDPR regulations. Utilizing gRPC over mTLS and local read-replicas ensures ultra-low latency for critical electronic medical records.