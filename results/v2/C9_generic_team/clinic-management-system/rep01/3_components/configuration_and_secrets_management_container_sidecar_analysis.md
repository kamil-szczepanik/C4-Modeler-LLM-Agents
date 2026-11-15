## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely manage patient admissions, electronic medical records, appointments, and billing. It provides high availability (99.99%) and strict HIPAA and GDPR compliance across on-premise Kubernetes and AWS (`eu-central-1`).

## Key Elements
*   Configuration and Secrets Management Sidecar (Vault / Kubernetes Secrets)
*   Core Domain Containers (Microservices / Kubernetes)
*   API Gateway / Reverse Proxy Container
*   Integration Engine Container (HL7 FHIR translator)
*   Asynchronous Event Bus Container (Kafka / RabbitMQ)
*   Shared Observability & Telemetry Container (Prometheus, Fluentbit, OpenTelemetry)

## Relationships
*   Core Domain Containers communicate with the Configuration and Secrets Management Sidecar via restricted local loopback Unix domain sockets / shared memory.
*   Configuration and Secrets Management Sidecar interacts with upstream Vault / Kubernetes Secrets using HTTPS.
*   API Gateway routes incoming client traffic to Core Domain Containers using HTTP/REST and gRPC.
*   Core Domain Containers communicate asynchronously via Kafka / RabbitMQ.
*   Integration Engine Container connects external Lab and Imaging Systems via HL7 FHIR APIs.

## Technology Stack
*   Kubernetes (on-prem-k8s and AWS `eu-central-1`): Container orchestration providing active-active high availability (≥ 99.99%).
*   HashiCorp Vault / Kubernetes Secrets: Secure backend for encrypted configuration and credential management.
*   JSON Schema: Typed validation contracts for local configuration parsing.
*   Unix Domain Sockets: Secure intra-pod communication between sidecar and core containers.
*   Prometheus, Fluentbit, OpenTelemetry: Observability and audit logging for HIPAA/GDPR compliance.

## Rationale
*   The hybrid Kubernetes infrastructure with sidecar isolation ensures 99.99% uptime and zero-trust security required for sensitive clinical EMR data.
*   Local sidecar caching, Unix domain sockets, and fail-secure circuit breakers guarantee low-latency performance (< 1s EMR load) while strictly enforcing HIPAA/GDPR compliance.