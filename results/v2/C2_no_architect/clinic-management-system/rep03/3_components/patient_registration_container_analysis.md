## Overview
The Patient Registration Container manages patient admissions, onboarding, and demographic data capture for the Clinic Management System. It ensures secure, high-availability registration workflows for front-end users while maintaining strict HIPAA and GDPR compliance.

## Key Elements
- Front Desk Staff & Patients (Primary Users)
- Patient Registration Container (Kubernetes Microservice)
- Istio Ingress Controller (Ingress Routing)
- PostgreSQL/MySQL Hybrid Databases (Persistence Layer with Read-Replicas)
- WORM-Compliant Log Storage (Audit Logging)
- HashiCorp Vault / Kubernetes Secrets Store CSI (Secret Management)

## Relationships
- Istio Ingress Controller -> Patient Registration Container: Routes authenticated traffic via mTLS
- Patient Registration Container -> PostgreSQL/MySQL Hybrid Databases: Persists and queries demographic data via TCP/AES-256
- Patient Registration Container -> WORM-Compliant Log Storage: Sends asynchronous audit logs via gRPC/TLS

## Technology Stack
- Kubernetes: Container orchestration and resource management ensuring high availability
- Istio Service Mesh: Manages zero-trust service-to-service communication and canary deployments
- OpenTelemetry: Distributed tracing for latency monitoring without exposing PHI
- HashiCorp Vault: Dynamic secret management for credential rotation

## Rationale
This architecture uses microservices on Kubernetes with encrypted data storage to achieve 99.99% availability and stringent HIPAA/GDPR compliance. It separates patient registration from downstream clinical workflows to optimize performance and reduce security risks.