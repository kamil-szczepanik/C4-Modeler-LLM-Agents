## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for medium-sized hospitals and clinics using a hybrid cloud architecture. It ensures high availability, 10-year data retention, and strict HIPAA and GDPR compliance.

## Key Elements
- Users: Patients, Receptionists, Clinicians, Billing Specialists
- External Systems: Identity Provider, Payment Gateway & Insurance Clearinghouse, External Lab & Imaging Systems
- Containers: API Gateway (Envoy / NGINX), Web Application Container (React / Next.js), Clinical & EMR Core Container (Spring Boot / Java), Billing & Claims Container (Node.js / Express), HL7 FHIR Integration Container (Apache Camel), Edge Sync Container (Go Daemon), Primary DB & Audit Store (PostgreSQL with Patroni)
- HL7 FHIR Integration Components: FHIR API Route Controller, Data Transformation & Mapping Engine (HAPI FHIR / Java), Dead-Letter & Retry Manager, External Connector Client, Audit & Compliance Publisher Component

## Relationships
- Clinical & EMR Core Container -> HL7 FHIR Integration Container: Internal communication [gRPC]
- HL7 FHIR Integration Container -> Lab & Imaging Systems: External lab data exchange [HL7 FHIR APIs, TLS 1.3, mTLS]
- HL7 FHIR Integration Container -> Primary DB & Audit Store: Audit event publishing [JDBC / TLS]

## Technology Stack
- Apache Camel: Integration engine for routing and transformation due to robust enterprise messaging features.
- HAPI FHIR / Java: Schema validation and resource mapping for clinical interoperability.
- PostgreSQL with Patroni: Highly available relational storage supporting ACID and HIPAA audit requirements.
- Kubernetes & Kafka: Container orchestration and autoscaling driven by queue depth.
- Resilience4j: Circuit breaking for third-party lab integrations to preserve core uptime.

## Rationale
The hybrid architecture distributes workloads across on-premises Kubernetes and AWS eu-central-1 to guarantee 99.99% active-active availability. Decoupled integration patterns and strict security controls satisfy HIPAA, GDPR, and real-time clinical performance requirements.