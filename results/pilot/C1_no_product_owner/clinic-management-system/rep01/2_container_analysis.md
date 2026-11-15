## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, appointments, and billing. It provides high availability, secure interoperability, and strict adherence to HIPAA and GDPR compliance mandates.

## Key Elements
* Patients & Clinic Staff (Users)
* External Labs, Imaging Systems, & Third-Party Insurance Gateways (External Systems)
* API Gateway (NGINX/Kong)
* Identity Service (Keycloak)
* Patient & EMR Service, Appointment Service, Billing Service (Spring Boot containers)
* HL7 FHIR Integration Engine (Apache Camel)
* Event Broker (Apache Kafka)
* Primary Database & Tiered Storage (PostgreSQL & S3-compatible WORM storage)
* Audit Logging Service

## Relationships
* Users to API Gateway via HTTPS/TLS 1.3
* Microservices to Identity Service via OAuth2/OIDC and mTLS (Istio)
* Patient & EMR Service to Event Broker (Apache Kafka) via SASL/SCRAM
* HL7 FHIR Integration Engine to External Labs and Imaging Systems via HL7 FHIR APIs
* Billing Service to Third-Party Insurance Gateways via HTTPS

## Technology Stack
* Hybrid Kubernetes (AWS EKS & On-Premises K8s) managed via ArgoCD for GitOps
* Java / Spring Boot for core business microservices
* PostgreSQL with Patroni/Raft for primary-replica database deployment
* Apache Kafka for asynchronous event-driven messaging
* Apache Camel for HL7 FHIR integration
* Istio Service Mesh for mTLS and east-west traffic security
* OpenTelemetry & Prometheus for distributed tracing and metrics

## Rationale
The hybrid Kubernetes architecture with active-replica PostgreSQL and Kafka decoupling ensures 99.99% uptime and sub-second EMR load performance. Strict mTLS, client-side encryption, and S3 WORM storage satisfy rigorous HIPAA, GDPR, and 10-year data retention mandates.