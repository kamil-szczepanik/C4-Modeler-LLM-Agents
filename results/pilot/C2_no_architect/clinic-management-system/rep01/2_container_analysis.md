## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and strict data segregation for clinical and financial workloads.

## Key Elements
- Users: Front Desk Administrator, Clinician, Billing Specialist, Patient
- Containers: Patient Registration, Appointment Scheduling, EMR, Billing & Claims, HL7 FHIR Interoperability, Patient Portal
- External Systems: External Lab & Imaging Systems
- Infrastructure: On-premise Kubernetes clusters, AWS `eu-central-1`

## Relationships
- Users access containers via HTTPS (TLS 1.3) with OAuth2/OIDC Multi-Factor Authentication.
- Containers communicate via internal gRPC and REST APIs secured with Mutual TLS (mTLS).
- HL7 FHIR Interoperability container integrates with External Lab & Imaging Systems via HL7 FHIR APIs.
- Databases replicate across hybrid boundaries using encrypted distributed storage.

## Technology Stack
- Kubernetes: Container orchestration for hybrid multi-cluster deployment with HPA.
- Istio Service Mesh: Manages mTLS, zero-trust network policies, and egress filtering.
- Prometheus & Grafana: Real-time metrics and monitoring.
- Falco: Real-time container runtime security and anomaly detection.
- Cosign: Immutable container image signing for supply chain security.
- AES-256 & KMS: Encryption at rest for persistent volumes and compliance.

## Rationale
The hybrid architecture utilizes multi-cluster Kubernetes and automated failover to guarantee 99.99% availability and meet active-active uptime requirements. Segregating billing and EMR containers ensures financial downtimes never compromise critical patient care delivery or data security.