## Overview
The Clinic Management System is a hybrid cloud platform designed to streamline patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized clinics. It ensures high availability, strict data protection, and interoperability with external healthcare networks.

## Key Elements
- **Users**: Patients, Clinic Staff/Receptionists, Clinicians/Doctors, Billing Specialists, System Administrators
- **Frontend Container**: React, TypeScript, CDN, Nginx
- **API Gateway**: Kong / Envoy, Istio Service Mesh
- **Core Services Container**: Go, Spring Boot, Node.js
- **EMR Service Container**: Go, Spring Boot, Node.js
- **Integration Service Container**: Go, Spring Boot, Node.js, HL7 FHIR APIs
  - *FHIR Gateway Component* (HAPI FHIR library)
  - *Adapter & Transformation Engine* (Apache Camel / Go middleware)
  - *Outbox & Retry Dispatcher* (PostgreSQL outbox)
  - *Clearinghouse Adapter Component* (Go / Spring Boot)
  - *Integration Metrics Exporter* (Prometheus / Micrometer)
- **Notification Container**: Go, Spring Boot, Node.js
- **Audit & Compliance Container**: Go, Spring Boot, Node.js, Kafka (TLS + SASL)
- **Databases**: PostgreSQL (AES-256), ClickHouse
- **Message Broker**: Apache Kafka, RabbitMQ
- **External Systems**: Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP), Payment Gateway

## Relationships
- Frontend Container -> API Gateway: Manages client traffic [HTTPS, REST/GraphQL]
- API Gateway -> Core Services Container: Routes internal domain requests [gRPC / REST]
- Integration Service Container -> Lab & Imaging Systems: Exchanges clinical data [REST/HTTPS, HL7 FHIR over mTLS]
- Clearinghouse Adapter Component -> Insurance Clearinghouses: Submits claims and adjudications [REST/HTTPS over mTLS, X12 EDI]
- Integration Service Container -> Audit & Compliance Container: Streams audit events [Kafka, TLS + SASL]
- Integration Metrics Exporter -> System Monitoring: Scrapes failure telemetry [Prometheus, HTTP]

## Technology Stack
- **Languages/Frameworks**: Go, Spring Boot, Node.js, React, TypeScript for multi-service efficiency
- **API & Interoperability**: HL7 FHIR APIs, Apache Camel, X12 EDI for standardized healthcare data exchange
- **Messaging & Resilience**: Apache Kafka, RabbitMQ, local PostgreSQL outbox for guaranteed delivery and dead-letter queues
- **Security**: OAuth 2.0, SMART-on-FHIR, mTLS (TLS 1.3), AES-256 for HIPAA and GDPR compliance
- **Infrastructure**: Kubernetes (on-prem-k8s and eu-central-1), Kong/Envoy, Istio for hybrid-cloud high availability

## Rationale
The hybrid cloud architecture combines on-premises Kubernetes with AWS (eu-central-1) to satisfy stringent data residency and 99.99% active-active availability constraints. Specialized integration components, mTLS security, and robust outbox patterns ensure zero-loss interoperability with external medical systems while strictly maintaining HIPAA and GDPR compliance.