## Overview
The Clinic Management System is a hybrid cloud clinical IT platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high availability and strict compliance for medium-sized hospitals and clinics.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Officers
- API Gateway (Kong / Nginx)
- Patient-Facing UI (React / Next.js)
- Clinical Core Services & Billing Services (Spring Boot / Java)
- Interoperability Service (Apache Camel / Node.js)
- Route Orchestrator, FHIR Transformer & Validator, Outbound Security & Auth Agent, Resiliency & DLQ Handler, Idempotency Store (Redis), Operational Metrics Exporter
- External Lab & Imaging Systems, Payment Gateway, Identity Provider (IdP)

## Relationships
- Patient-Facing UI -> API Gateway: HTTPS/REST [TLS 1.3]
- Clinical Core / Billing Services -> Interoperability Service: Internal RPC [gRPC, mTLS]
- Interoperability Service -> External Lab & Imaging Systems: HL7 FHIR REST APIs [mTLS, SMART-on-FHIR, TLS 1.3]
- Route Orchestrator -> Idempotency Store: Cache lookup [Redis RESP, TLS]
- Operational Metrics Exporter -> Monitoring Stack: Metrics scraping [Prometheus, HTTP]

## Technology Stack
- Spring Boot / Java: Powers core clinical and billing business logic for high performance.
- Apache Camel / Node.js: Orchestrates enterprise integration patterns in the Interoperability Service.
- Redis: Fast-lookup cache ensuring request idempotency via unique accession numbers.
- RabbitMQ / Kafka: Powers the Dead-Letter Queue (DLQ) for resilient failure handling.
- HashiCorp Vault: Secures and injects runtime API keys and OAuth2 client credentials.
- OpenTelemetry & Prometheus: Delivers distributed tracing, metrics, and alerting.

## Rationale
The hybrid architecture utilizes on-premises Kubernetes and AWS (eu-central-1) to meet stringent HIPAA and GDPR data regulations while achieving 99.99% availability. Strict protocol controls (mTLS, TLS 1.3, SMART-on-FHIR) and resilient integration patterns protect sensitive health data and ensure seamless clinical workflows.