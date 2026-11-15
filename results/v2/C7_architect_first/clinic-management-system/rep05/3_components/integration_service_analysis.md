## Overview
The Clinic Management System is an enterprise healthcare platform that securely manages patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high availability, stringent regulatory compliance, and robust interoperability for medium-sized hospitals and clinics.

## Key Elements
- Patients, Clinicians, Hospital Administrators
- API Gateway (Kong, Nginx, Envoy sidecar)
- Patient Portal Service, Patient & Scheduling Service, EMR Service, Billing Service, Integration Service (Apache Camel)
- Integration Service Components: FHIR Route Engine, HL7 v2/v3 Adapter, Kafka Event Publisher, Resilience & DLQ Handler, Payload Masking & Audit Interceptor
- PostgreSQL Databases with read replicas
- Apache Kafka Event Broker
- HashiCorp Vault
- External Systems: Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateways/Insurance Clearinghouses

## Relationships
- API Gateway -> Integration Service: Routes requests [gRPC / Internal Mesh with mTLS]
- FHIR Route Engine -> External Lab & Imaging Systems: Exchanges clinical data [HTTPS / REST / HL7 FHIR APIs]
- FHIR Route Engine -> Payload Masking & Interceptor: Passes clinical payloads [In-memory]
- Payload Masking & Interceptor -> Kafka Event Publisher: Forwards sanitized events [In-memory]
- FHIR Route Engine -> Resilience & DLQ Handler: Delegates failures [In-memory]
- Resilience & DLQ Handler -> Apache Kafka: Publishes encrypted poison messages to DLQ [TCP / TLS]
- Integration Service -> PostgreSQL Databases: Reads and writes clinical data [TCP / TLS]

## Technology Stack
- Node.js / TypeScript: Powers lightweight patient portal and scheduling services
- Java / Spring Boot: Runs the high-performance EMR service and Apache Camel Integration Service
- Python / FastAPI: Implements the billing and claims service
- Apache Camel: Orchestrates enterprise integration patterns and HL7 FHIR transformations
- Apache Kafka: Handles high-throughput asynchronous messaging and DLQ management
- PostgreSQL: Provides persistent relational data storage with read replicas
- Kubernetes & HashiCorp Vault: Delivers containerized orchestration (on-premise and AWS `eu-central-1`) and secure secret injection

## Rationale
The hybrid cloud architecture leverages active-active Kubernetes clusters to guarantee 99.99% availability and meet stringent HIPAA/GDPR data protection standards. Apache Camel combined with HL7 FHIR APIs ensures robust clinical interoperability while maintaining low-latency processing and zero data loss.