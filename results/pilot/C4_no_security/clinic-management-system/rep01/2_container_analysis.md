## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMR, scheduling, and billing for medium-sized clinics. It ensures HIPAA/GDPR compliance, 99.99% availability, and ten-year data retention.

## Key Elements
* Patients, Clinical Staff, Hospital Administrators
* Global Anycast Load Balancer and API Gateways (Kong)
* Patient Portal (Node.js, React)
* EMR & Scheduling Service (Java Spring Boot)
* Billing & Insurance Claim Service (Python FastAPI)
* HL7 FHIR Interoperability Engine (Apache Camel)
* Database Tier (PostgreSQL with PgBouncer)
* Messaging & Audit Layer (Apache Kafka, FluentBit, S3)
* Infrastructure & Mesh (Kubernetes, AWS `eu-central-1`, on-prem-k8s, Envoy sidecar)

## Relationships
* Users access the system via HTTPS through Kong API Gateway and Global Anycast Load Balancer.
* Patient Portal communicates with backend services via gRPC over mutual TLS (mTLS).
* EMR and Billing services interact asynchronously via Apache Kafka events.
* HL7 FHIR engine connects to external lab and imaging systems using HL7 FHIR APIs over persistent TCP connections.
* Core services persist state to PostgreSQL clusters using encrypted TCP connections.

## Technology Stack
* Go / Kong: API Gateway for secure high-performance ingress routing.
* Node.js & React: Patient portal for isolated, decoupled frontend administration.
* Java Spring Boot: Core EMR and scheduling for robust transactional integrity.
* Python FastAPI: Dedicated billing service for optimized insurance workflows.
* PostgreSQL (AES-256): Primary data store with row-level security and PgBouncer pooling.
* Apache Kafka: Asynchronous event streaming ensuring fault tolerance and audit trails.
* Kubernetes & ArgoCD: Hybrid deployment orchestration and GitOps synchronization across on-prem and AWS `eu-central-1`.
* Envoy & OpenTelemetry: Service mesh for mTLS and distributed tracing meeting sub-second P95 targets.

## Rationale
This hybrid architecture isolates clinical and billing workflows to guarantee fault tolerance, cash flow protection, and sub-second EMR performance. Utilizing Kubernetes, Kafka, and multi-region redundancy satisfies strict 99.99% uptime, encryption, and ten-year audit retention mandates.