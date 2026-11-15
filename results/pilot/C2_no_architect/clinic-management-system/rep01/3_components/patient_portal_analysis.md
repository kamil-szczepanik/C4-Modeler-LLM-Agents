## Overview
The Patient Portal is a secure, patient-facing subsystem of the Clinic Management System that empowers outpatients to manage appointments, view electronic medical records, and handle billing. It ensures high availability and regulatory compliance for medium-sized clinics and hospitals.

## Key Elements
- Patients (Outpatients, Accessibility-impaired users)
- Patient Portal Container (Kubernetes, REST API / gRPC)
- Appointment Scheduling Container (Kubernetes)
- EMR Container (Kubernetes, Encrypted Distributed Storage)
- External Lab & Imaging Systems (HL7 FHIR APIs)
- Ingress Layer with WAF and Edge Rate-Limiting

## Relationships
- Patient -> Patient Portal: Views appointments, lab results, and health records [HTTPS (TLS 1.3), OAuth2/OIDC MFA]
- Patient Portal -> Appointment Scheduling: Books and views appointments [gRPC / REST via mTLS]
- Patient Portal -> EMR: Retrieves health records and lab results [gRPC / REST via mTLS]
- Patient Portal -> External Lab & Imaging Systems: Exchanges health data [HL7 FHIR APIs]

## Technology Stack
- Kubernetes & ArgoCD: Hybrid orchestration (on-prem and AWS `eu-central-1`) and GitOps-driven canary deployments ensuring 99.99% availability.
- OAuth2/OIDC & JWT: Short-lived access tokens (15 minutes) with strict audience validation for authentication.
- Prometheus & OpenTelemetry: Custom metrics-driven Horizontal Pod Autoscalers and distributed tracing for latency monitoring.
- AES-256 & Column-Level Encryption: End-to-end data protection for Protected Health Information (PHI) at rest and in transit.

## Rationale
This architecture satisfies HIPAA and GDPR compliance mandates through robust encryption, strict zero-trust ACLs, and comprehensive audit logging. The hybrid cloud Kubernetes deployment with geo-distributed ingress and custom metric auto-scaling guarantees the required 99.99% uptime and low-latency performance.