## Overview
The Clinic Management System is a resilient, hybrid-cloud clinical IT platform designed to handle patient records, scheduling, and billing securely. It utilizes containerized microservices protected by Envoy sidecar proxies to maintain 99.99% availability and HIPAA/GDPR compliance.

## Key Elements
* Patients, Practitioners, Administrators (Users)
* API Gateway Container, Core Domain Containers, Read-Model / Query Container, Integration / Adapter Container, Background Worker Container, Data Archival & Migration Container, Session & State Management Container
* Envoy Sidecars (Envoy Proxy instances for mTLS, circuit breaking, and telemetry)
* Asynchronous Message Broker (Apache Kafka / RabbitMQ)
* External Systems: Insurance Providers, External Labs/Imaging, Identity & Access Management (IAM), Centralized Audit Logging Service

## Relationships
* Users to API Gateway Container via HTTPS (TLS 1.3, Multi-Factor Authentication)
* API Gateway Container to Core Domain Containers via gRPC / mTLS (enforced by Envoy Sidecars)
* Core Domain Containers to Asynchronous Message Broker via TCP / AMQP / Kafka Protocol
* Integration / Adapter Container to External Labs/Imaging via HL7 FHIR APIs (REST/HTTPS)
* Envoy Sidecars to Centralized Audit Logging Service via gRPC for distributed tracing telemetry

## Technology Stack
* Kubernetes (on-prem-k8s and AWS eu-central-1): Hybrid cloud orchestration ensuring high availability.
* Envoy Proxy: Sidecar pattern for mTLS enforcement, weighted traffic shifting, and circuit breaking.
* Apache Kafka / RabbitMQ: Asynchronous messaging for decoupled microservice communication.
* Redis: In-memory data store for session and state management.
* Cert-Manager / Vault: Automated short-lived certificate rotation for zero-trust security.

## Rationale
* The architecture uses Envoy sidecars and Kubernetes active-active deployment to meet the strict 99.99% availability and <1s P95 EMR performance requirements.
* Strict mTLS enforcement, automated certificate rotation, and GitOps-driven configurations ensure continuous HIPAA and GDPR compliance.