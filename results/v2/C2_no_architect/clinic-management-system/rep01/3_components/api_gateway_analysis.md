## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It provides secure, high-availability clinical IT operations while maintaining strict HIPAA and GDPR compliance.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists, Hospital Administrators
- Insurance Clearinghouses, External Labs/Imaging Vendors
- API Gateway (Kubernetes Ingress / Gateway API)
- WAF Container
- Patient Portal Container
- EMR Container, Scheduling Container, Billing Container, Notification Container, Analytics & Reporting Container
- PostgreSQL Databases (Patroni/etcd), Apache Kafka / RabbitMQ Event Broker, Immutable Audit Storage Sink, HashiCorp Vault

## Relationships
- WAF Container -> API Gateway: Forwards filtered traffic via HTTPS
- API Gateway -> Patient Portal, EMR, Scheduling, Billing, and Analytics Containers: Routes client requests via HTTPS with mTLS (SPIFFE/SPIRE)
- API Gateway -> Redis Cache: Performs local authorization caching and token validation
- API Gateway -> HashiCorp Vault: Retrieves secrets and manages automated TLS lifecycles via cert-manager

## Technology Stack
- Kubernetes & Hybrid Cloud (on-prem-k8s and eu-central-1): Enables high availability (99.99%) and active-active multi-region deployment.
- API Gateway (Kubernetes Ingress / Gateway API): Enforces OWASP top 10 guardrails, OAuth2/OIDC validation, and persona-based rate limiting.
- HashiCorp Vault & cert-manager: Manages AES-256 encryption at rest, SVID generation, and automated TLS certificate rotation.
- Distributed Redis: Provides fast local authorization caching to maintain sub-second P95 latencies.
- OpenTelemetry & Prometheus: Captures distributed traces and metrics across the zero-trust mesh.

## Rationale
This architecture uses a hybrid active-active deployment with an advanced API Gateway to meet strict 99.99% availability and sub-second P95 performance constraints. Centralizing security, OAuth2 validation, rate limiting, and mTLS at the gateway guarantees HIPAA and GDPR compliance while protecting core microservices from volumetric and application-layer threats.