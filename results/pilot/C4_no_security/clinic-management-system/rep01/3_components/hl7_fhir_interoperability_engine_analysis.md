## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, 10-year data retention, and strict HIPAA and GDPR compliance across hybrid cloud environments.

## Key Elements
- Patients, Clinical Staff, and Hospital Administrators
- External Lab and Imaging Systems, Third-Party Insurance Clearinghouses
- Global Anycast Load Balancer and API Gateways (Kong)
- Patient Portal (Node.js, React)
- EMR & Scheduling Service (Java Spring Boot)
- Billing & Insurance Claim Service (Python FastAPI)
- HL7 FHIR Interoperability Engine (Apache Camel)
- Database Tier (PostgreSQL with PgBouncer, AES-256)
- Messaging & Audit Layer (Apache Kafka, FluentBit, S3)
- Infrastructure & Mesh (Kubernetes, AWS eu-central-1, on-prem-k8s, Envoy sidecar)

## Relationships
- Patient Portal -> Global Anycast Load Balancer: HTTPS/TLS 1.3
- Global Anycast Load Balancer -> EMR & Scheduling Service: gRPC over HTTP/2
- EMR & Scheduling Service -> Database Tier: PostgreSQL wire protocol with TLS
- HL7 FHIR Interoperability Engine -> External Lab and Imaging Systems: HL7 FHIR APIs over persistent TCP connections
- HL7 FHIR Interoperability Engine -> Messaging & Audit Layer: Kafka Protocol over TCP

## Technology Stack
- Node.js & React: Powers the patient portal for responsive, interactive UI.
- Java Spring Boot: Handles EMR and scheduling with high performance and reliability.
- Python FastAPI: Provides rapid, asynchronous API endpoints for billing and insurance claims.
- Apache Camel: Acts as the core integration engine for HL7 and FHIR transformations.
- PostgreSQL with PgBouncer: Manages relational data persistence with connection pooling and AES-256 encryption.
- Apache Kafka & S3: Handles asynchronous event-driven messaging and long-term audit logging.
- Kubernetes & Envoy: Orchestrates hybrid cloud containers with secure service-mesh traffic management.

## Rationale
The hybrid Kubernetes architecture guarantees 99.99% active-active availability and resilient failover between on-premise and AWS regions. Technologies like Apache Kafka, PostgreSQL with AES-256, and Envoy sidecars fulfill rigorous HIPAA security, auditability, and interoperability mandates.