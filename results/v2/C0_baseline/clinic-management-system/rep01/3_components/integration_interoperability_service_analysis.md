## Overview
[The Clinic Management System manages patient admissions, EMR, scheduling, and billing for medium-sized healthcare facilities. It delivers high-availability, HIPAA/GDPR-compliant clinical IT operations across a hybrid on-premises and AWS cloud environment.]

## Key Elements
* Patients / Consumers, Receptionists, Clinicians, Billing Specialists, Clinic Administrators, Compliance Auditors
* API Gateway / Reverse Proxy (Kong / NGINX Ingress)
* Patient Portal (Next.js with TypeScript)
* Core Clinical Service (Java with Spring Boot)
* Billing & Scheduling Service (Node.js / TypeScript)
* Integration / Interoperability Service (Apache Camel / Spring Boot)
* Data Storage Layer (PostgreSQL with AES-256 and WORM audit storage)
* Messaging & Observability Infrastructure (Apache Kafka, Prometheus, Grafana, OpenTelemetry, Istio, HashiCorp Vault, ArgoCD)
* FHIR Ingress/Egress Router, Data Transformation Engine, DLQ Manager, Audit Interceptor, Consent & Policy Enforcement (Open Policy Agent)

## Relationships
* Core Clinical Service <-> Integration / Interoperability Service: Exchanges domain data [gRPC with mTLS via Istio]
* Billing & Scheduling Service <-> Integration / Interoperability Service: Exchanges domain data [gRPC with mTLS via Istio]
* FHIR Ingress/Egress Router -> Lab & Imaging Systems: External data exchange [HL7 FHIR REST over HTTPS]
* FHIR Ingress/Egress Router -> Consent & Policy Enforcement: Validates consent scopes [gRPC]
* DLQ Manager -> Messaging & Observability Infrastructure: Streams failure events [Apache Kafka]
* Data Transformation Engine -> WORM Audit Storage: Streams cryptographic audit metadata [gRPC/TLS]

## Technology Stack
* Java Spring Boot & Node.js: Provides robust, scalable backend microservices
* Apache Camel: Executes HL7 FHIR data transformations and routing
* Open Policy Agent (OPA): Enforces zero-trust patient consent and GDPR/HIPAA policies via sidecar
* Apache Kafka: Ensures durable messaging, backpressure management, and dead-letter queue processing
* PostgreSQL & WORM Storage: Secures relational data with AES-256 encryption and immutable compliance auditing
* Istio & HashiCorp Vault: Secures service meshes with mTLS and dynamic secret injection

## Rationale
[This architecture uses containerized microservices combined with event-driven messaging to achieve 99.99% availability and low-latency EMR performance. Strict boundary enforcement, cryptographic auditing, and OPA policy integration satisfy stringent HIPAA and GDPR compliance mandates.]