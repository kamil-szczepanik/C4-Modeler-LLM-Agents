## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals to handle patient admissions, electronic medical records, scheduling, and billing. It ensures HIPAA/GDPR compliance, high availability (99.99%), and robust interoperability via HL7 FHIR APIs.

## Key Elements
- Patients / Consumers
- Clinic Staff / Receptionists
- Healthcare Providers (Doctors/Nurses)
- System Administrators / Compliance Officers
- Patient Portal (Nginx, Single Page Application)
- Staff Dashboard (Nginx, Single Page Application)
- API Gateway (Kong / Envoy)
- Core Clinical & Billing Services (Go / Java / Spring Boot, PostgreSQL, Kafka / RabbitMQ)
- Interoperability & Analytics Gateway Container (HAPI FHIR JPA Server, HL7 FHIR)
- FHIR API Facade Component (HAPI FHIR JPA Server / Java)
- HL7 v2 to FHIR Adapter Component (Apache Camel)
- Audit & Compliance Interceptor Component (Custom Spring Boot Middleware)
- Break-Glass Authorization Component (Open Policy Agent / Java)
- External Systems: Identity Provider (IdP), Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Public Health Authority / Regulatory Registry

## Relationships
- API Gateway -> Interoperability & Analytics Gateway Container: Routes interoperability traffic [mTLS / Istio]
- API Gateway -> FHIR API Facade: Routes external interoperability traffic [mTLS / gRPC]
- FHIR API Facade <-> Lab & Imaging Systems: Exchanges clinical data [HL7 FHIR over HTTPS]
- Interoperability & Analytics Gateway Container -> Regulatory Registry: Sends regulatory data [HTTPS]
- FHIR API Facade -> Break-Glass Authorization Component: Validates emergency access override [gRPC]
- Break-Glass Authorization Component -> Audit & Compliance Interceptor: Dispatches high-priority security alerts [Kafka]
- Audit & Compliance Interceptor -> Core Clinical Services: Persists immutable audit logs [Kafka]

## Technology Stack
- HAPI FHIR JPA Server: Provides robust HL7 FHIR resource management and RESTful capabilities.
- Apache Camel: Facilitates reliable translation of legacy HL7 v2 messaging formats to modern FHIR bundles.
- Open Policy Agent (OPA): Enables declarative evaluation of clinical break-glass emergency policies.
- Kafka / RabbitMQ: Ensures asynchronous, reliable event streaming for audit logs and system integration.
- PostgreSQL: Provides secure, persistent relational data storage for core clinical services.
- Nginx: Serves static Single Page Applications for patient and staff interfaces.

## Rationale
This architecture uses a containerized, decoupled approach to meet the strict 99.99% availability and hybrid cloud performance targets. Dedicated interoperability and security components ensure HIPAA/GDPR compliance and 10-year data retention without compromising clinical workflow speeds.